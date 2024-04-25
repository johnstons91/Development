'''Create python file called name_module.py. 

Create  3 functions w/ 2 strings (1st name + last name):
 1. full_name- concatenate and return the full name
 2. reverse_name- flip name around (
 3. get_initials- take 1st + last nam, returning with initials
   
 Create a second python file, called name.py. 
 Import the module you just created and call the function with the necessary arguments so it prints a full names, reverse names, and initials as needed in the terminal. '''

print('Import successful')

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

def full_name(first_name, last_name):
    for f in full_name:
        full_name = first_name + last_name
    return True

full_name(first_name, last_name)

pass 


# def reversed_string(text):
# ..result = ""
# ...     for char in text:
# ...         result = char + result
# ...     return result
# ...

# >>> reversed_string("Hello, World!")
# '!dlroW ,olleH'





# # def reverse_name(name):
#       return pd.join(reversed(full_name)) in name


# def get_initials(name):