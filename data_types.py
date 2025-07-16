#  list - Ordered collection of data types which are mutable and allows duplicates, and can store different data types

# fruits = ["apple", "mango", "banana", "cherry"]
# # print(fruits)

# # methods
# fruits.append("orange")
# # print(fruits)

# fruits.remove("banana")
# # print(fruits)

# fruits.insert(1, "apple")
# # print(fruits)

# # fruits.pop()
# # print(fruits)

# fruits.sort()
# # print(fruits)

# fruits.sort(reverse=True)
# # print(fruits)

# # print(fruits[1:4])

# fruits[2] = "Tomato"
# print(fruits)


# ------------------------------------------------------------------------------------------------

# tuple - ordered collection of different data types which is NOT mutable and allows duplicates

# vals = (1, 2, 3,"apple", True, False, 78.89, 6, 6)
# # print(vals)
# print(vals[1:4])
# print(vals.count(6))

# --------------------------------------------------------------------------------------------------

# sets - unordered collection of different data types which are unique and mutable

# my_set = {1, 2, 3, 4, "apple", "mango", 34.90, "mango"}
# print(my_set)

# my_set.add(5)
# print(my_set)

# my_set.remove(4)
# print(my_set)

# my_set.discard("mango")
# print(my_set)

# my_set.discard("cherry")
# print(my_set)

# my_set.remove("Orange")
# print(my_set)

# ------------------------------------------------------------------------------------------------

# dictionary - dictionary is a collection of key-value pair with unique keys, it is ordered and mutable

person = {
    "name": "John",
    "age": 24,
    "city": "Bangalore",
    "languages": ["English", "Kannada", "Hindi"],
    "Prog languages": {"Python": 4, "Java": 3}
}

print(person["age"])

person["Job"] = "Data Engineer"
person["age"] = 32
del person["city"]

print(person)

# print(person["languages"][1])
# print(person["Prog languages"]["Python"])

person.pop("languages")
print(person)

print(person.keys())
print(person.values())
print(person.get("Job"))
print(person["Job"])