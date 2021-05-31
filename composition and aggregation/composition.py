class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        
    def annual_Salary(self):
        return (self.pay * 12) + self.bonus

class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay, bonus) #composition is applied here

    def total_salary(self):
        return self.obj_salary.annual_Salary()

emp = Employee('prithivi', 24, 5000, 15000)
print(emp.total_salary())