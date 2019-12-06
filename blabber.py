import pyttsx3
import os, sys


engine = pyttsx3.init()
text = sys.argv[1]

engine.say(text)
engine.runAndWait()
engine.stop()