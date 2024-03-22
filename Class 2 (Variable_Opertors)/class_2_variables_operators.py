# ---> Hashmark (Can leave a comment)

#Print Built in Function
print('Hello World') #Prints Hello World in the terminal

greeting = 'Happy Wednesday' #Prints Happy Wednesday in terminal
print(greeting)

first_name = 'Sarah'
print(first_name)

# Addition
print(4 + 2) #Prints 6 in terminal
print(5 + 5)
print(100 + 5)


# # Subtraction (prints the numbers in terminal)
print(10 - 3)
print(4 - 3)
print(10 - 5)

# Multiplication
print(3 * 3)
print(2 * 8)
print(5 * 7)

# Division
print(10 / 2)
print(5 / 3)
#print(5 / 0) #Error 

try: 
    print(5 / 0)
except ZeroDivisionError as e:
    print("You cannot divide by zero. Have a great day")

# Exponents
print(5 ** 5)
print(2 ** 5)
print(3 ** 6)


# # Integer Division
print(10 // 3)
print(4 // 3)
print(5 // 2)

# Modulo/Mod/Remainder (Used to determine if a number is even or odd)
print(5 % 2)
print(10 % 4)
print(6 % 2)

# Program to find the perimeter of a rectangle (perimeter = 2 * (length + width))

length = 10
width = 7
perimeter = 2 * (length + width)
print('The perimeter of this rectangle is', perimeter)

# Data Types: Integers, String, Bool, Float, List, Directory

# Integer
num_one = 5
print(num_one)
print(type(num_one)) #print built-in function, in that is type function, then variable function
#When you update terminal it shows that the class type is an integer

# String

fav_color = 'blue'
print(fav_color)
print(type(fav_color))


# Bool (True or False, capital. Has no quotes "".)

technical_errors = True
print(technical_errors)
print(type(technical_errors))

technical_errors = False
print(technical_errors)

# Float (Means there is a decimal) 

num_two = 1.22
print(num_two)
print(type(num_two))


# String

first_name = 'Sarah'
last_name = 'Johnston'
fullname = first_name + ' ' + last_name #Addition Opertor
print(fullname)
print(first_name, last_name)

# List (goes in [])

student_grades = [100, 95, 70, 85, 40]
print(student_grades)
print(type(student_grades))

#called a For loop
for s in student_grades:
    print(s)

# Dictionary          Key           Value
demographic_info = {"First Name": "Sarah",
                    "Last Name": "Johnston",
                    "State": "New York"}

print(demographic_info)
print(type(demographic_info))

# Cast a string to an integer (Created a variable with a number value within a string.)
my_string = '5'
print(type(my_string))

new_number = int(my_string) #Casting our string to an integer
print(new_number)
print(type(new_number))

# Cast integer to string
second_num = 10
print(type(second_num))

new_string = str(second_num)
print(new_string)
print(type(new_string))

# Student grade dataset (Length function)
fav_colors = ['blue', 'black', 'purple', 'green'] #List item has 4 elements
num_colors = len(fav_colors)
print(num_colors)

#Counts number of letters in the word orange
color = 'orange'
my_count = len(color)
print(my_count)

#loops through and gives you every single letter in each line.
for c in color:
    print(c)

# finding amount of assignments


# Perimeter of a rectangle


# Determine perimeter and display output


# Fahrenheit to Celsius
fahrenheit = 89

celsius = (fahrenheit - 32) * 5/9
print(celsius)

# Eval
cold_weather = "True"
print(eval(cold_weather))

def sayHello(word):
    return word
    print('Hello', word)

sayHello('Sarah')
'''
# You are given a triangle with a side #1 of 4, base of 6, and side #2 of 3. Create
a brief python script that will determine the perimeter of the triangle. Comment your code

1. Print the perimeter
2. Using boolean operators is side #1 greater than the base?
3. Using boolean operators is side #2 less than the base?
4. Using boolean operators is base larger than or equal to side #1?
'''

#Perimeter

#Boolean Operators: side #1 > the base

#Boolean Operators: side 2 < the base

#Boolean Operators: base >= side #1







