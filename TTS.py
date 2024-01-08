import pyttsx3

def talk(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def slow(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    engine.setProperty('rate', rate-50)
    for num in range(100):
        engine.setProperty('volume', volume+1)
    engine.say(text)
    engine.runAndWait()