def concatString(input):
    result = ""
    for i in range (1, input+1):
        result = result +str(i)
    return result 

input = int(input("enter any digit :"))
print ("final String is : ", concatString(input))