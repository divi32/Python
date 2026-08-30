#default value can be set inside value 
# if we assign less value while calling the function , error will not occur

'''positional argument'''

def addition(a,b,c,d=20):

    print(a+b+c+d)

addition(5,5,5)

'''error'''
#error will occur-> (a,b=20,c,d)
# instead do -> (a,c,d,b=20)


'''keyword argument'''

def subs(a,b):
    print(b-a)

subs(b=30,a=20) #if we want first value goes to b and second value goes to a