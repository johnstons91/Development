'''Creating two variables, one for first name, another for the last name.'''
first_name = 'Sarah'
last_name = 'Johnston'
full_name = first_name  + ' ' + last_name
print(full_name)
x= 'hello'
str2= 'Hello' .lower()
print(x)

test_character = 'b'
test_string = 'bananas'
print(test_character in test_string)

word_1 = 'happy' # capitalize me!

ex_1 = 'cerel' # capitalize me!
print(ex_1.capitalize())
print( 'cerel' .capitalize())

word_2 = 'SuPrIsE' #make me lower case!
print(word_2 .casefold())
print( 'SuPrIsE' .casefold())

word_3 = 'zoo' #make me lowercase
print(word_3.casefold())
print( 'zoo'.casefold())

word_4 = 'Good Evening'
print(word_4)
print(word_4.center(100)) #takes up 100 characters and center the string
print(word_4.center(50))

word_5 = 'pseudopseudohypoparathyrodoidism' #How many p's?
print(word_5.count('p'))

ex_5 = 'Antidisestablishmentarianism' # how many times does the letter 'e' occur?
print(ex_5.count('e'))

word_6 = 'I\tam\ta\ttab'
print(word_6)
print(word_6.expandtabs(10))

ex_6 = 'lets\t do\t some\ t coding! #lets try to increase the tabs to 10 whitespaces'
print(ex_6.expandtabs(15))

#find the position of the letter k
word_7 = 'omphaloskepsis'
print(word_7.find('k'))

#ex_7 = 'dichlorodifluoromethane' #find the position if the letter f
#print(ex_7.index(f))


#isalnum() Are all my characters alphanumeric? Alphanumeric is A-Z, a-z, and 0-9

test_3 = 'abcde'
test_4 = '012345'
# print(test_3.isalpha())
# print(test_4.isalpha())

ex_9 = 'LMNOP' #Are we all in the alphabet

#print(test)

test_7 = 'H1234'
test_8 = '9876'
print(test_7.isdigit())
print(test_8.isdigit())

test_9 = 'Zebra'

test_11 = 'Marshall'

ex_15 = 'Tempus Fugit' #check for title casing

my_colors = ['blue', 'green', 'red', 'orange', 'blue']
new_string = '&&' .join(my_colors)
print(new_string)

# Reference vs Value equality == vs is
x = 'hello' #declaring variable here
str2 = 'HELLO' .lower() 
print(x)
print(str2)
print(x == str2)
print(x is str2)
print(id(x))
print(id(str2))

#''' in'''
#test_character

ex_21 = '   sportsfan87   ' #sanitize this string

#strip() Returns a trimmed version of the string
username = '   jessica123    '
username_cleaned = username.strip()

user_input = input("what is your name? ")
print(user_input)

user_input = int(input("what is your favorite number? "))
print(int(user_input)) #casting the string to an integer
print(type(user_input))


#Get input from user
user_input = input('Good afternoon, please enter your input: ')
print(user_input)

#test input
result = user_input.isdigit()
print(result)

#provide output
print('Is your input a number or not?', result)
print(f'Is {user_input} a number or not', result)

#Take a word from the user. Then take a number from the user.

#Get user inout
user_word_input = ("Please enter your word: ")
user_number_input = input("Please enter your number: ")

#Convert where needed
length_of_word = len(user_word_input) #length of our word input

print(length_of_word)
#print(type_of)

#Comparison 
result = (length_of_word > user_number_input)

#output 
print(f'Is {user_word_input} longer than {user_number_input}?', result)
''' len() - Returns the length of a string, aka th enumber of characters in  a string.'''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
length_of_alphabet = len(alphabet)

''' create a variable that holds'''

animal = 'Wolves'
