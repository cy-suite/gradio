const production = !process.env.ROLLUP_WATCH;
module.exports = {
	content: [
		"./src/**/*.{html,js,svelte,ts}",
		"**/@gradio/**/*.{html,js,svelte,ts,css}"
	],

	theme: {
		extend: {},
		fontFamily: {
			mono: ["monospace"],
			sans: ["IBM Plex Sans", "system-ui"]
		}
	},
	mode: "jit",
	darkMode: "class", // or 'media' or 'class'

	variants: {
		extend: {}
	},
	plugins: [require("@tailwindcss/forms")]
};
