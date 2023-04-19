def primeOrNot(param):
    for i in range(2, param):
        if((param%i)==0):
            print (param, "is not a prime number")
            break
    else:
        print(param, "is a prime number")

num=int(input("Please enter the number : "))

if num > 1:
    primeOrNot(num)
else:
    print("Enter a valid number!")