# if str is    D I V Y A
# Then it is   0 1 2 3 4   as index
# or          -5-4-3-2-1

# [start: End: skip] or [index] for sigle character
#[:n] means starting to n-1
#[n:] means n to end 
#[:] means starting to end all
#[n:] means n to end 



name="harrywillyoumarryme"
nam=name[0:3]  #starts from 0 till 3 excluding 3
print(nam)
print(name[-4:-1])
print(name[1:4])
print(name[:]) 

print("now with skips......")

#print(name[-4:-1])
print(name[1:8:2])

