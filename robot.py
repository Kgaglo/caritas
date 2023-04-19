print ("hello, welcome to our Caritas Store!!!")
name = input ("What is your name ? :")
if name == "Armel":
    evil = input ("are you evil?: \n")
    if evil == "Yes":
        print( "Get out Evil Julie, you are not welcomed in here ! ")
        exit()
    else: 
        print("You are one of those good Julies!! Please come in !!")

else : 
    print ("hello " + name + "\nThank you so much for coming in today !")

menu =  "Black Coffee, Latte, Espresso, Cappucino, Frappucino"

print (name + " What would you like from our menu today? Here is what we offer : \n" + menu)

order = input ()
if order == "Black coffee":  
    price = 8
elif order == "Latte":
    price = 5
elif order == "Espresso":
    price = 10
elif order =="Cappucino":
    price = 13
elif order == "Frappucino":
    price = 15
else:
    print("We only sell coffee here !!")
    price =0
    exit()

quantity = input ("how many " + order + " would you like ? \n")

total = price * int (quantity)
#print ("your total is : $" + str (total))
print ("sounds good " + name + ", you want " + quantity + " " + order + " , and your total is : $" + str (total) )

