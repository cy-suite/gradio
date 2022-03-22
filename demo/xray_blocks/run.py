import gradio as gr

import random

xray_model = lambda diseases, img: {disease: random.random() for disease in diseases}
ct_model = lambda diseases, img: {disease: 0.1 for disease in diseases}

xray_blocks = gr.Blocks()

with xray_blocks:
    gr.components.Markdown(
        """
	# Detect Disease From Scan
	With this model you can lorem ipsum
	- ipsum 1
	- ipsum 2
	"""
    )
    disease = gr.components.CheckboxGroup(choices=["Covid", "Malaria", "Lung Cancer"], label="Disease to Scan For")

    with gr.Tabs():
        with gr.TabItem("X-ray"):
            with gr.Row():
                xray_scan = gr.components.Image()
                xray_results = gr.components.JSON()
                output_textbox = gr.components.Textbox()
                input_textbox = gr.components.Textbox(default_value="Hello This Is a Input Textbox")
            xray_run = gr.Button("Run", css={
                "background-color": "red",
                "--hover-color": "orange"
            })
            xray_run.click(xray_model, inputs=[disease, xray_scan], outputs=xray_results)
            xray_run.click(xray_model, inputs=[disease, xray_scan], outputs=output_textbox)

        with gr.TabItem("CT Scan"):
            with gr.Row():
                ct_scan = gr.components.Image()
                ct_results = gr.components.JSON()
            ct_run = gr.Button("Run")
            ct_run.click(ct_model, inputs=[disease, ct_scan], outputs=ct_results)

    overall_probability = gr.components.Textbox()

# TODO: remove later
import json
print(json.dumps(xray_blocks.get_config_file(), indent=2))
    
xray_blocks.launch()
