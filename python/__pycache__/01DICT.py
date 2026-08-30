#DICTIONARY- here keys= index, key is recommended to be unique
#


#creation
d={1:"apple",2:"mango",3:"grape",4:"banana"}
#access
print(d[1])

#expand dict
d[5]="kiwi"
print(d)

#update
d[2]="lichi"
print(d)

#clear
demo={1:"apple",2:"mango",3:"grape",4:"banana"}
demo.clear()
print(demo)

#get access
print(d.get(2))

#divides keys and values in a multiple tuples inside a list
print(d.items())

#keys 
print(d.keys())
print(d.values())

#dlete using key and return it
print(d.pop(3))
print(d)

#delete last item
print(d.popitem())
print(d)

newdict={1:"apple",2:"mango",3:"grape",4:"banana"}

#setdefault() : returns the value of the dpecified key.
#if key doesnot exist insert the key with the specified value
print(newdict.setdefault(9,"heii"))
print(newdict.setdefault(2))
print(newdict)


#update
newdict.update({2:"kiwi"})
print(newdict)