# inheritance

# --------------------------------------------------------
# Type - 1  | Single Inheritance

# class Father:
#     def show_father_property(self):
#         print("Father owns a commercial building in hsr")

# class Son(Father):
#     def show_son_property(self):
#         print("Son owns a residential building in hsr")

# son = Son()
# son.show_son_property()
# son.show_father_property()

# --------------------------------------------------------
# Type - 2 | Multiple Inheritance

# class Father:
#     def show_father_property(self):
#         print("Father owns a commercial building in hsr")

# class Mother:
#     def show_mother_property(self):
#         print("Mother owns a commercial plot in hsr")

# class Child(Father, Mother):
#     def show_son_property(self):
#         print("Son owns a residential building in hsr")

# c = Child()
# c.show_father_property()
# c.show_mother_property()
# c.show_son_property()

# --------------------------------------------------------
# Type - 3 | Multi-Level Inheritance

class GrandFather:
    def show_grandfather_property(self):
        print("GrandFather owns a commercial plot in hsr")

class Father(GrandFather):
    def show_father_property(self):
        print("Father owns a commercial building in hsr")

class Child(Father):
    def show_child_property(self):
        print("child owns a residential building in hsr")

c = Child()
c.show_grandfather_property()
c.show_father_property()
c.show_child_property()


