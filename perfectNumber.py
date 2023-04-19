num = int(input("Please enter a number : "))
sum = 0 
for i in range (1, (num // 2) +1):
    rem = num % i
    if rem ==0:
        sum = sum + i
if sum == num :
    print ("This is a perfect number")
else :
    print ("This is not a perfect number")
