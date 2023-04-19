def reverseNumber (num):
    rev = 0
    while num!= 0:
        rev =(rev *10) + (num % 10)
        num = num // 10
    
    return rev

num = int(input ("Please enter any number : "))
rev = reverseNumber (num)

if (rev ==num):
    print ("The number is a palyndrome")
else :
    print("This is not a palyndrome")
