# Employee class
class Employee:
  def __init__(self, name, employee_id, department, position):
  # Initialize the attributes
    self.name = name
    self.employee_id = employee_id
    self.department = department
    self.position = position

  def get_details(self):
  # Print the details of the employee
    print(f"Name: {self.name}, ID: {self.employee_id}, Department: {self.department}, Position: {self.position}")

# EmployeeManagement class
class EmployeeManagement:
  def __init__(self):
  # Initialize the list of employees
    self.employees = []

  def add_employee(self, employee):
  # Add an employee to the list
    self.employees.append(employee)

  def remove_employee(self, employee_id):
  # Remove an employee from the list
    self.employees = [employee for employee in self.employees if employee.employee_id != employee_id]

  def display_all_employees(self):
  # Display all employees
    for employee in self.employees:
        employee.get_details()

# Demonstrate the functionality
# Create some Employee objects
employee1 = Employee("John", "001", "IT", "Software Engineer")
employee2 = Employee("Jane", "002", "HR", "HR Manager")

# Create an EmployeeManagement object
employee_management = EmployeeManagement()

# Add the employees to the EmployeeManagement object
employee_management.add_employee(employee1)
employee_management.add_employee(employee2)

# Display all employees
print("All Employees:")
employee_management.display_all_employees()

# Remove an employee
employee_management.remove_employee("001")

# Display all employees
print("All Employees after removal:")
employee_management.display_all_employees()