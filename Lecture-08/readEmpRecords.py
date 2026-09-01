with open("employees.txt", "r") as emp_file:
    line = emp_file.readline()
    while line != "":
        emp_id = line.strip()
        emp_name = emp_file.readline().strip()
        department = emp_file.readline().strip()
        print(f"Name: {emp_name}")
        print(f"ID: {emp_id}")
        print(f"Department: {department}")
        line = emp_file.readline()