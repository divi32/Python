# SYNTAX : a=[12,35,46]
'''
->each has index 0 1 2 3....
->list is mutable i.e changeable
->duplicate values allowed


'''

#create list and change value
a=[10,20,30,40,50,60,100]
print(a[-1]) #accessing

a[-1]=70 #changing
print(a)

#access using loop (using values)
for i in a:
    print(i)


#access using loop (using index)

for i in range(0,len(a)):
    print(i,":",a[i])

