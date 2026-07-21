import random

print("What is my magic number (1 to 100 ?")
mynumber = random.randint(1, 100)
ntries = 1
your_guess = -1
while ntries <= 7 and your_guess != mynumber:
    msg = str(ntries) + ">> "
    if (ntries == 6) :
        print("Your last chance")
    your_guess = int(input(msg))
    if your_guess > mynumber :
        print("--> too high")
    else:
        print("--> too low")
    ntries +=1

if your_guess == mynumber :
    print("Yes! its", mynumber)
else:
    print("Sorry! my number is", mynumber)