import random
com = random.randint(1,100) #generate random no betwen 1 and 100
tries=0
while True:
    tries=tries+1
    hum = int(input("guess a no:"))   
    if hum == com:
        print("u won ,on tries",tries)
        break
    elif hum>com:
        print("go lower")
    elif hum<com:
        print("go higher")
