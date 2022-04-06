XRAY_CONFIG = {
    "mode": "blocks",
    "components": [
        {
            "id": 1,
            "type": "markdown",
            "props": {
                "default_value": "<h1>Detect Disease From Scan</h1>\n<p>With this model you can lorem ipsum</p>\n<ul>\n<li>ipsum 1</li>\n<li>ipsum 2</li>\n</ul>\n",
                "name": "markdown",
                "label": None,
                "css": {},
            },
        },
        {
            "id": 2,
            "type": "checkboxgroup",
            "props": {
                "choices": ["Covid", "Malaria", "Lung Cancer"],
                "default_value": [],
                "name": "checkboxgroup",
                "label": "Disease to Scan For",
                "css": {},
            },
        },
        {"id": 3, "type": "tabs", "props": {"css": {}, "default_value": True}},
        {
            "id": 4,
            "type": "tabitem",
            "props": {"label": "X-ray", "css": {}, "default_value": True},
        },
        {
            "id": 5,
            "type": "row",
            "props": {"type": "row", "css": {}, "default_value": True},
        },
        {
            "id": 6,
            "type": "image",
            "props": {
                "image_mode": "RGB",
                "shape": None,
                "source": "upload",
                "tool": "editor",
                "default_value": None,
                "name": "image",
                "label": None,
                "css": {},
            },
        },
        {
            "id": 7,
            "type": "json",
            "props": {"default_value": '""', "name": "json", "label": None, "css": {}},
        },
        {
            "id": 8,
            "type": "button",
            "props": {
                "default_value": "Run",
                "name": "button",
                "label": None,
                "css": {"background-color": "red", "--hover-color": "orange"},
            },
        },
        {
            "id": 9,
            "type": "tabitem",
            "props": {"label": "CT Scan", "css": {}, "default_value": True},
        },
        {
            "id": 10,
            "type": "row",
            "props": {"type": "row", "css": {}, "default_value": True},
        },
        {
            "id": 11,
            "type": "image",
            "props": {
                "image_mode": "RGB",
                "shape": None,
                "source": "upload",
                "tool": "editor",
                "default_value": None,
                "name": "image",
                "label": None,
                "css": {},
            },
        },
        {
            "id": 12,
            "type": "json",
            "props": {"default_value": '""', "name": "json", "label": None, "css": {}},
        },
        {
            "id": 13,
            "type": "button",
            "props": {
                "default_value": "Run",
                "name": "button",
                "label": None,
                "css": {},
            },
        },
        {
            "id": 14,
            "type": "textbox",
            "props": {
                "lines": 1,
                "placeholder": None,
                "default_value": "",
                "name": "textbox",
                "label": None,
                "css": {},
            },
        },
    ],
    "theme": "default",
    "layout": {
        "id": 0,
        "children": [
            {"id": 1},
            {"id": 2},
            {
                "id": 3,
                "children": [
                    {
                        "id": 4,
                        "children": [
                            {"id": 5, "children": [{"id": 6}, {"id": 7}]},
                            {"id": 8},
                        ],
                    },
                    {
                        "id": 9,
                        "children": [
                            {"id": 10, "children": [{"id": 11}, {"id": 12}]},
                            {"id": 13},
                        ],
                    },
                ],
            },
            {"id": 14},
        ],
    },
    "dependencies": [
        {
            "targets": [8],
            "trigger": "click",
            "inputs": [2, 6],
            "outputs": [7],
            "queue": False,
        },
        {
            "targets": [13],
            "trigger": "click",
            "inputs": [2, 11],
            "outputs": [12],
            "queue": False,
        },
    ],
}
