# This is the final exercise/exam of module 1 in the python fundamentals course - In this program we request input from the user and then check the input for the following:
# - make a for loop that loops through the chars of the quote we give
# - if it's an alphabitical char then add char to "word" variable
# - else add a blank char to "word" var
# - if the char is bigger than "h" then print it in upper chars
# - else just store a blank char in word var
# ----------------------------------------------------------------------------------

# define a function for letter finder(let_find) just the name of the function
def let_find():
# define a variable called quote that takes input from the user
    quote = input("Enter a 1 sentence quote, non-alpha separate words: ")
# define word variable that will store the whole chars later on. And define the quote variable to be equal for quote + " " (space)
    word = ""
    quote = quote + " "
# for loop to loop through each char in quote 
    for char in quote:
# if statement that checks if the chars are alpha and if true, char gets added to word var
        if char.isalpha():
            word += char
# else a space gets added to word var
        else:
            word += " "
# if statement that checks if the char provided is bigger or equals "h" and if true it prints it in upper case
            if word.lower() >= "h":
                print(word.upper())
                word = ""
# else just store a blank char in word var
            else:
                word = ""

# call the function 

let_find()
