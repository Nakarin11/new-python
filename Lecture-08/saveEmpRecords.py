num_emps = int(input("How many employee records do you want to create? : "))
with open("employees.txt", "w") as emp_file:
    for count in range(1, num_emps + 1):
        print(f"Enter the data for employee #{count}:")
        emp_id = input("Employee ID: ")
        emp_name = input("Employee Name: ")
        department = input("Department: ")
        emp_file.write(emp_id + "\n")
        emp_file.write(emp_name + "\n")
        emp_file.write(department + "\n")
        print()

print("Employee records saved to employees.txt successfully.")