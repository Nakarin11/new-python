numbers = [4, 2, 9, 1, 5, 6]

length = len(numbers)
print(f"Length of the list: {length}")

total_sum = sum(numbers)
print(f"Sum of the list: {total_sum}")

max_value = max(numbers)
print(f"Maximum value in the list: {max_value}")

min_value = min(numbers)
print(f"Minimum value in the list: {min_value}")

sorted_numbers = sorted(numbers)
print(f"Sorted list: {sorted_numbers}")

bool_list = [True, False, True, True]
any_true = any(bool_list)
print(f"Is any element True? {any_true}")

all_true = all(bool_list)
print(f"Are all elements True? {all_true}")

string = "hello"
char_list = list(string)
print(f"List of characters from string: {char_list}")

reversed_list = list(reversed(numbers))
print(f"Reversed list: {reversed_list}")

enumerated_list = list(enumerate(numbers))
print(f"Enumerated list: {enumerated_list}")
