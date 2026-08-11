animal = ["cat", "dog", "rabbit", "hamster","dog", "parrot"]
first_dog_index = animal.index("dog")
print(f"The first occurrence of 'dog' is at index: {first_dog_index}")

second_dog_index = animal.index("dog", first_dog_index + 1)
print(f"The second occurrence of 'dog' is at index: {second_dog_index}")