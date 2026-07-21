keep_going = 'y'
while keep_going == 'y':
    wholesale = float(input("Enter the wholesale cost: "))
    retail = wholesale * 2.5
    print(f'The retail price is: {retail:.2f}')
    keep_going = input("Do you have another item? (y/n): ")