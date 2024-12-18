import gradio as gr
from gradio import ChatMessage
from transformers import Tool, ReactCodeAgent  # type: ignore
from transformers.agents import stream_to_gradio, HfApiEngine  # type: ignore

# Import tool from Hub
image_generation_tool = Tool.from_space(
    space_id="black-forest-labs/FLUX.1-schnell",
    name="image_generator",
    description="Generates an image following your prompt. Returns a PIL Image.",
    api_name="/infer",
)

llm_engine = HfApiEngine("Qwen/Qwen2.5-Coder-32B-Instruct")
# Initialize the agent with both tools and engine
agent = ReactCodeAgent(tools=[image_generation_tool], llm_engine=llm_engine)


def interact_with_agent(prompt, messages):
    messages.append(ChatMessage(role="user", content=prompt))
    yield messages
    for msg in stream_to_gradio(agent, prompt):
        messages.append(msg)
        yield messages
    yield messages


with gr.Blocks() as demo:
    stored_message = gr.State([])
    chatbot = gr.Chatbot(
        label="Agent",
        type="messages",
        avatar_images=(
            None,
            "https://em-content.zobj.net/source/twitter/53/robot-face_1f916.png",
        ),
    )
    text_input = gr.Textbox(lines=1, label="Chat Message")
    text_input.submit(
        lambda s: (s, ""), [text_input], [stored_message, text_input]
    ).then(interact_with_agent, [stored_message, chatbot], [chatbot])

if __name__ == "__main__":
    demo.launch()
