def collectNumbers(totalNumbers):
    print ("Please enter", totalNumbers,  "numbers:")
    for i in range (0, totalNumbers):
        element= float(input())
        myList.append(element)

def averageOfNumbers ():
    total = 0
    for i in range (0,len(myList)):
        total = total + myList[i]
    return (total/totalNumbers)

myList = []        
totalNumbers = int (input ("average of how many numbers? : "))
collectNumbers(totalNumbers)
average = averageOfNumbers()
print(" your average is :"+str(average))