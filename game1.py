num = input("Please enter a number between 1-5 (press q to quit) : ")
num1 = input ("Do you want to play animals  (y/n) : ")
while not num == "q":

    if num == "1":
        print ("You are going to be the first in everthing!!")
    elif num == "2":
        age = (input("How old are you ? : "))
        print (f"I told you ! your age is {age}")
    elif num == "3": 
        name = input ("What is your sweet name ? :")
        print (f"You must be {name} and you are a king ")
    elif num == "4": 
        movie = input ("What is your favorite movie ? :")
        answer = (input(f"Oh Noooo!! Why do you like {movie} ? :"))
        print (f"That {answer} is a terrible answer!  Good bye !")
        exit()
    elif num == "5": 
        play_again = input ("Do you want to play animals?  y/n:")
        if play_again  == "n":
            exit()
        else:
            print("Let's play again!!")
    else:
        print ("You are out of the range ")

    num = input("Please enter a number between 1-5 (press q to quit): ")

while num1 == "y":
    print("Let's play animals !!")
    num1 = input ("Do you want to play animals  (y/n) : ")

   
    



