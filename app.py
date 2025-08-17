from openai import OpenAI
from apikey import api_data
import speech_recognition as sr  # Converts voice commands to text
import pyttsx3  # Read out text output to voice
import webbrowser

# Initialize OpenAI client
Model = "gpt-4o"
client = OpenAI(api_key=api_data)


def Reply(question):
    completion = client.chat.completions.create(
        model=Model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": question},
        ],
        max_tokens=200,
    )
    # Access properly – `.message` doesn’t exist in new SDK, use `.messages`
    answer = completion.choices[0].message["content"]
    return answer


# Text-to-speech setup
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("Hello, how are you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .......")
        r.pause_threshold = 1  # Wait for 1 sec before considering the end of a phrase
        audio = r.listen(source)

    try:
        print("Recognizing ....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")
    except Exception:
        print("Say that again .....")
        return "none"
    return query


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if query == "none":
            continue

        ans = Reply(query)
        print(ans)
        speak(ans)

        # Specific Browser Related Tasks
        if "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
        elif "open google" in query:
            webbrowser.open("https://www.google.com")
        elif "bye" in query:
            speak("Goodbye!")
            break
