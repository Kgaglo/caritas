def posNegZero (param):
    if (param ==0):
        print ("The number is zero or is invalid")
    elif(param>0):
        print ("The number is positive !!")
    else:
        print ("This number is negative")

num = float (input("please enter a number : "))
posNegZero(num)