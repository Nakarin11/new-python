score1 = input("Enter the first score: ")
score2 = input("Enter the second score: ")
score3 = input("Enter the third score: ")
total_score = int(score1) + int(score2) + int(score3)
average_score = total_score / 3
print("Your average score is:", average_score)
if average_score > 95:
    print("Congratulations!")