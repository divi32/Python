#print positive and negative elements separately
''''
a=[2,-2,4,0,-4,-9]
b=[]
c=[]
for i in a:
    if i<0:
        b.append(i)
    else :
        c.append(i)

print("negative number:",b)
print("positive:",c)
'''

#average
a=[2,-2,4,0,4,9]
sum=0
for i in a:
    sum=+i
n=len(a)
avg=sum/n
print(avg)

#greatest element and its index
'''
a=[2,-2,4,0,9]
great=a[0]
index=0
for i in range(0,len(a)):
    
    if a[i]>great:
        great=a[i]
        index=i

print("index=", i,"greatest:",great)

'''

# second greatest element and its index
'''
a=[2,-2,9,0,8,0]
great=a[0]
sec_gre=a[0]
index=0
for i in range(0,len(a)):
    
    if a[i]>great:
        sec_gre=great
        sec_index=index
        index=i
        great=a[i]
    elif a[i]>sec_gre: #this steps ensures if larger number comes before second number than loops doesnot stop right way 
        sec_gre= a[i]
        

print("index=", sec_index,"second greatest:",sec_gre)
'''
#check if a list is already shorted

a=[2,-2,4,0,9]

for i in range(len(a)-1):
        
        if a[i]<=a[i+1]:
              print("ur list is not sorted")
              break
else:
     print("sorted")

