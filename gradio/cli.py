import sys

import gradio.reload
import gradio.deploy


def cli():
    args = sys.argv[1:]
    if len(args) == 0:
        raise ValueError("No file specified.")
    if args[0] == "--deploy":
        gradio.deploy()
    else:
        gradio.reload.run_in_reload_mode(*args)
