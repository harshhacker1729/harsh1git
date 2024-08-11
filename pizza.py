pizza=(input("small pizza = 100 - write s \n medium pizza=200- write m \n large pizza=300 write as- l\n"))
bill=0 
if pizza=='s':
    bill+=100
    print(bill)
elif pizza=='m':
    bill+=200
    print(bill)
else:
    bill+=300
print(bill)

add_per=input("add pepperoni want are not Y/N")
if (add_per=='y'):
    if(pizza=='s'):
      bill+=30
    else:
      bill+=50
print("you have bill is")
print(int(bill))



