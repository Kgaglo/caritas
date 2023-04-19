index=int(input("Enter the index till you want the series : "))

firstNumber=0
secondNumber=1
temp=0

print(firstNumber)
print(secondNumber)
for i in range(0, index):
    temp = firstNumber + secondNumber
    firstNumber = secondNumber
    secondNumber = temp
    print(temp)