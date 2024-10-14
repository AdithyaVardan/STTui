import speech_recognition as sr
import pyttsx3

s = ""

def save_to_file(text, filename="Commands.txt"):
    with open(filename, "w") as f:
        f.write(text)

def speak(text):
    """Convert text to speech and append it to session log."""
    global s
    engine = pyttsx3.init()
    print(text)
    engine.say(text)
    s += text + "\n"
    engine.runAndWait()

def listen_for_command():
    """Listen for user input via microphone and return the transcribed text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Waiting for your response")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    
    try:
        command = r.recognize_google(audio).lower()
        speak('You said: ' + command)
    except sr.UnknownValueError:
        speak("Your last command couldn't be heard")
        command = listen_for_command()  # Recursively listen again
    return command
