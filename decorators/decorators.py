class Employee:
    def __init__(self, first_name, last_name, email_type):
        self.first_name = first_name
        self.last_name = last_name
        self.email_type = email_type

    @property
    def email_id(self):
        return self.first_name + "_" + self.last_name + "@" + self.email_type +".com" 

    @property
    def fullname(self):
        return self.first_name + " " + self.last_name

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first_name = first
        self.last_name = last

    @fullname.deleter
    def fullname(self):
        print("Deleting name...")
        self.first_name = None
        self.last_name = None

emp = Employee("abcd", "efgh", "gmail")

emp.fullname = "Prithivirajan Karthikeyan"
print(emp.first_name)
print(emp.last_name)
print(emp.email_id)

del emp.fullname
