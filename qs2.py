# Extend the above solution and find the average expense per employee. 
# The calculation must be dynamic, there should be no need for you to manually code each addition 
# operations. This can be done by keeping track of the objects being created – in a list (But don’t 
# manually append the objects to a list, this must happen when the objects are being created).

class Employee:
    employees_list = []
    def __init__(self, name):
        self.name = name
        self.salary = 0
        self.__class__.employees_list.append(self)
    def update_salary(self, hours):
        self.salary = hours * 200
    def __add__(self, other):
        if isinstance(other, (Employee, PartTimeEmployee)):
            total_salary = self.salary + other.salary
            total_employee = Employee(name="Total")
            total_employee.salary = total_salary
            self.__class__.employees_list.append(total_employee)
            return total_employee
        else:
            raise TypeError("Unsupported operand type for +")

    @classmethod
    def get_average_expense(cls):
        total_expense = sum(employee.salary for employee in cls.employees_list)
        return total_expense / len(cls.employees_list)


class PartTimeEmployee(Employee):
    def update_salary(self, hours):
        self.salary = hours * 150


e1 = Employee(name=input("Enter name: "))
e1.update_salary(hours=int(input("Enter working hours: ")))

e2 = Employee(name=input("Enter name: "))
e2.update_salary(hours=int(input("Enter working hours: ")))

e3 = PartTimeEmployee(name=input("Enter name: "))
e3.update_salary(hours=int(input("Enter working hours: ")))

total_expense = e1 + e2 + e3
average_expense = Employee.get_average_expense()

print("Total salary expense:", total_expense.salary)
print("Average expense per employee:", average_expense)
