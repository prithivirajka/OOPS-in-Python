class Rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        print("printing for testing") #To check number of times a class is called

rect1 = Rectangle(20, 25)
rect2 = Rectangle(30, 20)

print(rect1.height * rect1.width)
print(rect2.height * rect2.width)
