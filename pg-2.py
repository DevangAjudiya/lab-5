import random
i=0
b=[]
for i in range(20):
    c=random.randint(1,7)
    b.append(c)
a=int(input("enter the the number = "))
print("the number occurrences =",b.count(a))
                                         

