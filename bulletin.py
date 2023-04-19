
def collectGrades (totalNumbers):
    print ("Please enter ",totalNumbers,"numbers : ")
    for i in range (0, totalNumbers):
        element =float(input())
        myList.append (element)

def collectClass (classes):
    #print ("Please enter ",totalNumbers,"numbers : ")
    for i in range (0, classes):
        classe =  input("")
        myList1.append (classe)



def calculateAverage():
    total =0
    for i in range (0,len(myList)):
        total = total +myList[i]
    return (total/totalNumbers)

myList = []
myList1 =[]
classes = str(input("Please enter the classes you are taking : "))
collectClass(classes)
totalNumbers = int(input("average of how many numbers? : "))
collectGrades (totalNumbers)

average = calculateAverage()

print ("your average is :" + str (average))