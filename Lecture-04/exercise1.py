#Convert KPH to MPH
print("-------------------")
print("KPH\tMPH")
print("-------------------")
for kph in range(60, 131, 10):
    mph = kph * 0.6214
    print(f"{kph}\t{mph:.2f}")
print("-------------------")

#Convert MPH to KPH
print("-------------------")
print("MPH\tKPH")
print("-------------------")
for mph in range(60, 131, 10):
    kph = mph / 0.6214
    print(f"{mph}\t{kph:.2f}")
print("-------------------")