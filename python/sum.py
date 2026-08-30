#sum of n number 
'''n=int(input("enter last term for sum:"))
sum=0
for i in range(1,n+1):
    sum=sum+i

print(sum)'''

# factorial
'''n=int(input("enter whose factorial u:"))
prod=1
for i in range(1,n+1):
    prod=prod*i

print(prod)'''

#sum of odd and even numbers separately
'''evensum=0
oddsum=0
n=int(input("enter last term for sum:"))
for i in range(1,n+1):
      if i%2==0:
            evensum+=i
      else:
            oddsum+=i

print(evensum)
print(oddsum)'''

#sum of all factors except itself
'''n=int(input("enter whose factor u want:"))

sum=0
for i in range(1,n):
     if n%i==0:
          print(f"factors are {i}")
          sum=sum+i

print(sum)
if sum==n:
     print("perfect number")
else:
     print("not perfect") '''

#prime number
'''n=int(input("enter whose nature u want to check:"))

count=0
for i in range(1,n+1):
     if n%i==0:
          count+=1

if count==2:
     print("prime number")
else:
     print("not prime") '''


#reverse a string

'''a="PYTHON"
rev=""
for i in range(len(a)-1,-1,-1):
    rev=rev+a[i]
print(rev)  '''


#count of digits, characters and special characters in a string

''' a="pa45a^$^jdj sj"
char=0
spchar=0
digits=0

for i in a:
    if i.isdigit(): # .isdigits()
        digits+=1
    elif i.isalpha(): # .isalpha()
        char=char+1
    else:
        spchar+=1

print(f"characters {char},speccial char{spchar},digits {digits}")
'''

#using unicode

#first find the unicodes of all

print(ord("0")) #48
print(ord("9")) #57
print(ord("a")) #97
print(ord("z")) #122
print(ord("A")) #65
print(ord("Z")) #90

a="pa45a^$^jdj sj"
char=0
spchar=0
digits=0

for i in a:
    if ord(i)>=48 and ord(i)<=57:
        digits+=1
    elif ord(i)>=97 and ord(i)<=122 or ord(i)>=65 and ord(i)<=90:
        char=char+1
    else:
        spchar+=1

print(f"characters {char},speccial char{spchar},digits {digits}")
