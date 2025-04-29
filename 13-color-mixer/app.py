"""
Color Mixer App: Returns the color created from two 
inputted colors.
"""

print("🎨 COLOR MIXER 🎨")

# Use tuples to store color mixes
color_mixes = {
    ("red", "blue"): "purple",
    ("red", "yellow"): "orange",
    ("blue", "yellow"): "green",
    ("blue", "green"): "teal",
    ("white", "red"): "pink",
    ("red", "green"): "brown",
}

while True:
    # Get colors in lowercase with no leading/trailing whitespaces
    first_color = input("\nEnter first color: ").lower().strip()
    second_color = input("Enter second color: ").lower().strip()

    # keyword None: used to define a null value, data type is NoneType, None = None, neither True or False
    mixed_color = None

    # Find colors in mixes
    if (first_color, second_color) in color_mixes:
        mixed_color = color_mixes[(first_color, second_color)]
    elif (second_color, first_color) in color_mixes:
        mixed_color = color_mixes[(second_color, first_color)]

    # Return result
    if mixed_color:
        print(
            f"When you mix {first_color} and {second_color}, you get {mixed_color}!")
    else:
        print("I don't know what those colors make when mixed.")

    # Check if user wants to continue
    answer = input("\nMix more colors? (y/n): ").lower()
    if not answer.startswith("y"):
        print("Goodbye!")
        break
