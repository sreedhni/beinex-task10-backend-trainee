"""
             OOPS - Task
Task 1
Create a class Employee with name and salary attributes.
The salary must be calculated and should be initialized to zero.
Create a method to calculate the salary by taking the no of hours worked and multiply it by 200.You
can give no of hours to the method as an argument.
Now create a child class PartTimeEmployee by inheriting the Employee class, and by using method
overriding (create salary calculation method in this class also with the same name)
get the salary of part time employee by multiplying no of hours worked by 150.
Create 3 objects for each class.
Now implement '+' operator overloading and find the total salary expense for keeping those
employees by adding up the objects together.
Eg:
e1 = Employee(name="John")
e1.update_salary(hours=6)
e2 = Employee(name="Robin")
e2.update_salary(hours=8)
e3 = PartTimeEmployee(name="Jake")
e3.update_salary(hours=8)
# The below line should work.
total_expense = e1 + e2 + e3      """


class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def calculate_salary(self, work_hours):
        self.salary = work_hours * 200

    def __add__(self, other):
        total_salary = self.salary + other.salary
        total_employee = Employee(name="Total")
        total_employee.salary = total_salary
        return total_employee


class PartTimeEmployee(Employee):
    def calculate_salary(self, work_hours):
        self.salary = work_hours * 150


ey1_name = input("Enter the name of the first employee: ")
ey1_hours = int(input("Enter the number of hours worked by " + ey1_name + ": "))

ey2_name = input("Enter the name of the second employee: ")
ey2_hours = int(input("Enter the number of hours worked by " + ey2_name + ": "))

ey3_name = input("Enter the name of the third employee: ")
ey3_hours = int(input("Enter the number of hours worked by " + ey3_name + ": "))

e1 = Employee(name=ey1_name)
e1.calculate_salary(work_hours=ey1_hours)

e2 = Employee(name=ey2_name)
e2.calculate_salary(work_hours=ey2_hours)

e3 = PartTimeEmployee(name=ey3_name)
e3.calculate_salary(work_hours=ey3_hours)

total_expense = e1 + e2 + e3
print("Total salary expense:", total_expense.salary)
