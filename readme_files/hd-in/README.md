<!-- इस फ़ाइल को सीधे संपादित न करें। इसके बजाय readme_template.md या guides/1)getting_started/1)quickstart.md टेम्पलेट को संपादित करें और फिर render_readme.py स्क्रिप्ट चलाएँ। -->

<div align="center">

[<img src="../gradio.svg" alt="gradio" width=300>](https://gradio.app)<br>
<em>आसानी से मजेदार मशीन लर्निंग ऐप्स बनाएं और साझा करें।</em>

[![gradio-backend](https://github.com/gradio-app/gradio/actions/workflows/backend.yml/badge.svg)](https://github.com/gradio-app/gradio/actions/workflows/backend.yml)
[![gradio-ui](https://github.com/gradio-app/gradio/actions/workflows/ui.yml/badge.svg)](https://github.com/gradio-app/gradio/actions/workflows/ui.yml)  
 [![PyPI](https://img.shields.io/pypi/v/gradio)](https://pypi.org/project/gradio/)
[![PyPI downloads](https://img.shields.io/pypi/dm/gradio)](https://pypi.org/project/gradio/)
![Python version](https://img.shields.io/badge/python-3.8+-important)
[![Twitter follow](https://img.shields.io/twitter/follow/gradio?style=social&label=follow)](https://twitter.com/gradio)

[वेबसाइट](https://gradio.app)
| [दस्तावेज़ीकरण](https://gradio.app/docs/)
| [मार्गनिर्देशिका](https://gradio.app/guides/)
| [प्रारंभ करना](https://gradio.app/getting_started/)
| [उदाहरण](demo/)
| [English](readme_files/zh-cn#readme)

</div>

# Gradio: Python में मशीन लर्निंग वेब ऐप्स बनाएं

Gradio एक ओपन-सोर्स Python पुस्तकालय है जिसका उपयोग मशीन लर्निंग और डेटा साइंस डेमो और वेब ऐप्स बनाने के लिए किया जाता है।

Gradio के साथ, आप अपने मशीन लर्निंग मॉडल या डेटा साइंस वर्कफ़्लो के चारों ओर एक सुंदर उपयोगकर्ता इंटरफ़ेस तैयार कर सकते हैं और लोगों को उनकी खुद की छवियों को खींच-डालकर, पाठ को पेस्ट करके, अपनी आवाज़ को रिकॉर्ड करके और आपके डेमो के साथ इंटरैक्ट करके इसे "आज़माएं", सभी इसे ब्राउज़र के माध्यम से कर सकते हैं।

![इंटरफेस मोंटाज़](/readme_files/header-image.jpg)

Gradio का उपयोग निम्न कार्यों के लिए उपयोगी होता है:

- आपके मशीन लर्निंग मॉडल को **प्रदर्शित करना** (Demoing), जो क्लाइंट/सहयोगी/उपयोगकर्ता/छात्रों के लिए हो सकता है।

- अपने मॉडल को त्वरित रूप से **डिप्लॉय** (Deploy) करना, स्वतः साझा करने योग्य लिंक का उपयोग करके मॉडल के प्रदर्शन पर प्रतिक्रिया प्राप्त करना।

- विकास के दौरान अपने मॉडल को इंटरैक्टिव ढंग से **डीबग** (Debug) करना, जिसमें स्थापित मानिपुलेशन और व्याख्या उपकरण होते हैं।

## त्वरित प्रारंभ

**पूर्वापेक्षा**: Gradio को Python 3.8 या उच्चतर संस्करण की आवश्यकता होती है, बस इतना ही!

### Gradio क्या करता है?

अपने मशीन लर्निंग मॉडल, API या डेटा साइंस वर्कफ़्लो को दूसरों के साथ साझा करने के लिए एक बेहतरीन तरीका है उन्हें एक **इंटरैक्टिव ऐप** बनाकर उन्हें उपयोगकर्ताओं या सहयोगियों को उनके ब्राउज़र में डेमो का प्रयोग करने की अनुमति देना।

Gradio आपको **डेमो बनाने और उन्हें साझा करने** की सुविधा प्रदान करता है, और यह आमतौर पर कुछ ही कोड लाइन्स में होता है! तो चलिए शुरू करते हैं।

### हैलो, वर्ल्ड

एक सरल "हैलो, वर्ल्ड" उदाहरण के साथ Gradio को चलाने के लिए, निम्न तीन कदमों का पालन करें:

1\. pip का उपयोग करके Gradio को इंस्टॉल करें:

```bash
pip install gradio
```

2\. कृपया नीचे दिए गए कोड को एक Python स्क्रिप्ट या Jupyter नोटबुक ([या Google Colab में](https://colab.research.google.com/drive/18ODkJvyxHutTN0P5APWyGFO_xwNcgHDZ?usp=sharing)) चलाएं:

```python
import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    
demo.launch()
```

हम Gradio का उपयोग करके कोड की बेहतर पठनीयता के लिए आयातित नाम को `gr` तक संक्षेपित करते हैं। यह एक व्यापकता से अपनाया जाने वाला अनुशासन है जिसे आपको अनुसरण करना चाहिए ताकि आपके कोड के साथ काम करने वाले कोई भी उसे आसानी से समझ सके।

3\. नीचे दिए गए डेमो ज्ञापक रूप से Jupyter नोटबुक के अंदर दिखाई देगा, या यदि आप स्क्रिप्ट से चला रहे हैं तो ब्राउज़र में [http://localhost:7860](http://localhost:7860) पर पॉप अप करेगा:

![hello_world डेमो](/demo/hello_world/screenshot.gif)

स्थानीय विकास करते समय, यदि आप कोड को Python स्क्रिप्ट के रूप में चलाना चाहते हैं, तो आप ग्रेडियो सीएलआई का उपयोग करके एप्लिकेशन **पुनः लोड के मोड में** लॉन्च करने का उपयोग कर सकते हैं, जो सहज और तेज़ विकास प्रदान करेगा। [ऑटो-रीलोडिंग गाइड](https://gradio.app/developing-faster-with-reload-mode/) में रीलोड के बारे में अधिक जानें।.

```bash
gradio app.py
```

नोट: आप `python app.py` भी कर सकते हैं, लेकिन यह स्वचालित पुनः लोड मेकेनिज़्म प्रदान नहीं करेगा।

### `Interface` कक्षा

आप देखेंगे कि डेमो बनाने के लिए हमने `gr.Interface` बनाया है। यह `Interface` कक्षा किसी भी Python फ़ंक्शन को एक उपयोगकर्ता इंटरफ़ेस के साथ आवृत्त कर सकती है। उपरोक्त उदाहरण में, हमने एक सरल पाठ-आधारित फ़ंक्शन देखा, लेकिन फ़ंक्शन को संगीत जेनरेटर से लेकर टैक्स कैलकुलेटर तक और प्रीट्रेन किए गए मशीन लर्निंग मॉडल के पूर्वानुमान फ़ंक्शन तक कुछ भी हो सकता है।

मूल `Interface` कक्षा को तीन आवश्यक पैरामीटरों के साथ प्रारंभित किया जाता है:

- `fn`: UI के चारों ओर एक फ़ंक्शन को आवृत्त करने के लिए।
- `Inputs`: इनपुट के लिए कौन सा कम्पोनेंट(उदाहरण के लिए `"text"`, `"image"` या `"audio"`) का उपयोग करना है।
- `outputs`: आउटपुट के लिए कौन सा कम्पोनेंट(उदाहरण के लिए `"text"`, `"image"` या `"label"`) का उपयोग करना है।

चलो इनपुट और आउटपुट प्रदान करने के लिए इन कंपोनेंट्स की और अधिक नजदीक से देखते हैं।

### कंपोनेंट गुण

हमने पिछले उदाहरणों में कुछ सरल `Textbox` कंपोनेंट देखे, लेकिन यदि आप चाहते हैं कि आप UI कंपोनेंट्स की दिखावट या व्यवहार को कैसे बदलें?

मान लें कि आप इनपुट पाठ क्षेत्र को अनुकूलित करना चाहते हैं — उदाहरण के लिए, आप चाहते हैं कि यह बड़ा हो और एक पाठ प्लेसहोल्डर हो। यदि हम स्ट्रिंग शॉर्टकट का उपयोग करने के बजाय `Textbox` के लिए वास्तविक कक्षा का उपयोग करें, तो आपको कंपोनेंट गुणों के माध्यम से अधिक अनुकूलन की सुविधा मिलती है।

```python
import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(lines=2, placeholder="Name Here..."),
    outputs="text",
)
demo.launch()
```

![`hello_world_2` डेमो](/demo/hello_world_2/screenshot.gif)

### एकाधिक इनपुट और आउटपुट कंपोनेंट्स

सोचें कि आपके पास एक अधिक जटिल फ़ंक्शन है, जिसमें एकाधिक इनपुट और आउटपुट होते हैं। नीचे दिए गए उदाहरण में, हम एक स्ट्रिंग, बूलियन और नंबर लेने और एक स्ट्रिंग और नंबर लौटाने वाली फ़ंक्शन को परिभाषित करते हैं। देखें कि आप कैसे एक इनपुट और आउटपुट कंपोनेंट्स की सूची पास करते हैं।

```python
import gradio as gr

def greet(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "checkbox", gr.Slider(0, 100)],
    outputs=["text", "number"],
)
demo.launch()
```

![`hello_world_3` डेमो](/demo/hello_world_3/screenshot.gif)

आप सीधे कंपोनेंट्स को एक सूची में लपेटते हैं। `inputs` सूची में प्रत्येक कंपोनेंट फ़ंक्शन के पैरामीटरों में से एक के साथ मेल खाता है, क्रमबद्धता के अनुसार। `outputs` सूची में प्रत्येक कंपोनेंट फ़ंक्शन द्वारा लौटाए गए मानों में से एक के साथ मेल खाता है, फिर से क्रमबद्धता के अनुसार।

### एक छवि उदाहरण

ग्रेडियो बहुत सारे प्रकार के कंपोनेंट्स, जैसे `Image`, `DataFrame`, `Video`, या `Label`, का समर्थन करता है। चलिए इनके बारे में अनुभव प्राप्त करने के लिए एक इमेज-टू-इमेज फ़ंक्शन का प्रयोग करें!

```python
import numpy as np
import gradio as gr

def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189], 
        [0.349, 0.686, 0.168], 
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img

demo = gr.Interface(sepia, gr.Image(shape=(200, 200)), "image")
demo.launch()
```

![`sepia_filter` डेमो](/demo/sepia_filter/screenshot.gif)

जब आप `Image` कंपोनेंट का उपयोग इनपुट के रूप में करते हैं, तो आपकी फ़ंक्शन को एक नंपाई एरे मिलेगी जिसका आकार `(ऊंचाई, चौड़ाई, 3)` होगा, जहां अंतिम आयाम RGB मानों को प्रदर्शित करता है। हम एक नंपाई एरे के रूप में एक छवि भी लौटाएँगे।

आप `type=` कीवर्ड तर्क के साथ कंपोनेंट द्वारा उपयोग किए जाने वाले डेटाटाइप को भी सेट कर सकते हैं। उदाहरण के लिए, यदि आप चाहते हैं कि आपकी फ़ंक्शन एक नंपाई एरे की बजाय एक छवि फ़ाइल के लिए फ़ाइल पथ को ले, तो इनपुट `Image` कंपोनेंट को इस तरह से लिखा जा सकता है:

```python
gr.Image(type="filepath", shape=...)
```

ध्यान दें कि हमारे इनपुट `Image` कंपोनेंट के साथ एक संपादन बटन 🖉 भी होता है, जिसकी मदद से छवियों को क्रॉप और जूम करने का विकल्प मिलता है। इस तरीके से छवियों को मानव-अध्ययन मॉडल में छिपे हुए दोषों या छलों को प्रकट करने में मदद मिल सकती है!

आप [Gradio docs](https://gradio.app/docs) में इन कई कंपोनेंट्स के बारे में और उनका उपयोग कैसे करें के बारे में और अधिक पढ़ सकते हैं।

### Chatbots

ग्रेडियो में एक हाई-लेवल क्लास `gr.ChatInterface` शामिल है, जो `gr.Interface` के तुलनात्मक है, लेकिन यह विशेष रूप से चैटबॉट UI के लिए डिज़ाइन किया गया है। `gr.ChatInterface` क्लास भी एक फ़ंक्शन को लपेटता है लेकिन इस फ़ंक्शन को एक विशेष सिग्नेचर होनी चाहिए। फ़ंक्शन को दो आर्ग्यूमेंट्स लेना चाहिए: `message` और फिर `history` (आर्ग्यूमेंट्स को कुछ भी नाम दिया जा सकता है, लेकिन इस क्रम में होने चाहिए)

- `message`: उपयोगकर्ता के इनपुट को प्रतिष्ठित करने वाला एक `str`
- `history`: उस समय तक की बातचीत को प्रतिष्ठित करने वाली एक `list` की `list`. प्रत्येक आंतरिक सूची में एक जोड़ी का प्रतिष्ठित किया गया होता है: `[उपयोगकर्ता का इनपुट, बॉट का प्रतिक्रिया]`.

आपके फ़ंक्शन को एकल स्ट्रिंग प्रतिक्रिया लौटानी चाहिए, जो विशेष उपयोगकर्ता इनपुट `message` के लिए बॉट की प्रतिक्रिया होती है।

उसके अलावा, `gr.ChatInterface` कोई अनिवार्य पैरामीटर नहीं है (हालांकि इसके कई पैरामीटर UI की कस्टमाइज़ेशन के लिए उपलब्ध हैं)।

यहां एक खिलौना उदाहरण है:

```python
import random
import gradio as gr

def random_response(message, history):
    return random.choice(["Yes", "No"])

demo = gr.ChatInterface(random_response)

demo.launch()
```

![`chatinterface_random_response` डेमो](/demo/chatinterface_random_response/screenshot.gif)

आप [अधिक जानकारी के लिए पढ़ें `gr.ChatInterface` डेमो](https://gradio.app/guides/creating-a-chatbot-fast).

### ब्लॉक्स: और लचीलापन और नियंत्रण

Gradio दो तरीकों से ऐप्स बनाने का विकल्प प्रदान करता है:

1\. **Interface** और **ChatInterface**, जो की वे उच्च स्तरीय विस्तार को प्रदान करते हैं जिसके बारे में हम अब तक चर्चा कर रहे थे डेमो बनाने के लिए।

2\. **Blocks**, जो एक निम्न स्तरीय API है और जिसका उपयोग और लचीले लेआउट और डेटा फ़्लो वाले वेब ऐप्स डिज़ाइन करने के लिए किया जाता है। ब्लॉक्स आपको इस तरह की चीजें करने की अनुमति देता है जैसे कि मल्टीपल डेटा फ़्लो और डेमोज़, कंपोनेंट्स को पृष्ठ पर कहां दिखाएं, कॉम्प्लेक्स डेटा फ़्लो को हैंडल करें (उदाहरण के लिए, आउटपुट अन्य फ़ंक्शन के लिए इनपुट के रूप में सेव कर सकता है), और उपयोगकर्ता इंटरैक्शन के आधार पर कंपोनेंट्स की गुणों/दृश्यता को अद्यतन करें — और इन सभी को पैथन में ही। यदि आपको यह स्वनियोजितता चाहिए है, तो बजाय इसके, `Blocks` की कोशिश करें!

### नमस्ते, Blocks

चलिए एक सरल उदाहरण को देखें। ध्यान दें कि यहां एपीआई `Interface` से कैसे भिन्न है।

```python
import gradio as gr

def greet(name):
    return "Hello " + name + "!"

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

demo.launch()
```

![`hello_blocks` डेमो](/demo/hello_blocks/screenshot.gif)

यह बातें ध्यान में रखें:

- `Blocks` को `with` शर्त के साथ बनाया जाता है, और इस शर्त के अंदर बनाए गए किसी भी कंपोनेंट को अपने आप ऐप में जोड़ा जाता है।
- कंपोनेंट्स ऐप में ऊपर-नीचे क्रम में स्थानित होते हैं जैसे कि वे बनाए जाते हैं। (बाद में हम लेआउट कस्टमाइज़ करने के बारे में चर्चा करेंगे!)
- एक `Button` बनाया गया था, और फिर इस बटन में एक `click` इवेंट-सुनने-वाला जोड़ा गया था। इसके लिए API पुराने जैसा दिखना चाहिए! `Interface` की तरह, `click` विधि पायथन फ़ंक्शन, इनपुट कंपोनेंट्स, और आउटपुट कंपोनेंट्स लेती है।

### अधिक जटिलता

यहां एक ऐप है जिससे आप Blocks के साथ क्या संभव है उसका एक स्वाद मिलेगा:

```python
import numpy as np
import gradio as gr


def flip_text(x):
    return x[::-1]


def flip_image(x):
    return np.fliplr(x)


with gr.Blocks() as demo:
    gr.Markdown("Flip text or image files using this demo.")
    with gr.Tab("Flip Text"):
        text_input = gr.Textbox()
        text_output = gr.Textbox()
        text_button = gr.Button("Flip")
    with gr.Tab("Flip Image"):
        with gr.Row():
            image_input = gr.Image()
            image_output = gr.Image()
        image_button = gr.Button("Flip")

    with gr.Accordion("Open for More!"):
        gr.Markdown("Look at me...")

    text_button.click(flip_text, inputs=text_input, outputs=text_output)
    image_button.click(flip_image, inputs=image_input, outputs=image_output)

demo.launch()
```

![`blocks_flipper` डेमो](demo/blocks_flipper/screenshot.gif)

यहाँ और भी बहुत कुछ हो रहा है! हम इस [ब्लॉक के साथ बनाए गए ऐप्स](https://gradio.app/blocks-and-event-listeners) चर्चा करेंगे, जैसे कि आप ने अभी तक जान लिया है।

बधाई हो, अब आप Gradio के मूल तत्वों से परिचित हो चुके हैं! 🥳 हमारे [अगले गाइड](https://gradio.app/key_features) पर जाएं और Gradio की मुख्य विशेषताओं के बारे में और अधिक जानें।


## ओपन सोर्स स्टैक

ग्रेडियो बहुत सारी शानदार ओपन सोर्स पुस्तकालयों के साथ बनाया गया है, कृपया उन्हें भी समर्थन करें!

[<img src="../huggingface_mini.svg" alt="huggingface" height=40>](https://huggingface.co)
[<img src="../python.svg" alt="python" height=40>](https://www.python.org)
[<img src="../fastapi.svg" alt="fastapi" height=40>](https://fastapi.tiangolo.com)
[<img src="../encode.svg" alt="encode" height=40>](https://www.encode.io)
[<img src="../svelte.svg" alt="svelte" height=40>](https://svelte.dev)
[<img src="../vite.svg" alt="vite" height=40>](https://vitejs.dev)
[<img src="../pnpm.svg" alt="pnpm" height=40>](https://pnpm.io)
[<img src="../tailwind.svg" alt="tailwind" height=40>](https://tailwindcss.com)
[<img src="../storybook.svg" alt="storybook" height=40>](https://storybook.js.org/)
[<img src="../chromatic.svg" alt="chromatic" height=40>](https://www.chromatic.com/)

## लाइसेंस

ग्रेडियो का लाइसेंस अपाचे लाइसेंस 2.0 के तहत है, जो इस रिपॉजिटरी के मूल निर्देशिका में [LICENSE](LICENSE) फ़ाइल में मिलेगा।

## संदर्भ

कृपया विज्ञान शोध में ग्रेडियो का उपयोग करते हैं तो _[Gradio: Hassle-Free Sharing and Testing of ML Models in the Wild](https://arxiv.org/abs/1906.02569), ICML HILL 2019_, नामक पेपर को भी देखें और इसे संदर्भित करें।

```
@article{abid2019gradio,
  title = {Gradio: Hassle-Free Sharing and Testing of ML Models in the Wild},
  author = {Abid, Abubakar and Abdalla, Ali and Abid, Ali and Khan, Dawood and Alfozan, Abdulrahman and Zou, James},
  journal = {arXiv preprint arXiv:1906.02569},
  year = {2019},
}
```
