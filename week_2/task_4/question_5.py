# Student Score Tracker
student_names = []
student_scores = []
for i in range(3):
    name = input(f"Enter name of student {i+1}:")
    score = input(f"Enter your score for {name}:")
    student_names.append(name)
    student_scores.append(score)
    print("\nName\t\tScore")
    print("-" * 20)
for i in range (3):
    print(f"{student_names[i]:<10} {student_scores[i]}")