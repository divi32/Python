#loop in dictionary 

#01 merge 2 dict 
'''method1 d1.update(d2)
'''
'''
d1={1:20,2:30,3:40}
d2={3:50,5:60,6:70}


for i in d2:
    d1[i]=d2[i] #d2 goes to d1 as key of d2 doesnot exist in d1 ,so new key get assign at end od d1
            # if common key exist , it get updated
print(d1)
'''
#01 merge 2 dict and common keys values get addded

d1={1:20,2:30,3:40}
d2={3:50,5:60,6:70}


for i in d2:
    if i in d1.keys():
        d1[i]=d2[i]+d1[i] #if key of d1 is present in d2 then add
    else:
        d1[i]=d2[i] 
print(d1)


#sum all values in a dict
'''
d1={1:20,2:30,3:40}

sum=0
for i in d1:
    sum+= d1[i]

print(sum)

'''

#counting the frequency
'''
l=["a","b","c","a","b","c","b","c"]

d={}

count=0
for i in l:
    if i in d.keys(): #check whether ele of list is present in dict
        d[i]=d[i]+1 #if ele exist then ele becomes key and value is incresed by 1 
    else:
        d[i]=1 #if not exist then a new key is created and value is assigned 1
print(d)
'''