import random
ls=[]

for i in range(50):
    b=random.randint(1,30)
    ls.append(b)
print("list of 50 member =")
for i in ls:
    print(i)
    
for i in ls:
    c=0
    for j in ls:
        if(i==j):
          c=c+1
        if(c>=2):
            ls.remove(j)
print("after removing duplicate " )
for i in ls:
    print(i)
