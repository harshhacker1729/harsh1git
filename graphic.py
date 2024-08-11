leap=int(input("enter the year check leap year"))
if (leap%4==0):
    if(leap%100==0):
        if(leap%400==0):
            print("It is leap year")
        else:
            print("it is  not leap year")
    else:
        print("it is leap year")
else:
    print("it is not leap year")               
