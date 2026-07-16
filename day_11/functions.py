def add_two_numbers(x, y):
    sum = x + y
    return sum
print(add_two_numbers(5, 8))

def area_of_circle(r):
    pi = 3.14
    area = pi * r**2
    return area
print(area_of_circle(3))

def add_all_nums(*nums):
    total = 0
    for num in nums:
        if type(num) is not type(int):
            return f"Enter a valid number. All arguments must be a number" 
        total += num
    return total
print(add_all_nums(3, 4, 6, 5, 7))

def convert_celsius_to_fahrenheit(celsius):
    far = (celsius * 9/5) + 32
    return far
print(convert_celsius_to_fahrenheit(50))

def check_season(month):
    if month in ["december", "january", "februrary"]:
        return 'Winter'
    if month in ["march", "april", "may"]:
        return 'Spring'
    if month in ["june", "july", "august"]:
        return 'Summer'
    if month in ["september", "october", "november"]:
        return 'Autumn'
    else:
        return 'Invalid Month'
print(check_season(input('Input the name of a month')))

def calculate_slope(x1, x2, y1, y2):
    if x2 == x1:
        return "Undefined (vertical line)"
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(2, 5, 3, 4))


