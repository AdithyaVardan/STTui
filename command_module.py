import webbrowser
import re
from voice_module import speak, listen_for_command
from utility_module import speed_test, show_date_time, get_covid_stats, roll_dice

def process_command(command):
    """Process the command and perform corresponding actions."""
    if 'cut' in command:
        # Example for cut (can be replaced by actual file operations)
        speak("This is a placeholder for cut operation.")
    
    elif 'speed test' in command:
        speed_test()
    
    elif 'covid' in command:
        get_covid_stats()
    
    elif 'date and time' in command:
        show_date_time()
    
    elif 'dice' in command:
        roll_dice()
    
    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain + '.com'
            webbrowser.open(url)
            speak("Opening web browser")
    
    elif 'what\'s up' in command:
        speak("Just doing my thing.")
    
    elif 'joke' in command:
        try:
            res = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
            if res.status_code == requests.codes.ok:
                speak(res.json()['joke'])
            else:
                speak("Oops! I ran out of jokes.")
        except:
            speak("Unable to fetch a joke at this moment.")
    
    elif 'exit' in command:
        speak("Do you want to save the session?")
        response = listen_for_command()
        if 'yes' in response:
            from voice_module import s
            save_to_file(s)
            speak("Session saved.")
        speak("Have a great day!")
        exit()
    
    elif 'hai' in command:
        speak("Are you seriously jobless?")
    
    else:
        speak("I don't know what you mean!")
