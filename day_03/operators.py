## Day_03 Excercises

age = 20
print(age)
height = 1.75
print(height)

base_of_triangle = int(input("Enter the base of the triangle: "))
height_of_triangle = int(input("Enter the height of the triangle: "))
area_of_triangle = 0.5 * base_of_triangle * height_of_triangle
print(area_of_triangle)

side_a = int(input("Enter the first side of the triangle: "))
side_b = int(input("Enter the second side of the triangle: "))
side_c = int(input("Enter the third side of the triangle: "))
perimeter_of_triangle = side_a + side_b + side_c
print(perimeter_of_triangle)

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))    
print(area_of_rectangle := length * width)
print(perimeter_of_rectangle := 2 * (length + width))

radius = int(input("Enter the radius of the circle: "))
area_of_circle = 3.14 * radius ** 2
print(area_of_circle)
circumference_of_circle = 2 * 3.14 * radius
print(circumference_of_circle)

# Calculating the slope, x-intercept and y-intercept of y = 2x -2
slope = 2
y_intercept = -2
x_intercept = -y_intercept / slope
print(slope)
print(y_intercept)
print(x_intercept)

#Slope (m = y2-y1/x2-x1)
# point (2, 2) and point (6,10)
slope = (10 - 2) / (6 - 2)
print(slope)
euclidean_distance = ((6 - 2) ** 2 + (10 - 2) ** 2) ** 0.5
print(euclidean_distance)

len("python") == len("dragon")

sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)

text = "There is no 'on' in both dragon and python"
print("on" not in text)

even_number = int(input("Enter a number: "))
if even_number % 2 == 0:
    print(f"{even_number} is an even number")
else:
    print(f"{even_number} is an odd number")

hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
print(f"Your weekly earning is: ${hours * rate_per_hour}")    

num_of_years = int(input("Enter number of years you have lived: "))
num_of_seconds = num_of_years * 365 * 24 * 60 * 60
print(f"You have lived for {num_of_seconds} seconds.")

# Write a Python script that displays the following table

n = 1
print(f"{n} {n**0} {n**1} {n**2} {n**3}")
n = 2
print(f"{n} {n**0} {n**1} {n**2} {n**3}")
n = 3   
print((f"{n} {n**0} {n**1} {n**2} {n**3}"))
n = 4
print(f"{n} {n**0} {n**1} {n**2} {n**3}")
n = 5
print(f"{n} {n**0} {n**1} {n**2} {n**3}")