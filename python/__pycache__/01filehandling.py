# try : check all error except for indentation and syntax error
#try and except are mandantory together
# but else and finally are extra add on

'''try  except   else   finally   raise'''


'''
a=int(input("enter numb"))
b=int(input("enter second numb"))
 #if 'try' is not used and we put 0 as denominator our code will stop right away and remaining code will not run
try:
    print(a/b)
except Exception as err:
    print("sorry an error ocuured as",err)
else:
    print("no error")
finally:
    print("if there are errors or no error i will run ")

name ="divya"
print(name)

'''

age=int(input("ur age: "))
if age>= 18:
    raise TypeError("u r elligible") #instead of typeerroe u can write valueerror , syntax error etc..
    
print("u r not eligible")
