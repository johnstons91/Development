import re

#Username & Password Variables:
username = ''
password = ''

#Create account & requirements:

login = "Create username and password to sign up."

username_requirements = "Username requirements: 1.Start with a lowercase letter 2. Must contain only letters, numbers, and underscores"
password_requirements = "Password requirements: 1. At least 8 characters long. 2. At least 1 uppercase & lowercase letter. 3. At least 1 digit. 4. At least one character (!,?,@,#,$,^,&,*,_,-), 5.no spaces"
print(username_requirements)
print(password_requirements)

taken_usernames = {
    "admin": "admin",
    "admin123": "admin123",
    "superuser": "superuser",
    "superuser123": "superuser123"
}

def check_credentials(username, password):
    """Check if the username and password exist and match."""
    if username in taken_usernames and taken_usernames[username] == password:
        return True
    return False

def main():
    # Requesting username and password from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Checking credentials
    if check_credentials(username, password):
        print("Authentication successful!")
    else:
        print("Authentication failed. Invalid username or password.")

if __name__ == "__main__":
else:
    main()if len(user_input) 




#User ID requirements: 
# lower_case = usernames
taken_usernames = ['admin', 'admin123', 'superuser', 'superuser123']
first_letter = lower_case[0]
lower_case_test = first_letter.islower()

if lower_case_test is True:
    print("Usern. ")
else:
    print("Username is taken. ")



if users_username in taken_usernames :
    print()



# if then else 
chars = ('!','?','@','#','$','^','&','*','_','-')

#if passwords contains:(password == chars)

# error_messages = ['Incorrect username', 'Incorrect password', 'Invaild requirements']

# print(error_messages[0])
# print(error_messages[1])
# print(error_messages[2])







#Login successful