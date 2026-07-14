for num in range(0, 11):
    print(num)
print("Done!")

num = 0
while num <= 10:
    print(num)
    num += 1

for hash in range(1, 8):
    print("#" * hash)

sign = 1
while sign < 9:
    print("# " * 8)
    sign += 1

# another way to do the same thing
for row in range(8):
    for col in range(8):
        print("#", end=" ")
    print()

for row in range(11):
    product = row * row
    print(row, "*", row, "=", product)

list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in list:
    print(item)

for num in range(0, 101):
    if num % 2 == 0:
        print(f"{num} is even")
for num in range(0, 101):
    if num % 2 == 1:
        print(f"{num} is odd")

total = 0
for num in range(0, 101):
    total += num
    print(f"{num}, {total} so far")
print(f"The sum of all numbers from 0 to 100 is: {total}")

total = 0
for num in range(0, 101):
    if num % 2 == 0:
        total += num
print(f"The sum of all even numbers from 0 to 100 is: {total}")
total = 0
for num in range(0, 101):
    if num % 2 == 1:
        total += num
print(f"The sum of all odd numbers from 0 to 100 is: {total}")

# another way to do accumulator pattern
total_even = 0
total_odd = 0
for num in range(0, 101):
    if num % 2 ==0:
        total_even += num
    else:
        total_odd += num
print(f"The sum of all even numbers from 0 to 100 is: {total_even}")
print(f"The sum of all odd numbers from 0 to 100 is: {total_odd}")

# reverse a list using for loop
list = ['banana', 'orange', 'mango', 'lemon']
reversed_list = []

for fruit in list:
    reversed_list.insert(0, fruit)

print(reversed_list)
