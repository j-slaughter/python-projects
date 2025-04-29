# Countdown Timer App: A countdown timer
import time

print("=== ⏱️ COUNTDOWN TIMER ⏱️ ===")
print("✨ Count down from your chosen seconds! ✨")

while True:
    # Get number of seconds from user
    try:
        total = int(input("\nEnter seconds to countdown from: "))
    except ValueError:
        print("❌ Enter a valid number!")
        continue
    # Check for positive value
    if total <= 0:
        print("❌ Please enter a positive number.")
        continue
    # Start countdown
    print(f"⏳ Starting coundown from {total} seconds!")
    for i in range(total, 0, -1):
        print(f"⏰ {i} seconds remaining...")
        # Wait 1 second
        time.sleep(1)

    print("\n🎉 COUNTDOWN COMPLETE! 🎉")

    # Start again?
    start_again = input("\nStart another countdown? (yes/no): ").lower()
    if not start_again.startswith("y"):
        print("Thanks for using the countdown timer!")
        break
