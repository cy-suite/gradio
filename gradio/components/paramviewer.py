from __future__ import annotations

from typing import Literal, TypedDict

from gradio_client.documentation import document, set_documentation_group

from gradio.components.base import Component
from gradio.events import Events


class Parameter(TypedDict):
    type: str
    description: str
    default: str | None


set_documentation_group("component")


@document()
class ParamViewer(Component):
    """
    Displays an interactive table of parameters and their descriptions and default values with syntax highlighting. For each parameter,
    the user should provide a type (e.g. a `str`), a human-readable description, and a default value. Internally, this component
    is used to display the parameters of custom components in the Custom Component Gallery (https://www.gradio.app/custom-components/gallery).

    Preprocessing: passes value as a `dict[str, dict]`. The key in the outer dictionary is the parameter name, while the inner dictionary has keys "type", "description", and (optionally) "default" for each parameter.
    Postprocessing: expects a `dict[str, dict]` with the same format as the preprocessed value.
    Examples-format: a `dict[str, dict]` with the same format as the preprocessed value.
    """

    EVENTS = [
        Events.change,
        Events.upload,
    ]

    def __init__(
        self,
        value: dict[str, Parameter] | None = None,
        language: Literal["python", "typescript"] = "python",
        linkify: list[str] | None = None,
        every: float | None = None,
        render: bool = True,
    ):
        """
        Parameters:
            value: A list of dictionaries with keys "type", "description", and "default" for each parameter.
            language: The language to display the code in. One of "python" or "typescript".
            linkify: A list of strings to linkify. If any of these strings is found in the description, it will be rendered as a link.
            every: If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.
            render: If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.
        """
        self.value = value or {}
        self.language = language
        self.linkify = linkify
        super().__init__(
            every=every,
            value=value,
            render=render,
        )

    def preprocess(self, payload: dict[str, Parameter]) -> dict[str, Parameter]:
        """
        ADD DOCSTRING
        Parameters:
            payload: ADD DOCSTRING
        Returns:
            ADD DOCSTRING
        """
        return payload

    def postprocess(self, value: dict[str, Parameter]) -> dict[str, Parameter]:
        """
        ADD DOCSTRING
        Parameters:
            value: ADD DOCSTRING
        Returns:
            ADD DOCSTRING
        """
        return value

    def example_inputs(self):
        return {
            "array": {
                "type": "numpy",
                "description": "any valid json",
                "default": "None",
            }
        }

    def api_info(self):
        return {"type": {}, "description": "any valid json"}
