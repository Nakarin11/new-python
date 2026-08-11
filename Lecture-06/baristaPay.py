NUM_EMPLOYEES = 6

def main():
    hour = [0] * NUM_EMPLOYEES
    for index in range(NUM_EMPLOYEES):
        print('Enter the hours worked by employee ', index + 1, ': ', sep='', end='')
        hour[index] = float(input())

    payrate = float(input('Enter the hourly pay rate: '))
    for index in range(NUM_EMPLOYEES):
        grosspay = hour[index] * payrate
        print('Gross pay for employee ', index + 1, ': $', format(grosspay, ',.2f'), sep='')
main()