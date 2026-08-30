import pyttsx3
engine = pyttsx3.init()


a=input("what is your name?")
if a=='shashank':
    engine.say("ohh! my bf name is also shashank")
    m=input("your wife name is ")
    print("anyway do u love",m)
    n=int(input("if yes how much ?"))
    engine.say("Huhhhhhhh! she love u 100000000%  more than u")   

else: print(engine.say("fuck u"))

engine.runAndWait()
