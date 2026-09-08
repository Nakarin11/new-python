student = {"name": "Alice", "age": 20, "grade": "A", "major": "Computer Science"}

for key in student:
    print(f"{key}: {student[key]}")  # Accessing values using keys
    #Output:
    # name: Alice
    # age: 20
    # grade: A
    # major: Computer Science

for value in student.values():
    print(value)  # Accessing values directly
    #Output:
    # Alice
    # 20
    # A
    # Computer Science

for key, value in student.items():
    print(f"{key}: {value}")  # Accessing both keys and values
    #Output:
    # name: Alice
    # age: 20
    # grade: A
    # major: Computer Science
