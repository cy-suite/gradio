import os
from unittest.mock import patch

import pytest

import gradio as gr

os.environ["GRADIO_ANALYTICS_ENABLED"] = "False"


class TestExamples:
    def test_handle_single_input(self):
        examples = gr.Examples(["hello", "hi"], gr.Textbox())
        assert examples.processed_examples == [["hello"], ["hi"]]

        examples = gr.Examples([["hello"]], gr.Textbox())
        assert examples.processed_examples == [["hello"]]

        examples = gr.Examples(["test/test_files/bus.png"], gr.Image())
        assert examples.processed_examples == [[gr.media_data.BASE64_IMAGE]]

    def test_handle_multiple_inputs(self):
        examples = gr.Examples(
            [["hello", "test/test_files/bus.png"]], [gr.Textbox(), gr.Image()]
        )
        assert examples.processed_examples == [["hello", gr.media_data.BASE64_IMAGE]]

    def test_handle_directory(self):
        examples = gr.Examples("test/test_files/images", gr.Image())
        assert examples.processed_examples == [
            [gr.media_data.BASE64_IMAGE],
            [gr.media_data.BASE64_IMAGE],
        ]

    def test_handle_directory_with_log_file(self):
        examples = gr.Examples(
            "test/test_files/images_log", [gr.Image(label="im"), gr.Text()]
        )
        assert examples.processed_examples == [
            [gr.media_data.BASE64_IMAGE, "hello"],
            [gr.media_data.BASE64_IMAGE, "hi"],
        ]


class TestExamplesDataset:
    def test_no_headers(self):
        examples = gr.Examples("test/test_files/images_log", [gr.Image(), gr.Text()])
        assert examples.dataset.headers == []

    def test_all_headers(self):
        examples = gr.Examples(
            "test/test_files/images_log",
            [gr.Image(label="im"), gr.Text(label="your text")],
        )
        assert examples.dataset.headers == ["im", "your text"]

    def test_some_headers(self):
        examples = gr.Examples(
            "test/test_files/images_log", [gr.Image(label="im"), gr.Text()]
        )
        assert examples.dataset.headers == ["im", ""]


class TestProcessExamples:
    @pytest.mark.asyncio
    async def test_predict_example(self):
        io = gr.Interface(lambda x: "Hello " + x, "text", "text", examples=[["World"]])
        prediction = await io.examples_handler.predict_example(0)
        assert prediction[0] == "Hello World"

    @pytest.mark.asyncio
    async def test_coroutine_process_example(self):
        async def coroutine(x):
            return "Hello " + x

        io = gr.Interface(coroutine, "text", "text", examples=[["World"]])
        prediction = await io.examples_handler.predict_example(0)
        assert prediction[0] == "Hello World"

    @pytest.mark.asyncio
    async def test_caching(self):
        io = gr.Interface(
            lambda x: "Hello " + x,
            "text",
            "text",
            examples=[["World"], ["Dunya"], ["Monde"]],
        )
        io.launch(prevent_thread_lock=True)
        await io.examples_handler.cache_interface_examples()
        prediction = await io.examples_handler.load_from_cache(1)
        io.close()
        assert prediction[0] == "Hello Dunya"


def test_raise_helpful_error_message_if_providing_partial_examples(tmp_path):
    def foo(a, b):
        return a + b

    with patch("gradio.examples.CACHED_FOLDER", tmp_path):
        with pytest.warns(
            UserWarning,
            match="^Examples are being cached but not all input components have",
        ):
            with pytest.raises(Exception):
                gr.Interface(
                    foo,
                    inputs=["text", "text"],
                    outputs=["text"],
                    examples=[["foo"], ["bar"]],
                    cache_examples=True,
                )

        with pytest.warns(
            UserWarning,
            match="^Examples are being cached but not all input components have",
        ):
            with pytest.raises(Exception):
                gr.Interface(
                    foo,
                    inputs=["text", "text"],
                    outputs=["text"],
                    examples=[["foo", "bar"], ["bar", None]],
                    cache_examples=True,
                )

        def foo_no_exception(a, b=2):
            return a * b

        gr.Interface(
            foo_no_exception,
            inputs=["text", "number"],
            outputs=["text"],
            examples=[["foo"], ["bar"]],
            cache_examples=True,
        )

        def many_missing(a, b, c):
            return a * b

        with pytest.warns(
            UserWarning,
            match="^Examples are being cached but not all input components have",
        ):
            with pytest.raises(Exception):
                gr.Interface(
                    many_missing,
                    inputs=["text", "number", "number"],
                    outputs=["text"],
                    examples=[["foo", None, None], ["bar", 2, 3]],
                    cache_examples=True,
                )
