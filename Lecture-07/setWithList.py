# Attendance record for a week (each list represents a day's attendance)
attendance_week = [
    ["Alice", "Bob", "Charlie", "David"], #Day 1
    ["Alice", "Charlie", "David"], #Day 2
    ["Alice", "Bob", "David"], #Day 3
    ["Alice", "David", "Eve"], #Day 4
    ["Bob", "Charlie", "David"], #Day 5
]

# 1. Find the set of students who were present every day (intersection of all sets)
# 2. Determine the set of students who were absent at least one day (union of all sets)
# 3. Create a list of students who were present on the first day but absent on the last day (difference between first and last day's sets)
# 4. Calculate the total number of unique students who attended at least one day (length of the union set) 

# Convert each day's attendance list to a set
attendance_sets = [set(day) for day in attendance_week]
print(attendance_sets)

# 1. Find the set of students who were present every day (intersection of all sets)
present_every_day = set.intersection(*attendance_sets)
print("Students present every day:", present_every_day)
#Output: Students present every day: {'David'}

# 2. Determine the set of students who were absent at least one day (union of all sets)
all_students = set.union(*attendance_sets)
absent_at_least_one_day = all_students - present_every_day
print("Students absent at least one day:", absent_at_least_one_day)
#Output: Students absent at least one day: {'Bob', 'Charlie', 'Eve', 'Alice'}

# 3. Create a list of students who were present on the first day but absent on the last day (difference between first and last day's sets)
first_day_present = attendance_sets[0]
last_day_present = attendance_sets[-1]
first_day_but_not_last = first_day_present - last_day_present
print("Students present on the first day but absent on the last day:", first_day_but_not_last)
#Output: Students present on the first day but absent on the last day: {'Alice'}

# 4. Calculate the total number of unique students who attended at least one day (length of the union set)
total_unique_students = len(all_students)
print("Total number of unique students who attended at least one day:", total_unique_students)
#Output: Total number of unique students who attended at least one day: 5