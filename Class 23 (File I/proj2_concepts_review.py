from datetime import datetime

# '''Write a program that will take the user's first name, and than the users last name, and print the value to a text file on 2 separate lines'''
#One method
firstname = input("First name:")
lastname = input("Last name:")

f = open('my_output.txt', 'w') #we are opening a new file
f.write(f'{firstname} \n {lastname}')
f.close()

#with open (PROJECT: USE THIS FOR EMPLOYEES, help WRITE FILE INFORMATION WITH EMPLOYEE)
with open('fullname.txt', 'w') as output:
    firstname = input("First name:")
    lastname = input("Last name:")
    output.write(f'{firstname}\n{lastname}')

# ''' Write a function called print_even_numbers that will take in a list of integer values and will extract the even numbers from that list and write to a text file let's try different parameters in our open function x, a, w'''

# def find_even_numbers(my_list):
#     output_list = []
#     for m in my_list:
#         if m % 2 == 0:
#             output_list.append(m)

#     with open('even_nums.txt', 'w') as output:
#         for o in output_list:
#             o = str(o)
#             output.writelines(o)

#     print('File Printed Successfully')


# # my_list = [1,2,3,4,5,6,7,12,14,15,21,22] #this is the data we pass into our function

# # find_even_numbers(my_list) #this is our function call

# # ''' Lets read in the song lyrics and put it into a list, but before we do, lets look at other options we have to read files in'''

# # with open('time_to_say_goodbye.txt', 'r') as lyrics:
# #     my_paragraph = lyrics.read()
# #     my_line = lyrics.readline()
# #     lyric_list = lyrics.readlines()

# # print(my_paragraph)
# # print(my_line)
# # print(lyric_list)

# ''' Bank Account class 
# Create the bank account class per the specifications in the powerpoint.

# Test after creating constructor
# Test string representation with print built in function 

# SideNote- 02f is decimal place
# '''
#Type hinting: line 57 (str, int, str, float). PROJECT: USE TO find object
class BankAccount:

    def __init__(self, customer_name: str, acct_num: int, date: str, balance: float):
        self.customer_name = customer_name
        self.acct_num = acct_num
        self.date = date
        self.balance = balance
        
    #String representation for employee class (displays persons name, job title, ect)
    def __str__(self):
        return f'Customer name: {self.customer_name}\nAccount number: {self.acct_num}\nDate of opening: {self.date}\nBalance: ${self.balance}'
    
    #Make a deposit, update the amount
    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} has been deposited in your account')

    #Make a withdrawl, update the amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Sorry, insufficent funds")
        else:
            self.balance -= amount
            print(f'{amount} has been withdrawn in your account')
    
    #Check balance
    def check_balance(self):
        print(f'Your current balance is {self.balance}')

    #Check date
    def days_since_opened(self):
        open_date = datetime.strptime(self.date, '%m-%d-%y')
        today = datetime.now()
        days_since_opened = today - open_date
        return f' {days_since_opened.days} days ago'
    
    #In project
    def print_customer_details(self):
        f = open('customer_details.txt', 'w')
        f.write(f'Customer name: {self.customer_name}\nAccount number: {self.acct_num}\nDate of opening: {self.date}\nBalance: ${self.balance}\nAccount opened: {self.days_since_opened()}')
        f.close()

#Name, Account number, date, deposit amount
ac_no_1 = BankAccount("Toninho Takeo", 2345, "05-05-24", 1000 )
ac_no_2 = BankAccount("Jim Jones", 5424, "01-05-22", 1000 )
ac_no_3 = BankAccount("Sally Field", 3242, "11-04-15", 1000 )
ac_no_4 = BankAccount("Burt Reynolds", 4325, "08-11-13", 1000 )

ac_no_1.check_balance()
ac_no_1.deposit(220)
ac_no_1.check_balance()
ac_no_1.withdraw(2250)
ac_no_1.print_customer_details()

print(ac_no_1)
# print(ac_no_2)
# print(ac_no_3)
# print(ac_no_4)

'''The strptime() function is a method of the datetime module in Python that creates a datetime object from a given string. The function takes two arguments: a string that represents a date and time, and a format code that specifies how the string is formatted
1. The format code consists of directives that indicate how to parse the string, such as %d for day of the month, %m for month, %Y for year, %H for hour, and so on
2. The table below shows some of the common directives and their meanings
'''