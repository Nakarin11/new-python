counter = 0

def increment():
    global counter
    counter += 1

#Call the increment function twice
increment()
increment()

#Access the modified global variable
print(counter)  # Output: 2