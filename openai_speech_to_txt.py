import openai
import os
import speech_recognition as sr

# Setup OpenAI credentials (To generate a key check this link https://platform.openai.com/account/api-keys)
openai.api_key = os.getenv("OPENAI_API_KEY")

# set up speech recognizer
r = sr.Recognizer()

# Create a function which transcribes user input and generates a GPT response
def generate_gpt_response():
    with sr.Microphone() as source:
        print("Can you please say something!")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry I have no idea what you said :-)")
        return None
    except sr.RequestError as e:
        print(f"Sorry, there was an error processing your request: {e}")
        return None

    # Generate GPT response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=2048
    )

    return response.choices[0].text.strip()

# Listen for user input in a loop and generate a response
while True:
    # Call the function and print the result
    response = generate_gpt_response()
    if response:
        print("GPT response:", response)
    
    # Prompt user if they want to continue
    again = input("Would you like to continue? (y/n) ")
    if again.lower() != "y":
        break