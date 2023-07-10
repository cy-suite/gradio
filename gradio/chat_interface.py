"""
This file defines a useful high-level abstraction to build Gradio chatbots: ChatInterface.
"""


from __future__ import annotations

from typing import Callable

from gradio_client.documentation import document, set_documentation_group

from gradio.blocks import Blocks
from gradio.components import (
    Button,
    Chatbot,
    Markdown,
    State,
    Textbox,
)
from gradio.helpers import create_examples as Examples  # noqa: N812
from gradio.layouts import Group, Row
from gradio.themes import ThemeClass as Theme

set_documentation_group("interface")


@document()
class ChatInterface(Blocks):
    def __init__(
        self,
        fn: Callable,
        *,
        chatbot: Chatbot | None = None,
        textbox: Textbox | None = None,
        examples: list[str] | None = None,
        cache_examples: bool | None = None,
        title: str | None = None,
        description: str | None = None,
        theme: Theme | str | None = None,
        css: str | None = None,
        analytics_enabled: bool | None = None,
        submit_btn: str | None | Button = "Submit",
        retry_btn: str | None | Button = "🔄  Retry",
        delete_last_btn: str | None | Button = None,
        clear_btn: str | None | Button = "🗑️  Clear History",
    ):
        """
        Parameters:
            fn: the function to wrap the chat interface around. Should accept two parameters: a string input message and list of two-element lists of the form [[user_message, bot_message], ...] representing the chat history, and return a string response. See the Chatbot documentation for more information on the chat history format.
            chatbot: an instance of the gr.Chatbot component to use for the chat interface. If not provided, a default gr.Chatbot component will be created.
            textbox: an instance of the gr.Textbox component to use for the chat interface. If not provided, a default gr.Textbox component will be created.
            examples: sample inputs for the function; if provided, appear below the chatbot and can be clicked to populate the chatbot input.
            cache_examples: If True, caches examples in the server for fast runtime in examples. The default option in HuggingFace Spaces is True. The default option elsewhere is False.
            title: a title for the interface; if provided, appears above chatbot in large font. Also used as the tab title when opened in a browser window.
            description: a description for the interface; if provided, appears above the chatbot and beneath the title in regular font. Accepts Markdown and HTML content.
            theme: Theme to use, loaded from gradio.themes.
            css: custom css or path to custom css file to use with interface.
            analytics_enabled: Whether to allow basic telemetry. If None, will use GRADIO_ANALYTICS_ENABLED environment variable if defined, or default to True.
            submit_btn: Text to display on the submit button. If None, no button will be displayed. If a Button object, that button will be used.
            retry_btn: Text to display on the retry button. If None, no button will be displayed. If a Button object, that button will be used.
            delete_last_btn: Text to display on the delete last button. If None, no button will be displayed. If a Button object, that button will be used.
            clear_btn: Text to display on the clear button. If None, no button will be displayed. If a Button object, that button will be used.
        """
        super().__init__(
            analytics_enabled=analytics_enabled,
            mode="chat_interface",
            css=css,
            title=title or "Gradio",
            theme=theme,
        )
        self.fn = fn
        self.examples = examples
        self.cache_examples = cache_examples
        self.buttons: list[Button] = []
        self.history = []

        with self:
            if title:
                Markdown(
                    f"<h1 style='text-align: center; margin-bottom: 1rem'>{self.title}</h1>"
                )
            if description:
                Markdown(description)

            with Group():
                if chatbot:
                    self.chatbot = chatbot.render()
                else:
                    self.chatbot = Chatbot(label="Input")
                if textbox:
                    self.textbox = textbox.render() 
                else: 
                    self.textbox = Textbox(show_label=False, placeholder="Type a message...")
            
            with Row():
                for b, btn in enumerate([submit_btn, retry_btn, delete_last_btn, clear_btn]):
                    if btn:
                        if isinstance(btn, Button):
                            btn.render()
                        elif isinstance(btn, str):
                            btn = Button(btn, variant="primary" if b == 0 else "secondary")
                        else:
                            raise ValueError("The `submit_btn` parameter must be a gr.Button or a string")
                    self.buttons.append(btn)
                self.submit_btn, self.retry_btn, self.delete_last_btn, self.clear_btn = self.buttons
            
            if examples:
                self.examples_handler = Examples(
                    examples=examples,
                    inputs=self.textbox,
                    outputs=self.chatbot,
                    fn=self.fn,
                    cache_examples=self.cache_examples,
                )


            # self.stored_history = State()

            # # Invisible elements only used to set up the API
            # api_btn = Button(visible=False)
            # api_output_textbox = Textbox(visible=False, label="output")

            # self.buttons = [submit_btn, retry_btn, clear_btn]

            self.saved_input = State()

            self.textbox.submit(
                self._clear_and_save_textbox,
                [self.textbox],
                [self.textbox, self.saved_input],
                api_name=False,
                queue=False,
            ).then(
                self._submit_fn,
                [self.saved_input, self.chatbot],
                [self.chatbot],
                api_name=False,
            )

            self.submit_btn.click(
                self._clear_and_save_textbox,
                [self.textbox],
                [self.textbox, self.saved_input],
                api_name=False,
                queue=False,
            ).then(
                self._submit_fn,
                [self.saved_input, self.chatbot],
                [self.chatbot],
                api_name=False,
            )
            # delete_btn.click(self.delete_prev_fn, [self.chatbot], [self.chatbot, self.stored_input], queue=False, api_name=False)
            # retry_btn.click(self.delete_prev_fn, [self.chatbot], [self.chatbot, self.stored_input], queue=False, api_name=False).success(self.retry_fn, [self.chatbot, self.stored_input], [self.chatbot], api_name=False)
            # api_btn.click(self.submit_fn, [self.stored_history, self.textbox], [self.stored_history, api_output_textbox], api_name="chat")
            # clear_btn.click(lambda :[], None, self.chatbot, api_name="clear")

    def _clear_and_save_textbox(self, message):
        return "", message

    def _submit_fn(self, message: str, history: list[list[str]]):
        # Need to handle streaming case
        response = self.fn(message, history)
        history.append((message, response))
        return history

    def _delete_prev_fn(self, history):
        try:
            inp, _ = history.pop()
        except IndexError:
            inp = None
        return history, inp

    # def retry_fn(self, history, inp):
    #     if inp is not None:
    #         out = self.fn(history, inp)
    #         history.append((inp, out))
    #     return history
