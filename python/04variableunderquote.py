
import pyttsx3
engine = pyttsx3.init()
name=input("nam ?")
print(f"love you {name}")
engine.say(f"love you{name} meri jaan")

engine.runAndWait()
