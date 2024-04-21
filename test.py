import re

usernames_taken = ['admin', 'admin123', 'superuser', 'superuser123']
error_messages = ['Invalid username', 'Username Taken', 'Invalid Password']
messages = ['Sign up successful', 'Login successful']

print("To sign up, please enter a username and password.")
print("Username must start with a lowercase letter and only contain letters, numbers, and underscores.")
print("Password must be at least 8 characters long. Contain at least 1 uppercase letter, 1 lowercase letter, 1 digit, & 1 special character (!@#$%^&*_-). Must not contain any spaces.")

while True:
    username = input("Create Username: ")   
    if not re.match(r'^[a-z]\w*$', username): 
        print(error_messages[0])
        continue
    if username in usernames_taken:
        print(error_messages[1])
        continue
    break

pwd = input("Create Password: ")
while True:
    if len(pwd) < 8:
        print("Password must be at least 8 characters long.")
        pwd = input("Create Password: ")
        continue
 
    if not re.search(r'[!@#$%^&*-]', pwd):
        print("Password must contain at least one of the following special characters: !, @, #, $, %, ^, &, *, -")
        pwd = input("Create Password: ")
        continue
 
    if re.search(r'\s', pwd):
        print("Password must not contain any spaces.")
        pwd = input("Create Password: ")
        continue
    else:
        print(messages[0])
    break

print("Enter password and username to login.")   
un_log_in = input("Username: ")
pw_log_in = input("Password: ")
username = un_log_in
pwd = pw_log_in

while True:    
    if username == un_log_in and pwd == pw_log_in:
        print("Invalid username and password.")
        continue 
    
    break

print(messages[1])


    
    
    