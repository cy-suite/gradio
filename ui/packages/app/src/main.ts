import App from "./App.svelte";
import Login from "./Login.svelte";
import { fn } from "./api";

interface CustomWindow extends Window {
	gradio_mode: "app" | "website";
	launchGradio: Function;
	launchGradioFromSpaces: Function;
	gradio_config: Config;
}

declare let window: CustomWindow;
declare let BACKEND_URL: string;
declare let BUILD_MODE: string;

interface Component {
	name: string;
	[key: string]: unknown;
}

interface Config {
	allow_flagging: string;
	allow_interpretation: boolean;
	allow_screenshot: boolean;
	article: string;
	cached_examples: boolean;
	css: null | string;
	description: string;
	examples: Array<unknown>;
	examples_per_page: number;
	favicon_path: null | string;
	flagging_options: null | unknown;
	fn: Function;
	function_count: number;
	input_components: Array<Component>;
	output_components: Array<Component>;
	layout: string;
	live: boolean;
	queue: boolean;
	root: string;
	show_input: boolean;
	show_output: boolean;
	simpler_description: string;
	static_src: string;
	theme: string;
	thumbnail: null | string;
	title: string;
	version: string;
	space?: string;
	detail: string;
	dark: boolean;
}

window.launchGradio = (config: Config, element_query: string) => {
	let target = document.querySelector(element_query);

	if (!target) {
		throw new Error(
			"The target element could not be found. Please ensure atht element exists."
		);
	}

	if (config.root === undefined) {
		config.root = BACKEND_URL;
	}
	if (window.gradio_mode === "app") {
		config.static_src = ".";
	} else if (window.gradio_mode === "website") {
		config.static_src = "/gradio_static";
	} else {
		config.static_src = "https://gradio.s3-us-west-2.amazonaws.com/PIP_VERSION";
	}
	if (config.detail === "Not authenticated") {
		new Login({
			target: target,
			props: config
		});
	} else {
		let url = new URL(window.location.toString());
		if (config.theme !== null && config.theme.startsWith("dark")) {
			target.classList.add("dark");
			config.dark = true;
			if (config.theme === "dark") {
				config.theme = "default";
			} else {
				config.theme = config.theme.substring(5);
			}
		} else if (url.searchParams.get("__dark-theme") === "true") {
			config.dark = true;
			target.classList.add("dark");
		}
		config.fn = fn.bind(null, config.root + "api/");
		new App({
			target: target,
			props: config
		});
	}
};

window.launchGradioFromSpaces = async (space: string, target: string) => {
	const space_url = `https://huggingface.co/gradioiframe/${space}/+/`;
	let config = await fetch(space_url + "config");
	let _config: Config = await config.json();
	_config.root = space_url;
	_config.space = space;
	window.launchGradio(_config, target);
};

async function get_config() {
	if (BUILD_MODE === "dev") {
		let config = await fetch(BACKEND_URL + "config");
		config = await config.json();
		return config;
	} else {
		return window.gradio_config;
	}
}

if (window.gradio_mode == "app") {
	get_config().then((config) => {
		window.launchGradio(config, "#root");
	});
}
