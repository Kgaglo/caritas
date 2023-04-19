# function to reverse characters in a string 
def strLength(my_string):
    reverseString = ""
    for i in my_string:
        reverseString = i + reverseString
    return reverseString
    
my_string = input("Please enter a phrase : ") #"Welcome to Caritas, we love doing this"

str_rev =strLength (my_string)

print ("the reverse of the string is : ",str_rev)