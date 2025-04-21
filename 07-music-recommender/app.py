"""
Music Recommender App: recommends a musical artist based
on the selected music genre.
"""
import random

print("🎶 MUSIC RECOMMENDER 🎶")

# Store artists in dictionary
genres = {
    "rock": ["AC/DC", "Queen", "Led Zeppelin"],
    "pop": ["Ed Sheeran", "Ariana Grande", "Lady Gaga"],
    "hip-hop": ["Kendrick Lamar", "Snoop Dogg", "J.Cole"],
}

# Get user input
genre_choice = input("What genre do you like? (rock/pop/hip-hop): ").lower()

# Return recommendations
if genre_choice not in genres:
    print("Sorry, I don't know that genre.")
else:
    print(f"Check out {random.choice(genres[genre_choice])}!")
