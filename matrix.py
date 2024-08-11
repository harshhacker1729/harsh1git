import random
rps=int(input("enter the rock-0 paper-1 scissor-2---"))
x=[0,1,2]
x=random.randint(0,2)

if(rps==x):
    print("match is tie")
elif(rps>=3):
    print("we have enter wrong number")
elif(rps<=1):
    print("computer wins")
elif(rps>x):
    print("user wins")
elif(x==2):
    print("win ho gya")
elif(rps==2):
    print("computer wins")
