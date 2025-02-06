import random
odd=[]
even=[]
b=[]


for i in range(5):
    b=random.randint(1,100)*2+1
    odd.append(b)
for i in range(5):
    b=random.randint(1,100)*2
    even.append(b)
    
print(odd)
print(even)
odd.remove(odd[2])
odd.insert(2,even)
print(odd)
for i in odd:
    if(len(odd[i])!=1):
        for j in odd[i]:
            b.append(j)
    else:
        b.append(i)

print(b)
