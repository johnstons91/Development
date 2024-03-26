import re

TAKEN_USERNAMES = ['admin', 'admin123', 'superuser', 'superuser123']

def is_valid_username(username):
    # Check if the username meets the requirements
    # Username must start with a lowercase letter and only contain letters, numbers, and underscores
    # Username must not be in the list of taken usernames
    if not username[0].islower() or not username.isidentifier():
        return False
    if username in TAKEN_USERNAMES:
        return False
    return True

def is_valid_password(password):
    # Check if the password meets the requirements
    # Password must be at least 8 characters long
    # Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character
    # Password must not contain spaces
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*_-]", password):
        return False
    if ' ' in password:
        return False
    return True

def sign_up():
    print("\nSign up with us by creating a Username and Password to continue.\nUsername requirements:\n\n-Username must start with a lowercase letter and only contain letters, numbers, and underscores")
    while True:
        username = input("\nPlease create a username: ")
        if is_valid_username(username):
            print("Username has been created.")
            break
        else:
            if not username[0].islower() or not username.isidentifier():
                print("\nInvalid username.\nUsername must start with a lowercase letter and only contain letters, numbers, and underscores.")
            elif username in TAKEN_USERNAMES:
                print("\nUsername taken. Please choose a different username.")
    print("\nPassword requirements:\n\n-Password must be at least 8 characters long.\n-Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character (!@#$%^&*_-).\n-Password must not contain any spaces.")

    while True:
        password = input("\nPlease create a password: ")
        if is_valid_password(password):
            break
        else:
            print("Invalid password. Password must be at least 8 characters long and meet the requirements.")

    print("Sign up successful! You can now log in.")
    log_in(username, password)

def log_in(username, password):
    print("\nLog in to your account:")
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")

    while True:
        if input_username == username and input_password == password:
            print("\nLogin successful! {}!".format(username))
        elif not input_username == username and input_password == password:
            print("Incorrect username or password. Please try again.")
        return

if __name__ == "__main__":
    sign_up()