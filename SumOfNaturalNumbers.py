def sumOfNaturalNum(param):
    result = param *(param +1)
    result = result / 2
    return result
#return (param * (param+1))

num = flot (input ("Please enter the number :"))

if (num >0):
    print ("The sum of N natural number is : ", sumOfNaturalNum(num))
else :
    print ("The number is invalid")