#set has -> unique value, inside set we can store string ,tuple but not list because list is 
#immutable ,it is un ordered
'''indexing not available'''

s={}
print(type(s))  #we cannot create a empty set directly , it can be done by first creating a set and thn clearing all the elem
#list to set conversion

l=[1,2,2,8,7,7,9,9,9]
s=set(l)
print(s)  #duplicate values deleted

#direct create
se={1,'hello',(1,5,7)}

#add element
se.add(60)
print(se)

#clear
se.clear()
print(se)
print(type(se))

#discard /remove :remove specified ele
s={1,'hello',(1,5,7)}
s.discard((1,5,7))
print(s)


#pop remove any 1 elem randomly
s.pop()
print(s)


