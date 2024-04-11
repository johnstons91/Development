''' Tuples & Sets '''

'''
Fun Facts about Tuples
    -ordered and unchangeable (example, storing a username and password, storing an RGB value that must not change)
    -can't add or remove items
    -round brackets
    -faster than lists
    -used to store constants
    -used heterogeneous data structures (integers, floats, strings, etc) for example someone's age, gender and last name, (15, 'M', 'JONES')
    -heterogenous data structures save memory. why? lists need to over-allocate to account for new elements
    -readability
    -lets the programmer or other programmer know, this data collection should not be altered
'''
# Count & Indexing

my_number_tuple = (1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 8, 8, 8, 9, 10, 10, 10, 10)

# Use the count Tuple method to count how many instances we have for 2, 3, 8, 9, 10



my_letter_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
# Use the index tuple method to return the position of letters b, d, f, h, and i


# Unpacking
user = ('Joe', 'Smith', 24)



# Loop through list of Tuples

weekdays = [("Monday", 1), ("Tuesday", 2), ("Wednesday", 3), ("Thursday", 4), ("Friday", 5), ("Saturday", 6), ("Sunday", 7)]


# Adding tuples
first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)



'''
You have a tuple of numbers:
numbers = (1,2,3,4,5,6,7,8,9,10,11,12)
You have a tuple of months:
months = ("January","February","March","April","May","June", "July","August","September","October","November","December")
Use these tuples to make a list of tuples where each tuple contains a number and the month it corresponds to, like this: [("January",1),...,("December",12)]
Now print each month and its number using tuple unpacking in a for loop. The first line of output should look like this:
January is month 1 of the year.
'''
months = ("January","February","March","April","May","June", "July","August","September","October","November","December")
numbers = (1,2,3,4,5,6,7,8,9,10,11,12)

# Create List of Tuples


# Use a for loop to unpack and generate strings

'''
Fun Facts about Sets

-unordered, unchangeable*, and unindexed.
* The items are unchangeable, but you can add and remove items.
Sets do not allow duplicates, so they are used to store a set of unique values. You use curly brackets for sets: { }
Because sets are unordered, you can't index them like a list. They don't have indexes at all. You can still loop through a set with a for loop.

'''


# Ways to create a set

# What am I?


# Pass in a list
my_fav_colors_list = ['green', 'blue', 'red']


# Unordered
my_unordered_set = {'blue', 'green', 'red', 'orange'}

# Unchangeable
my_unchangeable_set = {'hello', 'welcome', 'to', 'newyork'}

# Unindexed
my_unindexable_set = {'I', 'cant', 'be', 'indexed'}

# Break up a string


# No duplicates allowed
# my_cars = {'chevy', 'toyota', 'ford', 'ford', 'honda', 'honda'}

# No duplicates - How did we solve this problem before?

'''
8. Exercise: Removing All Duplicates
You have a list storing important data for your company, but it contains some duplicate entries. 
Go through your list and remove all the duplicates. When you're done, each item should appear in 
the list exactly once.
'''
''' With a for loop and appending'''

#original list
# states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']



''' With sets and returning a list '''

states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']

# We can loop through sets
# top_ten_movies = {'shawshank redemption', 'avatar', 'avengers', 'its a wonderful life'}


# Let's add silver .add()
# colors = {'blue', 'green', 'red'}


# Lets clear all our items .clear()
# transportation = {'cars', 'bikes', 'plane'}


# Lets create a copy .copy()
# sitcoms = {'friends', 'seinfeld', 'honeymooners'}


# Remove vermont from our set
# states = {'california', 'new york', 'vermont', 'connecticut'}



# Difference - What's different?
student_set = {'oleg', 'anna', 'farley'}
student_set_2 = {'oleg', 'anna', 'brenetta'}


# Intersect - What do we have in common?
my_schedule = {'mon', 'wed', 'thurs'}
dana_schedule = {'wed', 'fri', 'sat'}


# Union - uniquely list every pet
sarah_pets = {'dog', 'cat', 'bird'}
isaiah_pets = {'chickens', 'dog', 'fish'}
khadaziah_pets = {'bird', 'dog', 'fish'}
brenetta_pets = {'turtle'}


# Symmetric difference - Items outside of matching items

my_books = {'catcher in the rye', 'richest man in babylon'}
her_books = {'catcher in the rye', 'richest man in babylon', 'sounder'}


'''
Exercise - Sets
You work for a sales company and must generate a set of all customers who get a certain discount. The criteria for getting a discount is that they're over 60 years old and have made at least 5 purchases.
You have a set of customers over 60, and a set of customers who have made at least 5 purchases. Use a set operation to output a set of customers that fit both criteria for the discount. You can do this in one line of code.
Example:
over_60_years = {'Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf'}
over_5_purchases = {'Finn', 'Simone', 'Aaron', 'Dominic'}
Output: {'Dominic', 'Simone'}
'''

# Solve with an intersection - solve with 1 or 2 lines of code
over_60_years = {'Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf'}
over_5_purchases = {'Finn', 'Simone', 'Aaron', 'Dominic'}



'''
Exercise - Sets
See flowchart
You work at a company where some people know Python, some people know JavaScript, and some people know both.
In a loop, prompt the user to input an employee name, whether they know Python, and whether they know JavaScript. Use this to build two sets: a set of employees that know Python, and a set of employees that know JavaScript.
Use set operators to compute the following sets:
The set of employees that know both Python and JavaScript
The set of employees that know JavaScript, but not Python
The set of employees that know Python or JavaScript, but not both
'''
#Initialize our variables


#Data Collection Sets
python_devs, js_devs = set(), set()

print(python_devs)
print(type(python_devs))

#User Input
dev_type_input, dev_name_input = '', ''

#Error Messages
error_msgs = ('Invalid Input, please try again.', 'Thank you, have a nice day')

#User Instructions
print(''' 
Python and JS Developer Tracker
Instructions
      Input 's' or 'stop' at anytime to exit program
      To add a python developer type 'p' when prompted
      To add a JavaScript developer type 'js' when prompted
''')

#While Loop
while True:
    #Inputs
    dev_type_input = input("\n Type 'P' for PYTHON Developer, 'JS' for Javacript Developer, or 'STOP' to exit program: ").lower() 
    
    #If statements, break keyword, continue
    #This gives the user an exit
    if dev_type_input == 'stop':
        print(error_msgs[1])
        break

    #Get a dev type, add to our sets, and offer an exit
    if dev_type_input == 'p' or dev_type_input == 'js':
        dev_name_input = input("Enter developer name: ").lower()

        if dev_name_input == 'stop':
            print(error_msgs[1])
            break
        elif dev_type_input == 'p':
            python_devs.add(dev_name_input.title())
        else:
            js_devs.add(dev_name_input.title())
    else:
        print(error_msgs[0])
        continue

    #Set Operations   
    both_languages = python_devs.intersection(js_devs) #Everybody who knows both (Intersection means they know both)
    know_js_not_python = js_devs.difference(python_devs) #Know JS not Python - difference
    know_python_or_js_but_not_both = js_devs.symmetric_difference(python_devs) #Who knows python or js but not both

    print(both_languages, know_js_not_python, know_python_or_js_but_not_both)
    break
#if sets are empty, disaplay no data for user
if both_languages == set():
    both_languages = 'No Data'

if know_js_not_python == set():
    know_js_not_python = 'No Data'

if know_python_or_js_but_not_both == set():
    know_python_or_js_but_not_both = 'No Data'


print('RESULTS')
print('--------------------------------------------------------')
print(f'The following developers know both languages: {both_languages}')
print(f'The following developers know Javascript but not PYTHON: {know_js_not_python}')
print(f'The following developers know PYTHON or Javascript but not both: {know_python_or_js_but_not_both}')
print('---------------------------------------------------------')





# initialize our variables
# instructions
# inputs
# while loop
# print statement, formatted strings
# sets
# break keyword, continue, if statements
# string methods
# put our error messages in a tuple
# instructions
# initialize our variables
# put our error messages in a tuple
# while loop
# inputs
# string methods for cleanup if needed .strip(), .title()
# if statements, break keyword, continue,
# sets
# print statement, formatted strings, to display the set results