# function to get number of characters in a string 
def strLength(my_string):
    len_count = 0
    for i in my_string:
        len_count =len_count + 1
    return len_count
    
my_string = input("Please enter a phrase : ") #"Welcome to Caritas, we love doing this"

str_len =strLength (my_string)

print ("the length of your phrase is : ",str_len)