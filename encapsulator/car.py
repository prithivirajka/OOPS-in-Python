#for encapsulation or private variables
class Car():
    def __init__(self, speed, color):
        self.__speed = speed
        self.color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

ford = Car(200, 'blue')
bmw = Car(225, 'black')
ferrari = Car(250, 'grey')

ford.set_speed(200)
bmw.set_speed(225)
ferrari.set_speed(250)

print(ford.get_speed())
print(bmw.get_speed())
print(ferrari.get_speed())

#print(ford.__speed)

# ford.speed = 200
# bmw.speed = 225
# ferrari.speed = 250 

# ford.color = 'blue'
# bmw.color = 'black'
# ferrari.color = 'grey'

# print(ford.speed)
# print(bmw.speed)
# print(ferrari.speed)

# print(ford.color)
# print(bmw.color)
# print(ferrari.color)


