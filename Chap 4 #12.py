def main():
    try:
        # Get user inputs
        start_input = input("Enter the starting number of organisms: ")
        increase_input = input("Enter the average daily increase (as a percentage): ")
        days_input = input("Enter the number of days the organisms will multiply: ")

        # Convert inputs to appropriate types
        start = float(start_input)
        increase_percent = float(increase_input)
        days = int(days_input)

        # Input validation
        if start < 1 or increase_percent < 0 or days < 1:
            print("Error: Starting organisms must be at least 1, increase must be non-negative, and days must be at least 1.")
            return

        # Convert percentage to decimal
        increase_rate = increase_percent / 100

        # Print header
        print("\nDay\tPopulation")
        print("-" * 20)

        # Loop through each day and calculate population
        population = start
        for day in range(1, days + 1):
            print(f"{day}\t{population:.5g}")
            population += population * increase_rate

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
