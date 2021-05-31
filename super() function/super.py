class Parent:
    def __init__(self, number):
        print("from parent class", number)

class Parent1:
    def __init__(self, number1):
        print("from parent class", number1)

class Child(Parent, Parent1):
    def __init__(self):
        print("from child class")
        Parent1.__init__(self,"2")
        Parent.__init__(self,"1")
        #Parent1.__init__(self,"2")

child = Child()