''' break-skips current iteration
    else - connected to for , if break statment is 
           executed within for else is nullified'''


for i in range (1,11):
    if i ==15:
        break
    print(i)
else:
    print("no break was encountered")