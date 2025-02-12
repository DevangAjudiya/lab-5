import random
ls1=[]
ls2=[]
ls3=[]
for i in range(20):
    b=random.randint(1,30)
    ls1.append(b)
print("list-1 of 50 member =",ls1)
for i in range(20):
    b=random.randint(1,30)
    ls2.append(b)
print("list-2 of 50 member =",ls2)
for i in ls1:
    c=0;
    for j in ls2:
        if(i==j):
            c=c+1
    if(c==0):
        ls3.append(i)
print("ls3 = ",ls3)       
