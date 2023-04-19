num1 =40
num2=30

if num1<num2 :
    print ("before swap",num1, num2)

    num2 =num2+num1
    num1=num2-num1
    num2 =num2-num1

    print ("after swapping",num1, num2)

else :
   print ("before swap",num1, num2)

   num1 = num1+num2
   num2= num1-num2
   num1 = num1-num2

   print ("after swapping",num1, num2)

