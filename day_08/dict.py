# Creating an empty dictionary
dog = {}
'''
dog["name"] = "Buddy"
dog["color"] = "Brown"
dog["breed"] = "Labrador"
dog["age"] = 3
dog["legs"] = 4
print(dog)
'''
# A better way to add multiple key-value pairs to a dictionary is to use the update() method
dog.update({"name": "Buddy", "color": "Brown", "breed": "Labrador", "age": 3, "legs": 4})
print(dog)  # Displaying the dictionary after adding multiple key-value pairs

student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 20,
    "marital_status": "Single",
    "skills": ["Python", "JavaScript", "HTML", "CSS"],
    "country": "USA",
    "city": "New York",
    "address": "123 Main Street"
}
print(student)  # Displaying the student dictionary

print(len(student))  # Displaying the number of key-value pairs in the student dictionary
print(student["skills"])  # Displaying the skills of the student
print(type(student["skills"]))  # Displaying the type of the skills value

student["skills"].append("SQL")  # Adding more skills to the skills list
student["skills"].append("Git")
print(student["skills"])  # Displaying the updated skills of the student

print(student.keys())  # Displaying the keys of the student dictionary
print(student.values())  # Displaying the values of the student dictionary
print(student.items())  # Displaying the key-value pairs of the student dictionary 

student.pop("city")  # Removing the city key-value pair from the student dictionary
print(student)  # Displaying the student dictionary after removing the city key-value pair

del dog