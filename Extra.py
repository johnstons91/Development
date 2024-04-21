'''Set sys id and pass'''
# sys_id = 'admin'
# sys_password = 'password'

''' Prompt User'''
# user_id = input("Please enter your username: ")
# user_password = input("Please enter your password: ")

'''Our initial check, while not equal we will enter loop.'''
# while sys_id != user_id and sys_password != user_password:
'''We entered the loop. this means the username/password did not match'''
#     print("Incorrect username or password")
#     user_id = input("Please enter your username: ")
#     user_password = input("Please enter your password: ")

# print("Login Successful") # Outside of the while loop'''


'''Login part of code'''
while True:
    if register_username == username and login_password == password:
        print("Login Successful")
        break
    else:
        print("Incorrect username and password")