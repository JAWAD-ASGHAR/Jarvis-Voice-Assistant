import google.generativeai as genai
import speech_recognition as sr
import webbrowser
import musicLibrary
import threading
import time
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('GEMINI_API_KEY')
r = sr.Recognizer()

class BeepController:
    def __init__(self):
        self.stop_beep = False
        self.beep_thread = None
    
    def play_beep(self):
        while not self.stop_beep:
            subprocess.run(['afplay', '/System/Library/Sounds/Ping.aiff'])
            time.sleep(1)
    
    def start_beeping(self):
        self.stop_beep = False
        self.beep_thread = threading.Thread(target=self.play_beep)
        self.beep_thread.daemon = True
        self.beep_thread.start()
    
    def stop_beeping(self):
        self.stop_beep = True
        if self.beep_thread and self.beep_thread.is_alive():
            self.beep_thread.join()

# Create a global beep controller
beep_controller = BeepController()

def aiProcess(command):
    genai.configure(api_key=key)

    beep_controller.start_beeping()
    
    try:
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction="You are a virtual assistant named Jarvis skilled in general tasks just like Siri or Alexa. Keep the response short and concise."
        )
        response = model.generate_content(
            command
        )
        # Stop the beeping
        beep_controller.stop_beeping()
        speak(response.text)
    except Exception as e:
        # Stop the beeping
        beep_controller.stop_beeping()
        print(f"An error occurred: {e}")
        speak("Sorry, I'm having trouble.")


def speak(text):
    subprocess.run(['say', text])

def processCommand(command):
    if "open google" in command.lower():
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command.lower():
        speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in command.lower():
        speak("Opening Facebook...")
        webbrowser.open("https://www.facebook.com")
    elif "open twitter" in command.lower():
        speak("Opening Twitter...")
        webbrowser.open("https://www.twitter.com")
    elif "open instagram" in command.lower():
        speak("Opening Instagram...")
        webbrowser.open("https://www.instagram.com")
    elif "open reddit" in command.lower():
        speak("Opening Reddit...")
        webbrowser.open("https://www.reddit.com")
    elif "open github" in command.lower():
        speak("Opening GitHub...")
        webbrowser.open("https://www.github.com")
    elif "open linkedin" in command.lower():
        speak("Opening LinkedIn...")
        webbrowser.open("https://www.linkedin.com")
    elif command.lower().startswith("play"):
        song = command.lower().split("play")[1].strip()
        link = musicLibrary.music.get(song)
        if link:
            speak("Playing " + song)
            webbrowser.open(link)
        else:
            speak("Song not found")
    else:
        aiProcess(command)
        

if __name__ == "__main__":
    speak("Initializing voice command system...")
    while True:
        try:
        # Listen for wake word for VA
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=5, phrase_time_limit=2)

            print("Processing speech recognition...")
            words = r.recognize_google(audio)
            print("You said: " + words)
            if "jarvis" in words.lower():
                speak("Yes?")   
                with sr.Microphone() as source:
                    print("VA listening...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("You said: " + command)

                    processCommand(command)
                     
        except Exception as e:
            print("Could not request results; {0}".format(e))