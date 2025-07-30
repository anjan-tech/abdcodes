
class Student:

    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    #getter method to access private name
    def get_name(self):
        return self.__name
    
    #getter method to access private marks
    def get_marks(self):
        return self.__marks
    
    # setter method to update name
    def __set_name(self, new_name):      # private method
        if str(new_name):
            self.__name = new_name
        else:
            print("Name not valid")

    # setter method to update marks
    def __set_marks(self, new_marks):    # private method
        if 0 <= new_marks <=100:
            self.__marks = new_marks
        else:
            print("Marks should be between 0 to 100")

    def update_marks(self, new_marks):
        return self.__set_marks(new_marks)
    
    def update_name(self, new_name):
        return self.__set_name(new_name)

    def get_info(self):
        return f"{self.__name} scored {self.__marks} marks"
    
s1 = Student("Deepak", 80)
print(s1.get_info())

s1.update_marks(90)
print(s1.get_info())

s1.update_name("Deepak Yadav")
print(s1.get_info())

    

