columns = int(input("How many columns? "))

for i in range(1, 101):
    print(f"*", end="")
    if i % columns == 0:
        print()