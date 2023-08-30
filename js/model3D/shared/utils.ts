import type { FileData } from "@gradio/upload";
import * as BABYLON from "babylonjs";

export const add_new_model = (
	canvas: HTMLCanvasElement,
	scene: BABYLON.Scene,
	engine: BABYLON.Engine,
	value: FileData | null,
	clear_color: [number, number, number, number],
	camera_position: [number | null, number | null, number | null]
): void => {
	if (scene && !scene.isDisposed && engine) {
		scene.dispose();
		engine.dispose();
	}

	engine = new BABYLON.Engine(canvas, true);
	scene = new BABYLON.Scene(engine);
	scene.createDefaultCameraOrLight();
	scene.clearColor = scene.clearColor = new BABYLON.Color4(...clear_color);

	engine.runRenderLoop(() => {
		scene.render();
	});

	window.addEventListener("resize", () => {
		engine.resize();
	});

	if (!value) return;

	let url: string;
	if (value.is_file) {
		url = value.data;
	} else {
		let base64_model_content = value.data;
		let raw_content = BABYLON.Tools.DecodeBase64(base64_model_content);
		let blob = new Blob([raw_content]);
		url = URL.createObjectURL(blob);
	}

	BABYLON.SceneLoader.ShowLoadingScreen = false;
	BABYLON.SceneLoader.Append(
		url,
		"",
		scene,
		() => {
			// scene.createDefaultCamera(createArcRotateCamera, replace, attachCameraControls)
			scene.createDefaultCamera(true, true, true);
			// scene.activeCamera has to be an ArcRotateCamera if the call succeeds,
			// we assume it does
			var helperCamera = scene.activeCamera! as BABYLON.ArcRotateCamera;

			if (camera_position[0] !== null) {
				helperCamera.alpha = (Math.PI * camera_position[0]) / 180;
			}
			if (camera_position[1] !== null) {
				helperCamera.beta = (Math.PI * camera_position[1]) / 180;
			}
			if (camera_position[2] !== null) {
				helperCamera.radius = camera_position[2];
			}
		},
		undefined,
		undefined,
		"." + value.name.split(".")[1]
	);
};
