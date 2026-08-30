#to create a function we use 
'''def variable( parameters ):'''
#parameters are the values u accept while calling the fn
# arguments r the values u provide to parameters 

#basic form
def hello():
    print("hello miss")

hello()

# check palindrome

def pcheck(a):
    copy=a
    rev=0

    while a>0:
        rev=rev*10+a%10
        a=a//10

    if copy== rev:
        print("it is a palindrome")
    else:
        print("not a palindrome")

x=int(input("enter a numbetr:"))
pcheck(x)

