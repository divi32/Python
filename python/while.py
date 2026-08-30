#extract each digits and reverse it

a=24979
rev=0  #  newrev=rev*10+ last term

while a>0:
     rev=rev*10+a%10
     a=a//10
print(rev)