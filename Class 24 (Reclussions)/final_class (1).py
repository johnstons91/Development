import pandas as pd

'''
Remove the duplicates from this list below. Can you do this in one line of code?

remove_dupes = [1, 2, 2, 3, 3, 3, 'new york', 'pennsylvania', 'new york', blue, blue, blue, green, 'hi', 'hello', 'hi']
'''

remove_dupes = [1, 2, 2, 3, 3, 3, 'new york', 'pennsylvania', 'new york', 'blue', 'blue', 'blue', 'green', 'hi', 'hello', 'hi']

print(set(remove_dupes))



''' Write a function that will take a single digit number written as a string and return the integer equivalent

for example
Input: 'five'
Output: 5

Hint: A dictionary can help you do this quickly

'''
def word_to_integer(word): 

    single_digit_number = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

    for key, value in single_digit_number.items():
        if key == word:
            print(value)
    
# word_to_integer('five')









'''Recursion

Using recursion, write a recursive function which takes a positive number as an argument and prints the numbers from the specified argument down to zero

recusive- a function that calls itself.
recursion- technique of employing a reclusive function
Programming problems are best solved using recursion 

(Courtesy of Python Simplified and Realpython.com)
'''

def countdown(n):
    print(n)
    if n == 0:
       return n
    else:
       return (countdown(n - 1))

# countdown(5)

'''
You are given a dataset with the top 20 grossing movies of all time. Return a dataframe with just the movies in this list made in 2018 or after, put them in a new dataframe and create an excel file with the results

Read an excel file
Use the .loc function to filter the dataframe
Output to excel
Filename - top_twenty_movies.xlsx
'''
# df = pd.read_excel('top_twenty_movies.xlsx')
# print(df)
# top_20 = df.loc



'''
Hide the credit card number
Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent “4444444444444444”, then it should return “4444”.
Do not just cut out the first 12 characters and append the last for characters to a string.

ccnum = str(1234567890987654)
result = '************' + ccnum[12:16]
print(result)
 Loop through and solve with indexing
'''
def mask_cc_number(ccnum):

    amex = ''
    for c,d in enumerate(ccnum):
        if c < 12:
            amex += '*'
        else:
            amex += d
    return amex

ccnum = '7594217083211426'
# print(mask_cc_number(ccnum))


    



'''
Repeat the characters
Create a Python function that accepts a string. The function should return a string, with each character in the original string doubled. If you send the function “now” as a parameter, it should return “nnooww,” and if you send “123a!”, it should return “112233aa!!”.

Hint: Looks like a job for lambda functions and filters
'''


str_1 = 'now'
str_2 = '123a!'



''' 
Create a function, use a for loop and conditionals (if statements) to solve the following:
Given a list of even numbers, odd numbers, and words, create a function that will create a list of even numbers, a list of odd numbers, and a list of words. (3 separate lists)

data = [1,2,3,4,5,6,7,8,9,10,11, 'horse', 'mule', 'ketchup', 'sunshine']
'''





