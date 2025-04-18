"""
Grade Calculator App: Calculates grade based on 
inputted score(s).
"""

print("📊 GRADE CALCULATOR 📊")
total_scores = 0
score_count = 0
done = False

# Get test scores from user
while not done:
    score = input("Enter a test score (or 'done'): ")
    # Check for number score or done
    if score.isdigit():
        # Update score values
        total_scores += int(score)
        score_count += 1
        # Calculate average score
        avg_score = round(total_scores / score_count, 1)
        print(f"Average score: {avg_score}")
        # Calculate grade
        if avg_score >= 90:
            print("Grade: A")
        elif avg_score >= 80:
            print("Grade: B")
        elif avg_score >= 70:
            print("Grade: C")
        elif avg_score >= 60:
            print("Grade: D")
        else:
            print("Grade: F. You are failing!")
    else:
        done = True
print("Goodbye! 👋")

# ALTERNATIVE SOLUTION
# print("GRADE CALCULATOR")
# scores = []
# while True:
# score = input("Enter a test score (or 'done')")
# if score.lower() == "done":
# print("Goodbye!")
# break
# scores.append(float(score))
# average = sum(scores) / len(scores)
# print(f"Average score: {average:.1f}")
# if average >= 90:
# print("Grade: A")
# elif average >= 80:
# print("Grade: B")
# elif average >= 70:
# print("Grade: C")
# elif average >= 60:
# print("Grade: D")
# else:
# print("Grade: F")
