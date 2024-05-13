import datetime

'''Employee Management System
~System allows employee data to be stored and managed~

-updating employee information (update_employee_info)
-searching for employees by name & department (search)
-Calculating Salary Expenses (total_expenses, salary * years_worked)

years_worked = todays date - hire_year

Class = Employee

'''
class Employee:
    '''Initializer of Employee class'''
    def __init__(self, name:str, job_title:str, department:str, salary:float, hire_year:int):
        self._name = name
        self._job_title = job_title
        self._department = department
        self._salary = salary
        self._hire_year = hire_year

    '''String representation for employee class'''
    def __str__(self):
        return f'Name: {self._name}\nJob Title: {self._job_title}\nDepartment: {self._department}\nSalary: {self._salary}\nHire Year: {self._hire_year}'
    
    '''Employee Information to a text file'''
    def write_employees(self, employee):
        with open(employee, 'a') as file:
            file.write(str(self))

    '''Mutator Method for name'''
    def set_name(self, name):
           self._name = name  

    '''Accessor Method for name'''
    def get_name(self):
           return self.name
    
    '''Mutator Method for job_title'''
    def set_job_title(self, job_title):
           self._job_title = job_title

    '''Accessor Method for job_title'''
    def get_job_title(self):
           return self.job_title	
    	   
    '''Accessor Method for department'''
    def get_department(self):
           return self.department
              
    '''Mutator Method for department'''
    def set_department(self, department):
           self._department = department

    '''Accessor Method for salary'''
    def get_salary(self):
           return self._salary
    
    '''Mutator Method for salary'''
    def set_salary(self, salary):
           self._salary = salary

    '''Accessor Method for hire_year'''
    def get_hire_year(self):
           return self._hire_year 

    '''Mutator Method for hire_year'''
    def set_hire_year(self, hire_year):
           self._hire_year = hire_year  

    '''Updating employee information'''
    def years_worked(self):
        current_year = datetime.datetime.now().year
        return current_year - self._hire_year

    '''Calculating salary expenses by salary * years worked'''
    def total_expense(self):
        return self._salary * self.years_worked()


#Creating Employee Obects 
employee1 = Employee("Sunny Smith", "Technician", "Technology", 67000, 2020)

#Return string representation of employee object
print(employee1)

# Updating employee information to include years worked
print("Years Worked:", employee1.years_worked())

# #Calculating salary expenses by salary * years worked
print("Total Expense", employee1.total_expense())

#writing employee information to a text file
employee1.write_employees("employee.txt")



