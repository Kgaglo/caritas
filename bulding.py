myList = []
totalNumbers  = int (input("Vous voulez faire la moyenne de combien de nombres ?:  "))

def collectNumbers (totalNumbers):
    print ("Entrez les ",totalNumbers, "nombres en tapant a chaque fois sur la touche Entree: ")
    for i in range (0,totalNumbers):
        element=float (input())
        myList.append(element)


def average():
    total =0
    for i in range (0, len(myList)):
        total = total + myList[i]
    return (total/totalNumbers)

collectNumbers (totalNumbers)
myAverage = average()
print ("La moyenne est de : " + str(myAverage))