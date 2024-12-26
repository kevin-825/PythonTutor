import pyttsx3

tty_engine = pyttsx3.init()

sample_text = "This was python tutorial! Welcome to this tutorial!"

tty_engine.say(sample_text)

tty_engine.runAndWait()