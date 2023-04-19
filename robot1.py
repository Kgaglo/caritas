print ("Hello, welcome to our StayAwakeCoffe shop!!")
name = input ("What is your name ? :")
if name == "Armel":
    coffeeDrinker = input("Are you a cofee drinker ? :")
    if coffeeDrinker == "No":
        print ("get the hell out of here!")
        exit()
    else: 
        print("Oh you are one of those coffee Drinker !! Welcome in!!")
else: 
    print (name + " We are so glad to have you in here today!!")
#Creating menu 
menu = "Black coffee, Latte, Cappuccino, Espresso, Frappuccino"
# print menu 
print (name + " What would you like from our menu today ? \nHere is what we offer: \n " + menu)
#creating order 
order =input ()
if order == "Black Coffee":
    price = 5
elif order == "Latte":
    price = 7
elif order == "Cappuccino":
    price = 10
elif order == "Espresso":
    price = 6
elif order == "Frappuccino":
    price = 11
else: 
    print("We only sell coffee here! Get out !")
    price = 0
    exit()

quantity = input (" How many "+ order +" would you like? :")
total = price * int(quantity)

print("Sounds good!!\n You want "+ quantity + order + ",and your Total is : $" + str(total))
