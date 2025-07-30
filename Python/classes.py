# class


# class person:

#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return f"Hello {self.name}, Good Evening!"
    
# Dileep = person("Dileep")
# print(Dileep.greet())
    
# Farooq = person("Farooq")
# print(Farooq.greet())

name = "Dileep"

class Car:

    def __init__(self, brand: str, color: str, speed: int):
        self.brand = brand  #public variable
        self.color = color
        self.speed = speed

    def drive(self):
        return f"The {self.color} {self.brand} is driving at the speed of {self.speed} km/hr"
    

toyota = Car("Toyota", "Red", 80)
hundai = Car("Hundai", "White", 100)
Kia = Car("Kia", "Purple", 140)

print(toyota.drive())
print(hundai.drive())
print(Kia.drive())
print(Kia.brand)



