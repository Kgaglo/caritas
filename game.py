num = input ("Please enter a number between 1-5 (enter q to quit):")
num2 = 2
while not num == "q": 
    if num == "1":
        print ("You are going to be the first in everything !!")
    elif num == "2":
        age = input("How old are you ? : ")
        print (f"I told you that you are {age} years old")
        #print ("I told you that you are" + age + "years old ")
    elif num == "3":
        name = input("What is your name please? : ")
        print (f"You must be  {name} and you are from a King family")
    elif num == "4":
        movie = input ("What is your favorite movie? : ")
        answer = input (f"Oh noooo!! Why do you like {movie} ?:")
        print (f"That {answer} is a terrible answer!! Good bye !")
        exit()
    

    num = input ("Please enter a  valid number between 1-5 (enter q to quit):")

# for i in range (0,num2):
#     total =0
#     total =total+i
# print (total)

