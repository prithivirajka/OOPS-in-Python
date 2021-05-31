class Rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        print("printing for testing")

rect1 = Rectangle(20, 25)
rect2 = Rectangle(30, 20)

# rect1.height = 20 
# rect2.height = 30 

# rect1.width = 25 
# rect2.width = 20 

print(rect1.height * rect1.width)
print(rect2.height * rect2.width)