
#Collect numbers and make a list 

def collectNumbers(totalNumber):
    print("please enter ",totalNumber, "numbers")
    for i in range (0,totalNumber):
        ele =float(input())
        myList.append(ele)

#Calculate the average

def calculateAverage ():
    total =0
    for i in range (0,len(myList)):
        total = total+myList[i]
    return (total/totalNumber)

myList =[]
totalNumber =int (input("average of how many numbers? "))
collectNumbers(totalNumber)# Calling the function to create the  list 

average = calculateAverage()
print ("Your average  is : " + str (average))