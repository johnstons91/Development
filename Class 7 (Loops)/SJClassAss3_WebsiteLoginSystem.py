'''
Exercise

You're working on a project to develop a login system for a website. The website requires the user to enter a username and password to log in. Write a Python program that checks whether the user entered the correct username and password.
Create two variables called username and password and set them to any valid string values.
Prompt the user to enter their username and password using the input() function.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
If they match, print “Login successful.” If they don't, print “Incorrect username or password.”
'''
''' Exercise solution '''

# Prompt the user to enter their username and password using the input() function. Be sure to sanatize your data.

variable_1 = 'hotstuffcantlie'
variable_2 = 'awesomeness'

input_username = input("Enter your Username. ")
input_password = input("Enter your Password. ")

# Check if user entered correct username and password. Conditionals & logic operators that check if user input matches variables.

if input_username == variable_1 and input_password == variable_2:
    print("Login Successful")
else:
    print("Incorrect username or password")




