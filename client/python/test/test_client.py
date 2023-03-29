import json

import pytest

from gradio_client import Client

HF_TOKEN = "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"  # Intentionally revealing this key for testing purposes


class TestPredictionsFromSpaces:
    @pytest.mark.flaky
    def test_numerical_to_label_space(self):
        client = Client("gradio-tests/titanic-survival")
        output = client.predict("male", 77, 10).result()
        assert json.load(open(output))["label"] == "Perishes"

    @pytest.mark.flaky
    def test_private_space(self):
        client = Client("gradio-tests/not-actually-private-space", hf_token=HF_TOKEN)
        output = client.predict("abc").result()
        assert output == "abc"


class TestEndpoints:
    @pytest.mark.flaky
    def test_numerical_to_label_space(self):
        client = Client("gradio-tests/titanic-survival")
        assert client.endpoints[0].get_info() == {
            "parameters": {
                "sex": ["Any", "", "Radio"],
                "age": ["Any", "", "Slider"],
                "fare_(british_pounds)": ["Any", "", "Slider"],
            },
            "returns": {"output": ["str", "filepath to json file", "Label"]},
        }
        assert client.view_api(return_info=True) == {
            "named_endpoints": {
                "predict": {
                    "parameters": {
                        "sex": ["Any", "", "Radio"],
                        "age": ["Any", "", "Slider"],
                        "fare_(british_pounds)": ["Any", "", "Slider"],
                    },
                    "returns": {"output": ["str", "filepath to json file", "Label"]},
                },
                "predict_1": {
                    "parameters": {
                        "sex": ["Any", "", "Radio"],
                        "age": ["Any", "", "Slider"],
                        "fare_(british_pounds)": ["Any", "", "Slider"],
                    },
                    "returns": {"output": ["str", "filepath to json file", "Label"]},
                },
                "predict_2": {
                    "parameters": {
                        "sex": ["Any", "", "Radio"],
                        "age": ["Any", "", "Slider"],
                        "fare_(british_pounds)": ["Any", "", "Slider"],
                    },
                    "returns": {"output": ["str", "filepath to json file", "Label"]},
                },
            },
            "unnamed_endpoints": {},
        }

    @pytest.mark.flaky
    def test_private_space(self):
        client = Client("gradio-tests/not-actually-private-space", hf_token=HF_TOKEN)
        assert len(client.endpoints) == 3
        assert len([e for e in client.endpoints if e.is_valid]) == 2
        assert len([e for e in client.endpoints if e.is_valid and e.api_name]) == 1
        assert client.endpoints[0].get_info() == {
            "parameters": {"x": ["Any", "", "Textbox"]},
            "returns": {"output": ["Any", "", "Textbox"]},
        }
        assert client.view_api(return_info=True) == {
            "named_endpoints": {
                "predict": {
                    "parameters": {"x": ["Any", "", "Textbox"]},
                    "returns": {"output": ["Any", "", "Textbox"]},
                }
            },
            "unnamed_endpoints": {
                2: {
                    "parameters": {"parameter_0": ["Any", "", "Dataset"]},
                    "returns": {
                        "x": ["Any", "", "Textbox"],
                        "output": ["Any", "", "Textbox"],
                    },
                }
            },
        }
