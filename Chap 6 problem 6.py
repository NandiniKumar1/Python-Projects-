def calculate_average_from_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = []
            for line in file:
                line = line.strip()
                if line:  # Ignore empty lines
                    numbers.append(int(line))
            
            if numbers:
                average = sum(numbers) / len(numbers)
                print(f"The average is: {average}")
            else:
                print("The file is empty.")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except ValueError:
        print("Error: The file contains non-integer values.")

# Run the function with the assumed existing file
calculate_average_from_file('numbers.txt')
