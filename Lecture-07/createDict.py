student = {"name": "Alice", "age": 25, "grade": "A", "major": "Computer Science"}
print(student)  # Output: {'name': 'Alice', 'age': 25, 'grade': 'A', 'major': 'Computer Science'}

student = dict(name="Alice", age=25, grade="A", major="Computer Science")
print(student)  # Output: {'name': 'Alice', 'age': 25, 'grade': 'A', 'major': 'Computer Science'}

student = dict([("name", "Alice"), ("age", 25), ("grade", "A"), ("major", "Computer Science")])
print(student)  # Output: {'name': 'Alice', 'age': 25, 'grade': 'A', 'major': 'Computer Science'}

student = {}
student["name"] = "Alice"
student["age"] = 25
student["grade"] = "A"
student["major"] = "Computer Science"
print(student)  # Output: {'name': 'Alice', 'age': 25, 'grade': 'A', 'major': 'Computer Science'}

student = {"name": "Alice", "age": 25, "grade": "A", "major": "Computer Science"}
print(student["name"])  # Output: Alice
print(student["age"])  # Output: 25
print(student["grade"])  # Output: A
print(student["major"])  # Output: Computer Science

