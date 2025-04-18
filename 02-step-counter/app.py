"""
Step Counter App: Tracks your step goal
"""

print("🏃 STEP COUNTER 🏃")
# Get user's step goal
goal = int(input("What is your daily step goal? "))
# Get amount of steps already performed
steps_taken = int(input("✨ How many steps have you taken today? "))
# Calculate amount of steps til step goal
steps_remaining = goal - steps_taken

if steps_remaining > 0:
    print(f"💪 You need {steps_remaining} more steps to reach your goal!")
else:
    print(
        f"🎉 Congratulations! You've exceeded your goal by {-steps_remaining} steps!")
