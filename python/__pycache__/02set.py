#difference: a-b uncommom out

s={1,2,3,30,40}
p={20,30,40,50}

print(s.difference(p)) 


#difference n update
'''
s-=p
print(s)
'''

#intersection -returns the common

print(s.intersection(p))

 #intersection n update

s&=p
print(s)

#subset: <= symbolises subset

x={1,2,3,30,40}
y={20,30,40,50}
q={30,40}

print(q<=y)  


#superset: all ele of q is in y
print(q>=y)

#symmetric_difference or write  x^=y

print(x.symmetric_difference(y))

#union: or use (x.union(y))
print(x|y)