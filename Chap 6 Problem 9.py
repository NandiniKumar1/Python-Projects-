def calculate_average_from_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = []
            for line in file:
                line = line.strip()
                if line:  # skip empty lines
                    try:
                        number = int(line)
                        numbers.append(number)
                    except ValueError:
                        print(f"Warning: Skipping invalid value '{line}'")

            if numbers:
                average = sum(numbers) / len(numbers)
                print(f"The average is: {average}")
            else:
                print("No valid integers found in the file.")

    except IOError:
        print(f"Error: Could not open or read from file '{filename}'.")

# Run the function
calculate_average_from_file('numbers.txt')
