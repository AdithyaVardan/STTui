#version-2.0.0
from voice_module import speak, listen_for_command
from command_module import process_command
import datetime

def main():
    # Greeting based on time
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    if current_time <= "12:00:00":
        speak("Good morning")
    else:
        speak("Good evening")
    
    speak('Hi, I am your assistant')
    speak("How can I help you?")
    
    # Main loop to listen for and process commands
    while True:
        command = listen_for_command()
        process_command(command)

if __name__ == "__main__":
    main()
