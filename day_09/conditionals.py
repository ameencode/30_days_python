user = int(input("Please enter your age: "))
if user >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You are too young to learn to drive. You need to wait {18 - user} more years.") 

# Shorthand if statement
print("You are old enough to learn to drive.") if user >= 18 else print(f"You are too young to learn to drive. You need to wait {18 - user} more years.")
if user >= 18: print("You are old enough to learn to drive.")

# age comparison
my_age = 20
your_age = int(input("Please enter your age: "))
if your_age > my_age:
    if your_age - my_age == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {your_age - my_age} years older than me.")
elif your_age < my_age:
    if my_age - your_age == 1:
        print("You are 1 year younger than me.")
    else:
        print(f"You are {my_age - your_age} years younger than me.")        
else:
    print("We are the same age.")

num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter another number: "))
if num_1 > num_2:
    print(f"{num_1} is greater than {num_2}.")
elif num_2 > num_1:
    print(f"{num_2} is greater than {num_1}.")
else:
    print(f"{num_1} and {num_2} are equal.")

score = int(input("Please enter your score: "))   
if score >= 90 and score <= 100:
    print("Your grade is A.")
elif score >= 80 and score < 90:
    print("Your grade is B.")
elif score >= 70 and score < 80:
    print("Your grade is C.")
elif score >= 60 and score < 70:
    print("Your grade is D.")
else:
    print("Your grade is F.")

month = input("Please enter the month: ").lower()
if month in ["september", "october", "november"]:
    print("The season is Autumn.")
elif month in ["december", "january", "february"]:
    print("The season is Winter.")
elif month in ["march", "april", "may"]:
    print("The season is Spring.")
elif month in ["june", "july", "august"]:
    print("The season is Summer.")
else:
    print("Please enter a valid month.")

fruits = ['banana', 'orange', 'mango', 'lemon']
added_fruit = input("Please enter a fruit to add: ").lower()
if added_fruit in fruits:
    print(f"{added_fruit} is already in the list.")
else:
    fruits.append(added_fruit)
    print(f"{added_fruit} has been added to the list.")
    print("Updated fruit list:", fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    },
    'city': 'Helsinki'
    }

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    },
    'city': 'Helsinki'
    }
if 'skills' in person:
    print(person['skills'][len(person['skills']) // 2])
else:
    print("Not found.")
if 'skills' in person and 'Python' in person['skills']:
    print("Python is present in the skills.")
if 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print("He is a front end developer.")
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print("He is a backend developer.")
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print("He is a fullstack developer.")
else:
    print("unknown title")

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")