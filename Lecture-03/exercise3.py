hoursWork = int(input("Enter hours worked: "))
payRate = float(input("Enter pay rate: "))
if hoursWork <= 40:
    grossPay = hoursWork * payRate
else:
    grossPay = 40 * payRate + (hoursWork - 40) * payRate * 1.5

print(f"The gross pay is: ${grossPay:.2f}")