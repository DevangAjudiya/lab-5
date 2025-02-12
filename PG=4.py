import random
ls=[]
posi=[]
negi= []
for i in range(30):
    b= random.randint(-10000,10000)
    ls.append(b)
print("list of 30 members")
for i in ls:
    print(i)
for i in ls:
    if(i>=0):
        posi.append(i)
    else:
        negi.append(i)

print("list of positives = ",posi)
print("list of negative = ",negi)
    
        
    
    
