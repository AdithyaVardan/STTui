Here's a comprehensive README file for your project:

---

# **STTui - SPEECH TO TEXT User Interface**

This is a Python-based voice assistant that listens to user commands, performs various tasks like checking internet speed, fetching COVID-19 data, rolling a dice, telling jokes, and more. The assistant can recognize voice commands using Google's Speech Recognition API and respond audibly using text-to-speech technology.

## **Table of Contents**
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Files and Modules](#files-and-modules)
- [Requirements](#requirements)
- [License](#license)

---

## **Features**
- **Voice Recognition**: The assistant can recognize user commands via microphone input.
- **Text-to-Speech**: It converts text responses into audible speech.
- **Speed Test**: Measures your internet speed (upload and download).
- **COVID-19 Stats**: Fetches live data on COVID-19 cases, deaths, and recoveries.
- **Date and Time**: Provides the current date and time.
- **Website Navigation**: Opens websites directly from voice commands.
- **Dice Roller**: Simulates rolling a dice.
- **Dad Jokes**: Fetches random dad jokes.
- **Session Logging**: Optionally logs user interactions to a file upon exit.

---

## **Installation**
### **Prerequisites**
Ensure you have Python installed on your system. This project uses Python 3.6+.

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant
```

### **Step 2: Install the Required Libraries**
Install the dependencies listed in the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

Or manually install the required packages:
```bash
pip install speechrecognition pyttsx3 speedtest-cli requests beautifulsoup4
```

### **Step 3: Run the Program**
```bash
python main.py
```

---

## **Usage**
After starting the program, the voice assistant will greet you based on the time of day and wait for your voice commands. Below is a list of commands you can try:

### **Available Commands:**
- **Speed Test**: "speed test"
- **Fetch COVID-19 Stats**: "covid"
- **Get Date and Time**: "date and time"
- **Roll Dice**: "dice"
- **Open a Website**: "open website [website-name]"
- **Tell a Joke**: "joke"
- **Casual Responses**: "what's up?", "hai"
- **Exit**: "exit"

### **Exit Command**:
If you say "exit," the assistant will ask if you'd like to save your session log to a file before closing.

---

## **Files and Modules**

### 1. **`main.py`**
   - The main entry point of the program.
   - Initiates the assistant, listens for commands, and processes them.
   
### 2. **`voice_module.py`**
   - Handles voice recognition (converting speech to text) and text-to-speech conversion.
   - Contains functions like `listen_for_command()` and `speak()`.

### 3. **`utility_module.py`**
   - Contains utility functions such as speed testing, fetching COVID-19 data, showing date and time, and rolling a dice.

### 4. **`command_module.py`**
   - Processes and interprets voice commands, mapping them to the appropriate utility functions.

### 5. **`requirements.txt`**
   - Lists all the dependencies needed to run the project.

---

## **Requirements**

- Python 3.6+
- Libraries:
  - `speechrecognition`: For converting speech to text.
  - `pyttsx3`: For converting text to speech.
  - `speedtest-cli`: To measure internet speed.
  - `requests`: For making HTTP requests (used to fetch jokes and COVID-19 data).
  - `beautifulsoup4`: For web scraping (to get COVID-19 data).

### **Optional**
- A working microphone for voice recognition.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## **Contributing**

Pull requests are welcome! If you have any suggestions for improvements or find any bugs, feel free to contribute by opening an issue or submitting a pull request.

---


## **Authors**

- [@AdithyaVardan](https://www.github.com/AdithyaVardan)
- [@__sohan_sudheer__](https://www.instagram.com/__sohan_sudheer__)


---



