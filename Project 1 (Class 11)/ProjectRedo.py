import re

Usernames_Taken = ['admin', 'admin123', 'superuser', 'superuser123']

#Meeting Requirements to create username:
def does_username_meet_requirements(username):
    if not username[0].islower() or not username.isidentifier():
        return False
    if username in Usernames_Taken:
        return False
    return True

#Meeting requirements to create password:
def does_password_meet_requirements(password):
    if len(password) < 8:
        return False
    if not password[0].isupper(f'[A-Z]', password):
        return False



#Sign-up to Get user ID and Password:

def sign_up():
    print("Please sign up by creating a Username and Password to continue.")
#Prompt to create username:
while True:
    username = input("\nCreate username to login. \nUsername reqirements: \n ~Username must start with a lowercase letter and only contain letters, numbers and underscores.")
    if does_username_meet_requirements(username):
        print("\nYour username has been created. Lets now create a password")
        break
    else:
        print("Invaild Username. Username requirements: \n ~Username must start with a lowercase letter and only contain letters, numbers and underscores.")
    if username in Usernames_Taken:
        print("Username is taken. Please create a different username.")

    #Prompt to create passaword:
    print("\nPassword Requirements: \nPassword must be at least 8 characters long. \n~Contain at least one uppercase letter. \n~Contain at least one lowercase letter. \n~Contain at least one digit. \n~Contain at least one of these characters (!, ?, @, #, $, ^, &, *, _, -. \nDoes not contain any spaces. ")
while True:
    password = input("Create a password to complete the sign-up process: ")
    if does_password_meet_requirements(password):
        break
    else:
        print("The password is invalid. Please try again. \nPassword Requirements: \nPassword must be at least 8 characters long. \n~Contain at least one uppercase letter. \n~Contain at least one lowercase letter. \n~Contain at least one digit. \n~Contain at least one of these characters (!, ?, @, #, $, ^, &, *, _, -. \nDoes not contain any spaces.")
print("\nYou have successfully signed-up. please continue to log-in")

log_in(username, password)
        
#Verify username log-in after successful sign-up.
def log_in(username, password):
    print("\nPlease log-in to your account:")
while True:
    username_input = input("Enter your username: ")
    if username_input == username:
        break 
    else:
        print("Username is incorrect. Please attempt to try again.")
#Verify username log-in after successful sign-up:
while True:
    password_input = input("Enter your password: ")
    if password_input == password:
        print("Log-in successful! Thank you for joining. ")