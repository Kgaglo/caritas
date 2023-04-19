age = int(input("Please enter your age : "))
while age <= 0:
    print ("age cannot be less than zero")
    age = int(input("Please enter your correct age :"))
print (f"Your age is {age}")