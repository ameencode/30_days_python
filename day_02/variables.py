# Day 2: 30 Days of python programming

first_name = "Ameenullah"
last_name = "Olalere"
full_name = first_name + " " + last_name
print(full_name)
country = "Nigeria"
city = "Lagos"
age = "old_enough"
year = 2026
is_married = True
is_true = True
is_light_on = False

# Defining multiple variables in one line
name, age, country, is_married = "Ameenullah", 20, "Nigeria", True  

# Checking the data types of the variables
print(type(first_name))  # <class 'str'>
print(type(last_name))   # <class 'str'>
print(type(full_name))   # <class 'str'>
print(type(country))     # <class 'str'>
print(type(city))        # <class 'str'>
print(type(age))         # <class 'str'>
print(type(year))        # <class 'int'>
print(type(is_married))  # <class 'bool'>
print(type(is_true))     # <class 'bool'>
print(type(is_light_on)) # <class 'bool'>

print(len(first_name))  # Length of first_name
print(len(last_name))   # Length of last_name
print(len(first_name) == len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
print(total)

variable_diff = num_one - num_two
print(variable_diff)

variable_product = num_one * num_two
print(variable_product)

variable_division = num_one / num_two
print(variable_division)

variable_remainder = num_two % num_one
print(variable_remainder)

variable_exp = num_one ** num_two
print(variable_exp)

floor_division = num_one // num_two
print(floor_division)

area_of_circle = 3.14 * (30 ** 2)
print(area_of_circle)

circum_of_circle = 2 * 3.14 * 30
print(circum_of_circle)

radius = input("Enter radius: ")
area_of_circle = 3.14 * (int(radius) ** 2)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

help('keywords')