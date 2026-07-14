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

