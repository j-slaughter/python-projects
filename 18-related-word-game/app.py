"""
Word Association Game App: Tests how quickly users can come 
up with a related word to the given prompt word. Scores points 
based on the speed in seconds.
"""
import random
import time

# word pairs => (prompt: related words)
word_pairs = {
    "sky": ["blue", "cloud", "bird", "fly", "sun", "moon"],
    "water": ["drink", "ocean", "swim", "fish", "boat", "wet"],
    "food": ["eat", "cook", "tasty", "meal", "restaurant", "kitchen"],
    "music": ["song", "dance", "listen", "band", "rhythm", "play"],
    "book": ["read", "story", "page", "author", "library", "character"],
    "tree": ["leaf", "green", "forest", "wood", "shade", "tall"],
    "car": ["drive", "road", "wheel", "travel", "speed", "fast"],
    "dog": ["pet", "bark", "walk", "loyal", "puppy", "fur"],
}

print("=== WORD ASSOCIATION GAME ===")
print("✨ Respond with a related word quickly! ✨")

score = 0
rounds = 0

# Start game
while True:
    # Select a random prompt word
    prompt = random.choice(list(word_pairs.keys()))
    related_words = word_pairs[prompt]
    print(f"\n🔤 Prompt word: {prompt.upper()}")
    print("Quick! Type a word related to this prompt!")

    # Time the player's response
    start_time = time.time()
    # strip() removes leading and trailing whitespace
    response = input("> ").lower().strip()
    response_time = time.time() - start_time
    # example output: 2.46475887298584 (in secs)
    print("response time", response_time)

    # Check if response is related
    if response in related_words:
        points = max(1, 5 - int(response_time))
        score += points
        print(
            f"✅ Good association! +{points} points (answered in {response_time:.1f}s)")
    else:
        print(
            f"❌ Not a common association. Related words included: {', '.join(related_words)}")

    # Print total score
    rounds += 1
    print(f"Score: {score}/{rounds * 5} possible points")

    # Ask to play again
    if not input("\n🔄 Play again? (yes/no): ").lower().startswith("y"):
        print(f"Final score: {score}. Thanks for playing! 👋")
        break
