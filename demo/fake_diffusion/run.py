import gradio as gr
import numpy as np
import time
import os


def fake_diffusion(steps):
    for _ in range(steps):
        time.sleep(1)
        image = np.random.random((200, 200, 3))
        yield image
    
    image = os.path.join(os.path.dirname(__file__), "cheetah.jpg")    
    yield image


demo = gr.Interface(fake_diffusion, 
                    inputs=gr.Slider(1, 10, 3), 
                    outputs="image")

if __name__ == "__main__":
    demo.launch()
