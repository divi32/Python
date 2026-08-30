#CRUD- create , read, update , delete


#extend the list
#append always put value in last spot

a=[10,20,30,True,"hello",50]
a.append(60)
print(a)

#insert

a.insert(5,"world")
print(a)

#delete- remove, pop, clear
'''pop deletes and store the deleted value in another container'''
b= a.pop(-2)  #use inndex or else default last element is remmoved
print(a)
print(b)


#remove- uses values to remove value at first occurance
b=[10,20,30,True,"hello",50]
b.remove(20)
print(b)

#clear- remove all elements
a=[10,20,30,True,"hello",50]
a.clear()
print(a)

#sort
x=[3,5,7,9,2,0,10,3]
x.sort()
print(x)
#x.sort(reverse=True) -> for descending


#reverse
y=[3,5,7,9,2,0,10,3]
y.reverse()
print(y)
