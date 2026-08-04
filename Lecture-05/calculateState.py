def calculate_state(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total_sum, average, maximum, minimum

#Example usage
numbers = [5, 10, 15, 20, 25]
total, avg, max_value, min_value = calculate_state(numbers)
print(f"Total Sum: {total}")
print(f"Average: {avg}")
print(f"Maximum Value: {max_value}")
print(f"Minimum Value: {min_value}")