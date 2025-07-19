from abc import ABC, abstractmethod            # ABC - Abstract base class

class Animal(ABC):                             # Abstract class
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):           # the classes which inherit the abstract class, must and should implement the abstract methods in it.
    def sound(self):
        print("Dog barks!")

class Cat(Animal):
    def sound(self):
        print("Cat meows!")

    def cat_sound(self):
        print("Cat meows!")

# a = Animal()   # Abstract classes cannot be instantiated, its object cannot be created, Abstract classes are in-complete classes
# a.sound()

d = Dog()
d.sound()

c = Cat()
c.cat_sound()

# --------------------------

# Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    # @abstractmethod
    # def dummy(self):
    #     pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
    
    def circumference(self):
        return 3.14 * 2 * self.radius
    
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
c = Circle(5)
r = Rectangle(4,6)

print(f"Circle area: {c.area()}")
print(f"Rectangle area: {r.area()}")
print(f"Circumference of a circle: {c.circumference():.2f}")