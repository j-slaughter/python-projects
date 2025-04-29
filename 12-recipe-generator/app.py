"""
Recipe Generator App: Generates random recipes for the 
user, including a protein, veggie, and carb.
"""
import random

flavors = ["lemon", "herb", "garlic", "spicy", "sweet & sour", "curry"]
methods = ["baked", "roasted", "grilled", "stir-fried", "sauteed"]
proteins = ["tofu", "chicken", "beef", "fish", "eggs"]
veggies = ["spinach", "bell peppers", "broccoli", "carrots", "mushrooms"]
carbs = ["quinoa", "pasta", "rice", "potatoes", "bread"]

print("RANDOM RECIPE GENERATOR")

while True:
    # Get random recipe
    r_flavor = random.choice(flavors)
    r_method = random.choice(methods)
    r_protein = random.choice(proteins)
    r_veggie = random.choice(veggies)
    r_carb = random.choice(carbs)

    print(
        f"\nYour random recipe: {r_flavor} {r_method} {r_protein} with {r_veggie} and {r_carb}")

    answer = input("\nGenerate another recipe? (y/n): ").lower()
    # Check user answer to continue or not
    if not answer.startswith("y"):
        print("Goodbye!")
        break
