import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

# Initialize speech recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    # Voice introduction
    speak("You have 10 seconds to speak your command. Begin after the countdown.")
    print("Recording for 10 seconds... (Speak after countdown)")

    # Countdown
    speak("3")
    speak("2")
    speak("1")
    speak("Speak now")

    # Record for exactly 10 seconds
    audio_text = r.record(source, duration=10)

    speak("Recording complete")
    print("Recording complete")

    try:
        # Recognize speech using Google Web Speech API
        recognized_text = r.recognize_google(audio_text)
        print("You said: " + recognized_text)
        speak("You said: " + recognized_text)
    except sr.UnknownValueError:
        error_msg = "Sorry, I could not understand what you said."
        print(error_msg)
        speak(error_msg)
    except sr.RequestError as e:
        error_msg = f"Could not request results: {e}"
        print(error_msg)
        speak("Sorry, there was an error with the speech recognition service.")
    except Exception as e:
        error_msg = f"Error: {e}"
        print(error_msg)
        speak("Sorry, an unexpected error occurred.")
