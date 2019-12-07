import pyttsx3

engine = pyttsx3.init()
text = sys.argv[1]

engine.say(text)
engine.runAndWait()
engine.stop()