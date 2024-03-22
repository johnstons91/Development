'''
Exercise - Valid email
Write some code that takes input from the user and prints whether it's a valid email address. Make sure to sanitize the user input with .strip()
An email address is valid if:
It has a "." at the third-to-last index
It has exactly one "@" symbol, at the fifth-to-last index or earlier
There is at least one character before the "@" symbol
It doesn't have any spaces (doesn't contain " ")
If all these conditions are met, print True. Otherwise, print False.
To do this, use boolean statements on your string.
Test your code on a few inputs to make sure it works!

'''

# Get input 
email = input("Hello, please enter your email address: ")
print(email)

# Sanatize Data (Clean Input)
email = email.strip()
print(email)

# Test 1: It has a "." at the third-to-last index
#email = 'johnstons91@outlook.com'
test_1 = (email[-3] =='.')
print("Test 1: Does the email have a '.' at the third-to-last index?", test_1)

# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier, email cannot be @.com
test_2 = email.count("@") == 1 and "@" in email[:-4]
print("Test 2: Does the email have a '@' symbol, at the fifth-to last index or earlier?", test_2) 

# Test 3: There is at least one character before the "@" symbol
test_3 = email.index("@") > 0
print("Is there at least one character before the '@' symbol?", test_3)

# Test 4: It doesn’t have any spaces (doesn’t contain " ")
test_4 = " " not in email
print("It doesn’t have any spaces?", test_4)

#Final Test with and Keyword
test_5 = test_1 and test_2 and test_3 and test_4
print("Does this email pass all tests?", test_5)








