---
"@gradio/app": minor
"gradio": minor
---

highlight:

#### Add `render` function to `<gradio-app>`

We now have an event `render` on the <gradio-app> web component, which is triggered once the embedded space has finished rendering.

```html
<script>
	function handleLoadComplete() {
		console.log("Embedded space has finished rendering");
	}
	const gradioApp = document.querySelector("gradio-app");
	gradioApp.addEventListener("render", handleLoadComplete);
</script>
```
