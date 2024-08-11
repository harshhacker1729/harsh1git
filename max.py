num=input("enter the number with space-- ")
x=num.split()
count=0
for i in x:
    count=count+1
print(count) #indention error if we do space it will give 1 2 3 4
for n in range(count):
    x[n]=int(x[n])
print(x)
maxm=x[0]
for m in x:
    if(m>maxm):
     maxm=m
print(maxm)