![image](https://github.com/sr2echa/ai69/assets/65058816/57eb644c-e3b9-4810-9050-9cd52abc486d)


`ai69` is a Python package to dynamically generate and execute Python functions for any occation. It's designed to simplify the process of integrating AI-powered functions for anything you want.

---

## Installation

To install `ai69`, run the following command in your terminal:

```bash
pip install ai69
```

Ensure you have Python 3.6 or later installed on your system.


## Usage

### Setting Up

First, import `ai69` and set your OpenAI API key:

```python
from ai69 import ai

ai.set_key("your-openai-api-key")
```

> [!IMPORTANT]
> <samp> You must obtain an API key from OpenAI. You can get it from [here](https://platform.openai.com/api-keys). </samp>

Alternatively, If you have an environment variable `OPENAI_API_KEY` set, you need not use **ai.set()** to set up the key. ai69 will auto import the key for you 


### Calling Functions

With `ai69`, you can call functions dynamically. The package will attempt to generate the appropriate Python code using OpenAI's Codex:

```python
from ai69 import ai

await ai.getWeather('Chennai') # 'sunny'
await ai.randomNumberBetween(1, 10) #6
await ai.slugify('My Article') # 'my-article'
await ai.hasProfanityRegex('f*ck this lol') # False
await ai.extractHashtags('this is #really cool! #ai #code') # ['really', 'ai', 'code']
await ai.getProgrammerJoke() # 'What do you call a programmer from Finland? Nerdic.'

```



## Features

- **Dynamic Function Generation:** Create functions on the fly based on method names and arguments.
- **AI-Powered Code Generation:** Utilizes OpenAI's GPT-3.5 Turbo model for generating Python code.
- **Flexible and Easy to Use:** Designed to be intuitive and straightforward, requiring minimal setup.




## Important Notes

- **Security:** Executing dynamically generated code can be risky. Always validate and sanitize inputs and use `ai69` in a secure environment.
- **API Key:** Your OpenAI API key should be kept confidential. Do not expose it in publicly accessible areas like GitHub repositories.

>[!NOTE]
> The responses from the AI can vary, and the generated code's quality depends on the model's current capabilities and understanding.




## Disclaimer

> `ai69` is an experimental tool that relies on AI to generate code. The developers of `ai69` are not responsible for any consequences arising from the use of this package, including but not limited to generated code quality, security vulnerabilities, or AI model inaccuracies.<br>
> Currently only OpenAI's GPT-3.5 Turbo model is supported. Support for other models may be added in the future. For this reason, we use openai's api rather than openai's python package.

>UwU we ***totally**** recommend you to use in production *lmaow*




## Contributing

Contributions to `ai69` are welcome! Please feel free to open a pull request or issue on GitHub. All contributions must be released under the [MIT](LICENSE).

---

###### `ai69` is released under the [MIT License](LICENSE).
