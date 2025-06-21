# number_analysis.py

def main():
    numbers = []

    print("Please enter 20 numbers:")

    for i in range(1, 21):
        while True:
            try:
                num = float(input(f"Number {i}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    print("\nAnalysis of the numbers entered:")
    print(f"Lowest number: {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total of numbers: {total}")
    print(f"Average of numbers: {average}")

if __name__ == "__main__":
    main()
