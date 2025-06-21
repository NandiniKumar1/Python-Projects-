def mix_colors(color1, color2):
    # Normalize inputs to lowercase for easy comparison
    color1 = color1.lower()
    color2 = color2.lower()

    primary_colors = {"red", "blue", "yellow"}

    # Check if inputs are valid primary colors
    if color1 not in primary_colors or color2 not in primary_colors:
        return "Error: Invalid color entered. Please enter red, blue, or yellow."

    # If both colors are the same
    if color1 == color2:
        return f"Mixing {color1} and {color2} results in {color1}."

    # Determine the secondary color
    mix = {color1, color2}
    if mix == {"red", "blue"}:
        return "Purple"
    elif mix == {"red", "yellow"}:
        return "Orange"
    elif mix == {"blue", "yellow"}:
        return "Green"
    else:
        return "Error: Unexpected input."

def main():
    color1 = input("Enter the first primary color (red, blue, or yellow): ")
    color2 = input("Enter the second primary color (red, blue, or yellow): ")

    result = mix_colors(color1, color2)
    print(result)

if __name__ == "__main__":
    main()
