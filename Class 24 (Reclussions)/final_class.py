import pandas as pd

'''
Remove the duplicates from this list below. Can you do this in one line of code?

remove_dupes = [1, 2, 2, 3, 3, 3, 'new york', 'pennsylvania', 'new york', blue, blue, blue, green, 'hi', 'hello', 'hi']
'''


# remove_duplicates = set(remove_dupes)
# print(remove_duplicates)

''' Write a function that will take a single digit number written as a string and return the integer equivalent

for example
Input: 'five'
Output: 5

Hint: A dictionary can help you do this quickly

'''




'''Recursion

Using recursion, write a recursive function which takes a positive number as an argument and prints the numbers from the specified argument down to zero

(Courtesy of Python Simplified and Realpython.com)
'''




'''
You are given a dataset with the top 20 grossing movies of all time. Return a dataframe with just the movies in this list made in 2018 or after, put them in a new dataframe and create an excel file with the results

Filename - top_twenty_movies.xlsx
'''

df = pd.read_excel('top_twenty_movies.xlsx')
print(df)




'''
Hide the credit card number
Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent “4444444444444444”, then it should return “4444”.
Do not just cut out the first 12 characters and append the last for characters to a string.

ccnum = str(1234567890987654)
result = '************' + ccnum[12:16]
print(result)

 Loop through and solve with indexing


'''



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





