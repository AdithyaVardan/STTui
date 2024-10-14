import random
import datetime
import requests
from bs4 import BeautifulSoup
from speedtest import Speedtest
from voice_module import speak

def speed_test():
    """Perform speed test and announce download and upload speeds."""
    st = Speedtest()
    download_speed = str(int(st.download() / 1000000)) + "Mbps"
    upload_speed = str(int(st.upload() / 1000000)) + "Mbps"
    speak(f"Download speed: {download_speed}")
    speak(f"Upload speed: {upload_speed}")

def show_date_time():
    """Get and announce the current date and time."""
    now = datetime.datetime.now()
    speak(str(now))

def get_covid_stats():
    """Fetch and announce COVID-19 statistics."""
    url = "https://www.worldometers.info/coronavirus/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    data = soup.find_all("div", class_="maincounter-number")
    
    speak(f"Total cases: {data[0].text.strip()}")
    speak(f"Total deaths: {data[1].text.strip()}")
    speak(f"Total recovered: {data[2].text.strip()}")

def roll_dice():
    """Roll a dice and announce the value."""
    dice_value = random.randint(1, 6)
    speak(f"Dice value: {dice_value}")
