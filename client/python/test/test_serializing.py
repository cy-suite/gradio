from gradio import components

from gradio_client.serializing import COMPONENT_MAPPING


def test_check_component_fallback_serializers():
    for component_name, class_type in COMPONENT_MAPPING.items():
        if component_name == "dataset":  # cannot be instantiated without parameters
            continue
        component = components.get_component_instance(component_name)
        assert isinstance(component, class_type)
