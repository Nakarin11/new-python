set1 = {1, 2, 3}
set2 = {3, 4, 5}

#Union
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}

#Intersection
print(set1.intersection(set2))  # Output: {3}

#Difference
print(set1.difference(set2))  # Output: {1, 2}

#Symmetric Difference
print(set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}

union_set = set1 | set2

print("Union:", union_set)  # Output: {1, 2, 3, 4, 5}

intersection_set = set1 & set2
print("Intersection:", intersection_set)  # Output: {3}

difference_set = set1 - set2
print("Difference:", difference_set)  # Output: {1, 2}

symmetric_difference_set = set1 ^ set2
print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 4, 5}