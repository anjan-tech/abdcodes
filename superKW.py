# super()

class Parent():
    def __init__(self):
        print("Parent Constructor")

    def show(self):
        print("This is the parent method")

class Child(Parent):
    def __init__(self):
        super().__init__()              # --> calls the parent constructor method
        print("Child Constructor")

    def show(self):
        super().show()                  # --> calling parent class method called show()
        print("This is the child method")

# c = Child()
# c.show()

# -----------------------------------------------------

class Trainer:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is learning basic driving")

class AdvancedTrainer(Trainer):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level
        print(f"{self.name} is now learning {self.level} driving")

student = AdvancedTrainer("Hari", "sports")

