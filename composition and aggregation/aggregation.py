class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        
    def annual_Salary(self):
        return (self.pay * 12) + self.bonus

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.obj_salary = salary # aggregation is applied here

    def total_salary(self):
        return self.obj_salary.annual_Salary()

salary = Salary(5000, 15000)
emp = Employee('prithivi', 24, salary)
print(emp.total_salary())