import struct


num_record = int(input("Enter the number of records do you want to create? "))
with open('records.bin', 'wb') as file:
    for i in range(num_record):
        id_num = int(input("Enter ID number: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        gpa = float(input("Enter GPA: "))
        data = struct.pack('i20sif', id_num, name.encode('utf-8'), age, gpa)
        file.write(data)

print(f"{num_record} records have been written to 'records.bin'.")