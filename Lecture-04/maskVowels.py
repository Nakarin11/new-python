input_string = input("Enter a string: ")
modified_string = ""
vowels = "aeiouAEIOU"

for char in input_string:
    upperchar = char.upper()
    if upperchar in vowels:
        modified_string += "*"
    else:
        modified_string += upperchar

print("Modified string:", modified_string)