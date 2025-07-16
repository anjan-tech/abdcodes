# functions/methods - is a block of code which we can reuse multiple times to perform a specific task.

# def addition():
#     return "something"

# def addition(a,b):
#     return a + b

# print(addition(10,30))

# print(addition(100,220))

# ---------------------------------
# find the squares

# n = int(input("Enter the number:"))

# def find_squares(x):
#     for i in range(x):
#         print(i**2)

# find_squares(n)

# ---------------------------------

# nested functions

# def outer(x):
#     def inner(y):
#         return x + y
#     return inner

# add_num = outer(5)
# print(add_num(10))

# ---------------------------------

# lambda functions - inline or single line functions or "Anonymous"

# def multiplication(a,b):
#     return a*b

# multiplication = lambda a,b: a*b

# print(multiplication(10,20))


# def is_even(a):
#     if a%2==0:
#         return True
#     else:
#         return False
    
# is_even = lambda a: f"{a} is an even num" if a%2==0 else f"{a} is an odd num"

# print(is_even(200))


# data = [10, 20, 30, 45, 55, 65]

# evens = list(filter(lambda x: x%2==0, data))

# squares = list(map(lambda x: x**2, evens))
# print(squares)

# ---------------------------------

# Generators
# A generator is a special type of function in Python that remembers its state and yields values one at a time, 
# instead of returning them all at once.

# def count_up_to(max_num):
#     cnt=1
#     while cnt<=max_num:
#         yield cnt
#         cnt+=1

# # for number in count_up_to(5):
# #     print(number)

# n = count_up_to(5)
# print(next(n))
# print(next(n))
# print(next(n))


# ---------------------------------

# list comprehensions

# def even_nums():
#     c = []
#     for i in range(2,31):
#         if i%2==0:
#             c.append(i)
#     return c

# This is a list comprehension, which is a short and clean way to create a list.
# [expression for item in iterable if condition]

# using list comprehension
even_nums = [i for i in range(2,31) if i%2==0]

# using lambda+filter
even_nums1 = list(filter(lambda x : x%2==0, range(2,31)))

print(even_nums1)

    






