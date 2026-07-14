#Select Operation and Calculate
select = input("Select operation from 1, 2, 3, 4 : ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if select == "1":
    operation= "+"
    result = num1 + num2
elif select == "2":
    operation = "-"
    result = num1 - num2
elif select == "3":
    operation = "*"
    result = num1 * num2
elif select == "4":
    operation = "/"
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"

print(num1, operation, num2, "=", result)