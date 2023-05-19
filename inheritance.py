class Mammal:
    def walk(self):
        print("Walk")

# class Dog(Mammal):
#     pass

# class Cat(Mammal):
#     pass

# dog1 = Dog()
# cat1 = Cat()
# dog1.walk()
# cat1.walk()

class Dog(Mammal):
    def bark(self):
        print("Barks")

class Cat(Mammal):
    def is_annoying(self):
        print("is annoying")

dog1 = Dog()
cat1 = Cat()

dog1.walk()
dog1.bark()

cat1.walk()
cat1.is_annoying()
