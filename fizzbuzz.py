a=int(input("enter the number want to fizzbuzz:- "))
for i in range(1,a+1):
    if(i%5==0 and i%3==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")       
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)