# string methods

# name = "Good Morning!"
# print(name.upper())
# print(name.lower())
# print(name.split(" "))  # returns array ["Good", "Morning!"]

# example = " Hello,People "
# print(example.strip())
# print(example)
# print(example.split(","))
# print(example.split(" "))

# String Formatters

# 1 - .format()
# 2 - f""

salary = 30000
position = "Team Lead"
# print("My salary is", salary, "and my position is", position)
# print("My salary is {0} and my position is {1}" .format(salary, position))
# print("My salary is {0} and my position is {1}" .format(position, salary))
# print("My salary is {sal} and my position is {pos}" .format(sal=salary, pos=position))
# print("My salary is {sal} and my poition is {pos}" .format(pos=position, sal=salary))

# 2. f {}
print(f"My salary is {salary} and my position is {position}")
