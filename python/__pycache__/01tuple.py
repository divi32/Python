#tuple is immutable ,has index,duplicate values allowed

#create directly
a=("mon","tues",365,7)

#create via list
lists=[3,6,9,0]
tup=tuple(lists)
print(type(tup))

#implicit
def stud():
    return "divi",25102010,"f"

info=stud() #INFO is tuple
name,roll,sec=info #UNPACKING tuple name goes to divi ....
print("name",name)


#access element
print("element:")
print(tup[0])

#access index
print("index are:")
print(tup.index(9))
print(a.index("tues"))

#occurence of an element

x=(2,4,5,244,3,2,3,2,4,2,2)
print("count is:")
print(x.count(2))