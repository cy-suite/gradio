import { test, describe, assert, afterEach } from "vitest";
import { cleanup, render } from "@gradio/tootils";
import Audio from "./Index.svelte";
import type { LoadingStatus } from "@gradio/statustracker";
import { setupi18n } from "../app/src/i18n";
import ResizeObserver from "resize-observer-polyfill";

global.ResizeObserver = ResizeObserver;

const loading_status: LoadingStatus = {
	eta: 0,
	queue_position: 1,
	queue_size: 1,
	status: "complete",
	scroll_to_output: false,
	visible: true,
	fn_index: 0,
	show_progress: "full"
};

describe("Audio", () => {
	setupi18n();

	afterEach(() => cleanup());

	test("renders audio component", async () => {
		const { getAllByTestId } = await render(Audio, {
			loading_status,
			label: "music",
			value: {
				url: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
				path: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
				orig_name: "SoundHelix-Song-1.mp3"
			},
			root: "",
			proxy_url: "",
			theme_mode: "dark"
		});

		assert.exists(getAllByTestId("waveform-music"));
	});
});
