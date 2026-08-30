'''
'r' read only
'w' write only
'a' appnend to end
'x' create 

'''
# open-> create / open new file 


'''
file=open("hello.txt","w")
data= input("wt u want to write in ur file")
file.write(data)
'''

#read 
'''
file=open("hello.txt","r")
print(file.read())

'''
#with is a statement it automatically closes the file even if error occurs
#if indentation is not maintained u will go out from file


with open("hello.txt","a") as f:
    f.write(" " +"i want to see if it is working")
