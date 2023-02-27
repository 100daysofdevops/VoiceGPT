# 🎤 VoiceGPT🎤 

We often interact with ChatGPT by manually typing, but it could be better to interact with it using voice. I wrote a script that will be able to perform that.

## 💪 How does it work?

✅ It uses the speech_recognition library to transcribe user speech and then feeds that text into the OpenAI API to generate a response.

## 👀 Some other features

✅ The max_tokens parameter is set to 2048. This means that the maximum length of the generated text will be 2048 tokens.

✅ The GPT engine used in the above code is "text-davinci-002".It's one of the most advanced GPT-3 models currently available on the OpenAI platform, and it can produce high-quality natural language responses across a wide range of topics. The "002" in the engine name refers to the specific version of the model being used.

✅ The program runs in a loop, listening for user input and generating responses as often as the user wishes to continue.

## 🤷‍♂️ How to use the code

✅  To use this code, you'll need to export an OpenAI API key. To generate an OpenAPI key, check this doc https://platform.openai.com/account/api-keys

✅  Run the following command 

```python
export OPENAI_API_KEY="your-openapi-key" 

```

## Feedback

🎬 This was a fun weekend project so the code may have a bug. I am looking forward to your feedback. If you have any issues, please create a GitHub PR or issue. Also, this is not the first attempt; people have already tried it, so please check their project, too 🙏.
