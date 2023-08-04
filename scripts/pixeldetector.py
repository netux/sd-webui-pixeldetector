import gradio as gr
from pixeldetector import run
from modules import script_callbacks


def add_tab():
	with gr.Blocks() as ui:
		with gr.Row():
			with gr.Box():
				with gr.Group():
					input_image = gr.Image(type="pil", tool="select", image_mode="RGB")

					with gr.Accordion(label="Settings"):
						palette = gr.Checkbox(label="Palette", value=True)
						palette_max = gr.Number(label="Palette max", precision=0, value=128)
						rescale = gr.Number(label="Rescale", precision=0, value=-1)

				with gr.Row():
					submit = gr.Button(value="Submit", variant="primary")

			output_image = gr.Image(elem_classes="pixel-perfect", interactive=False)


			submit.click(run, inputs=[input_image, rescale, palette, palette_max], outputs=output_image)

	return [(ui, "Pixel detector", "pixel_detector")]

script_callbacks.on_ui_tabs(add_tab)
