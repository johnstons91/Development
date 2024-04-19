import re

TAKEN_USERNAMES = ['admin', 'admin123', 'superuser', 'superuser123']

# Meeting Requirements? (Username)
'''Username must start with a lowercase letter and only contain letters, numbers, and underscores. Username must not be in the list of taken usernames'''
def is_valid_username(username):
    # Checks the first digit for a lowercase letter
    '''isidentifier() checks for python valid identifier which includes letters, numbers, and underscores but does not by itself check the first digit'''
    if not username[0].islower() or not username.isidentifier():
        return False
    # Check if the username is in the list of taken usernames
    if username in TAKEN_USERNAMES:
        return False
    return True

# Meeting Requirements? (Password)
''' Password must be at least 8 characters long
# Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character'''
# Password must not contain spaces
def is_valid_password(password):
    # Check for at least 8 characters
    if len(password) < 8:
        return False
    # Check for uppercase letter
    if not re.search(r"[A-Z]", password):
        return False
    # Check for lowercase letter
    if not re.search(r"[a-z]", password):
        return False
    # Check for digit
    if not re.search(r"\d", password):
        return False
    # Check for special character
    if not re.search(r"[!@#$%^&*_-]", password):
        return False
    # Check for spaces
    if ' ' in password:
        return False
    return True

#Sign up username and password verification
def sign_up():
    # Displays username requirements
    print("\nSign up with us by creating a Username and Password to continue.\n\nUsername requirements:\n  -Username must start with a lowercase letter and only contain letters, numbers, and underscores")
    # While loop to allow for multiple attempts at creating a username
    while True:
        # Prompts user for username input
        username = input("\nPlease create a username: ")
        # Checks user input against the username requirements
        if is_valid_username(username):
            print("\nUsername has been created. Now let's create a password.")
            break
        else:
            print("Invalid username.\n  -Username must start with a lowercase letter and only contain letters, numbers, and underscores.")
            # Checks for taken usernames
        if username in TAKEN_USERNAMES:
                print("\nUsername taken. Please choose a different username.")
    # Displays password requirements
    print("\nPassword requirements:\n  -Password must be at least 8 characters long.\n  -Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character (!@#$%^&*_-).\n  -Password must not contain any spaces.")
    # While loop to allow for multiple attempts at creating a password
    while True:
        # Prompts user for password input
        password = input("\nPlease create a password: ")
        # Checks user input against the username requirements
        if is_valid_password(password):
            break
        else:
            print("Invalid password.\n  -Password must meet the requirements.")
    # Displays a successful sign up
    print("\nSign up successful! You can now log in.")
    # Continues from sign up to login using username and password
    log_in(username, password)

# Log in verification after successful sign up
def log_in(username, password):
    print("\nLog in to your account")
    # While loop to allow for multiple attempts at entering the correct username
    while True:
        # Prompts for user input for username
        input_username = input("Enter your username: ")
        if input_username == username:
            break
        else:
            print("Incorrect username. Please try again.")
    # While loop to allow for multiple attempts at entering the correct password
    while True:
        # Prompts for user input for password
        input_password = input("Enter your password: ")
        if input_password == password:
            # Displays successful login and adds the username that was created inside the {}
            print("\nLogin successful! {}!\n".format(username))
            break
        else:
            print("Incorrect password. Please try again.")
        

# The if __name__ == "__main__": block is a common Python idiom used to ensure that a block of code is only executed when the script is run directly, and not when it is imported as a module into another script.
if __name__ == "__main__":
    sign_up()
