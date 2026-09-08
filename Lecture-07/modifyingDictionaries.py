student = {"name": "Alice", "age": 25, "grade": "A"}

student["age"] = 26  # Modifying the age
student["major"] = "Computer Science"  # Adding a new key-value pair
print(student)  # Output: {'name': 'Alice', 'age': 26, 'grade': 'A', 'major': 'Computer Science'}

del student["grade"]  # Deleting the grade key-value pair
print(student)  # Output: {'name': 'Alice', 'age': 26,

remove_major = student.pop("major")  # Removing and returning the value of the major key
print(remove_major)  # Output: Computer Science
print(student)  # Output: {'name': 'Alice', 'age': 26}