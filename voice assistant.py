import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
pip install pyttsx3
engine = pyttsx3.init('sapi5')  # Choose appropriate voice engine for your system
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set voice (0 for male, 1 for female)

def speak(text):
   """Speaks the given text."""
   engine.say(text)
   engine.runAndWait()

def wish_me():
   """Greets the user based on the time of day."""
   hour = int(datetime.datetime.now().hour)
   if hour >= 0 and hour < 12:
       speak("Good Morning!")
   elif hour >= 12 and hour < 18:
       speak("Good Afternoon!")
   else:
       speak("Good Evening!")

   speak("I am your voice assistant. How may I help you?")

def take_command():
   """Takes microphone input from the user and returns string output."""
   r = sr.Recognizer()
   with sr.Microphone() as source:
       print("Listening...")
       r.pause_threshold = 1
       audio = r.listen(source)

   try:
       print("Recognizing...")
       query = r.recognize_google(audio, language='en-in')  # Adjust language for your region
       print(f"User said: {query}\n")
   except Exception as e:
       # Error handling for voice recognition
       print(e)
       print("Say that again please...")
       return "None"
   return query

def run_assistant():
   """Main function to run the assistant."""
   wish_me()
   while True:
       query = take_command().lower()

       # Logic for executing tasks based on user commands
       if 'hello' in query:
           speak("Hello there! How can I help you?")
       elif 'time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"The time is {strTime}")
       elif 'date' in query:
           today = datetime.date.today()
           strDate = today.strftime("%B %d, %Y")
           speak(f"Today's date is {strDate}")
       elif 'wikipedia' in query:
           speak('Searching Wikipedia...')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           print(results)
           speak(results)
       elif 'who is' in query:
           person = query.replace('who is', '')
           results = wikipedia.summary(person, 1)
           speak('According to Wikipedia')
           print(results)
           speak(results)
       elif 'search' in query:
           speak("What do you want to search for?")
           query = take_command().lower()
           url = f"https://www.google.com/search?q={query}"
           webbrowser.open(url)
           speak(f"Here are some results for {query}")
       elif 'open google' in query:
           webbrowser.open(f'https://www.google.co.in/search?')
       elif 'exit' in query:
           speak("Thank you for giving us this opportunity")
           break
       else:
           speak('Please say the command again.')

if __name__ == "__main__":
   run_assistant()