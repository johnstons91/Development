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
username = input("\nCreate username to login:")

while True:


