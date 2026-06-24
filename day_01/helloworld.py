name = "Ameenullah"
other_name = "Olalere"

full_name = name + " " + other_name
print(full_name)
print(type(full_name))
print(type(10))
print(type(3.14))
print(type(4 - 4j))
print(type(True))
print(type(None))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2, 3}))
print(type({"name": "Ameenullah", "age": 20}))

# Find an Euclidean distance between (2, 3) and (10, 8)


x1, y1 = 2, 3
x2, y2 = 10, 8
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Euclidean distance between (2, 3) and (10, 8):", euclidean_distance)
