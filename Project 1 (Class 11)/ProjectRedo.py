import re

usernames_taken = ['admin', 'admin123', 'superuser', 'superuser123']
error_messages = ['Invalid username', 'Username Taken', 'Invalid Password', 'Incorrect username and password']
messages = ['Sign up successful', 'Login successful']

print("To sign up, please enter a username and password.")
print("Username must start with a lowercase letter and only contain letters, numbers, and underscores.")
print("Password must be at least 8 characters long. Contain at least 1 uppercase letter, 1 lowercase letter, 1 digit, & 1 special character (!@#$%^&*_-). Must not contain any spaces.")

while True:
    username = input("Create Username: ")
    pwd = input("Create Password: ")
    #Checking username
    username_check = username[0].islower() and username.isidentifier() 

    if not username_check: 
        print(error_messages[0])
        continue

    if username in usernames_taken:
        print(error_messages[1])
        continue

    #Checking password   
    if len(pwd) < 8:
        print(error_messages[2])
        continue

    if not re.search(r'[!@#$%^&*-]', pwd):
        print(error_messages[2])
        continue

    if re.search(r'\s', pwd):
        print(error_messages[2])
        continue
    else:
        print(messages[0])

    print("Enter username and password to login.")
    un_log_in = input("Username: ")
    pw_log_in = input("Password: ")
 
    if un_log_in == username and pw_log_in == pwd:
        print(messages[1])
        break
    else:
        print(error_messages[3])
        continue