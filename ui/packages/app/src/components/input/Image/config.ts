import Component from "./Image.svelte";
import ExampleComponent from "./Example.svelte";
import Interpretation from "./Interpretation.svelte";
import { loadAsData } from "../../utils/example_processors";

export default {
	component: Component,
	example: ExampleComponent,
	interpretation: Interpretation,
	process_example: loadAsData
};
