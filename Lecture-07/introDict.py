phonebook = {'Nakarin': '081-234-5678', 'John': '082-345-6789', 'Jane': '083-456-7890'}
print(phonebook)

print(phonebook['John'])  # Accessing John's phone number
print(phonebook.get('Jane'))  # Accessing Jane's phone number using get method

key = 'Pluto'
if key in phonebook:
    print(phonebook[key])
else:
    print(key + " is not found in the phonebook.")  # Handling the case where the key is not found

phonebook['Simpson'] = '084-567-8901'  # Adding a new entry
phonebook['Pluto'] = '082-999-9999'  # Modifying Pluto's phone number
phonebook.pop('John')  # Removing John's entry
print(phonebook)  # Output: {'Nakarin': '081-234-5678', 'Pluto': '082-999-9999', 'Simpson': '084-567-8901'}

del phonebook['Simpson']  # Deleting Simpson's entry
print(phonebook)  # Output: {'Nakarin': '081-234-5678', 'Pluto': '082-999-9999'}