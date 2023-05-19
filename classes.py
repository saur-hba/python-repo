# class Point:
#     def move(self):
#         print("move")

#     def draw(self):
#         print("draw")


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# print(point1.y)
# point1.draw()
# point1.move()

class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f"Hii, I am {self.name}")


person = Person("John Smith")
person.talk()
person2 = Person("Bob Smith")
person2.talk()