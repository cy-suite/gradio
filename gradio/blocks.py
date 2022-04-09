from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional, Tuple

from gradio import utils
from gradio.context import Context
from gradio.launchable import Launchable

if TYPE_CHECKING:  # Only import for type checking (is False at runtime).
    from gradio.components import Component


class Block:
    def __init__(self, without_rendering=False):
        if without_rendering:
            return
        self.render()

    def render(self):
        """
        Adds self into appropriate BlockContext
        """
        self._id = Context.id
        Context.id += 1
        if Context.block is not None:
            Context.block.children.append(self)
        if Context.root_block is not None:
            Context.root_block.blocks[self._id] = self
        self.events = []

    def set_event_trigger(
        self,
        event_name: str,
        fn: Callable,
        inputs: List[Component],
        outputs: List[Component],
        preprocess: bool = True,
        postprocess: bool = True,
        queue=False,
        no_target: bool = False,
    ) -> None:
        """
        Adds an event to the component's dependencies.
        Parameters:
            event_name: event name
            fn: Callable function
            inputs: input list
            outputs: output list
            preprocess: whether to run the preprocess methods of components
            postprocess: whether to run the postprocess methods of components
            no_target: if True, sets "targets" to [], used for Blocks "load" event
        Returns: None
        """
        # Support for singular parameter
        if not isinstance(inputs, list):
            inputs = [inputs]
        if not isinstance(outputs, list):
            outputs = [outputs]

        Context.root_block.fns.append((fn, preprocess, postprocess))
        Context.root_block.dependencies.append(
            {
                "targets": [self._id] if not no_target else [],
                "trigger": event_name,
                "inputs": [block._id for block in inputs],
                "outputs": [block._id for block in outputs],
                "queue": queue,
            }
        )


class BlockContext(Block):
    def __init__(self, visible: bool = True, css: Optional[Dict[str, str]] = None):
        """
        css: Css rules to apply to block.
        """
        self.children = []
        self.css = css if css is not None else {}
        self.visible = visible
        super().__init__()

    def __enter__(self):
        self.parent = Context.block
        Context.block = self
        return self

    def __exit__(self, *args):
        Context.block = self.parent

    def get_template_context(self):
        return {"css": self.css, "default_value": self.visible}

    def postprocess(self, y):
        return y


class Row(BlockContext):
    def __init__(self, visible: bool = True, css: Optional[Dict[str, str]] = None):
        """
        css: Css rules to apply to block.
        """
        super().__init__(visible, css)

    def get_template_context(self):
        return {"type": "row", **super().get_template_context()}


class Column(BlockContext):
    def __init__(self, visible: bool = True, css: Optional[Dict[str, str]] = None):
        """
        css: Css rules to apply to block.
        """
        super().__init__(visible, css)

    def get_template_context(self):
        return {
            "type": "column",
            **super().get_template_context(),
        }


class Tabs(BlockContext):
    def __init__(self, visible: bool = True, css: Optional[Dict[str, str]] = None):
        """
        css: css rules to apply to block.
        """
        super().__init__(visible, css)

    def change(self, fn: Callable, inputs: List[Component], outputs: List[Component]):
        """
        Parameters:
            fn: Callable function
            inputs: List of inputs
            outputs: List of outputs
        Returns: None
        """
        self.set_event_trigger("change", fn, inputs, outputs)


class TabItem(BlockContext):
    def __init__(
        self, label, visible: bool = True, css: Optional[Dict[str, str]] = None
    ):
        """
        css: Css rules to apply to block.
        """
        super().__init__(visible, css)
        self.label = label

    def get_template_context(self):
        return {"label": self.label, **super().get_template_context()}

    def change(self, fn: Callable, inputs: List[Component], outputs: List[Component]):
        """
        Parameters:
            fn: Callable function
            inputs: List of inputs
            outputs: List of outputs
        Returns: None
        """
        self.set_event_trigger("change", fn, inputs, outputs)


class Blocks(Launchable, BlockContext):
    def __init__(
        self,
        theme: str = "default",
        analytics_enabled: Optional[bool] = None,
        mode: str = "blocks",
    ):

        # Cleanup shared parameters with Interface
        self.save_to = None
        self.ip_address = utils.get_local_ip_address()
        self.api_mode = False
        self.theme = theme
        self.requires_permissions = False  # TODO: needs to be implemented
        self.enable_queue = False
        self.is_space = True if os.getenv("SYSTEM") == "spaces" else False
        self.mode = mode

        # For analytics_enabled and allow_flagging: (1) first check for
        # parameter, (2) check for env variable, (3) default to True/"manual"
        self.analytics_enabled = (
            analytics_enabled
            if analytics_enabled is not None
            else os.getenv("GRADIO_ANALYTICS_ENABLED", "True") == "True"
        )

        super().__init__()
        self.blocks = {}
        self.fns = []
        self.dependencies = []

    def render(self):
        self._id = Context.id
        Context.id += 1

    def process_api(self, data: Dict[str, Any], username: str = None) -> Dict[str, Any]:
        raw_input = data["data"]
        fn_index = data["fn_index"]
        fn, preprocess, postprocess = self.fns[fn_index]
        dependency = self.dependencies[fn_index]

        if preprocess:
            processed_input = [
                self.blocks[input_id].preprocess(raw_input[i])
                for i, input_id in enumerate(dependency["inputs"])
            ]
            predictions = fn(*processed_input)
        else:
            predictions = fn(*raw_input)
        if len(dependency["outputs"]) == 1:
            predictions = (predictions,)
        if postprocess:
            predictions = [
                self.blocks[output_id].postprocess(predictions[i])
                if predictions[i] is not None
                else None
                for i, output_id in enumerate(dependency["outputs"])
            ]
        return {"data": predictions}

    def get_template_context(self):
        return {"type": "column"}

    def get_config_file(self):
        config = {"mode": "blocks", "components": [], "theme": self.theme}
        for _id, block in self.blocks.items():
            config["components"].append(
                {
                    "id": _id,
                    "type": block.__class__.__name__.lower(),
                    "props": block.get_template_context()
                    if hasattr(block, "get_template_context")
                    else None,
                }
            )

        def getLayout(block):
            if not isinstance(block, BlockContext):
                return {"id": block._id}
            children = []
            for child in block.children:
                children.append(getLayout(child))
            return {"id": block._id, "children": children}

        config["layout"] = getLayout(self)
        config["dependencies"] = self.dependencies
        return config

    def __enter__(self):
        if Context.block is None:
            Context.root_block = self
        self.parent = Context.block
        Context.block = self
        return self

    def __exit__(self, *args):
        Context.block = self.parent
        if self.parent is None:
            Context.root_block = None
        else:
            self.parent.children.extend(self.children)

    def load(
        self, fn: Callable, inputs: List[Component], outputs: List[Component]
    ) -> None:
        """
        Adds an event for when the demo loads in the browser.

        Parameters:
            fn: Callable function
            inputs: input list
            outputs: output list
        Returns: None
        """
        self.set_event_trigger(
            event_name="load", fn=fn, inputs=inputs, outputs=outputs, no_target=True
        )
