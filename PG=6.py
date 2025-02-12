ls=[]
print("enter the temp in fahreneit =")
for i in range(5):
    b=int(input())
    ls.append(b)
print("the list temp in fahreneit= ",ls)
for i in range(5):
    ls[i]=(ls[i]-32)*5/9
print(" the list temp in celsius= ",ls)
