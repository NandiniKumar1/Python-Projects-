def determine_age_group(age):
    if age == 1:
        return "infant"
    elif 1 < age < 13:
        return "child"
    elif 13 <= age < 20:
        return "teenager"
    elif age >= 20:
        return "adult"
    else:
        return "invalid age"

def main():
    # Ask the user to enter age
    age_input = input("Enter the person's age (in years): ")
    try:
        age = int(age_input)
        if age < 0:
            print("Age cannot be negative.")
            return
        group = determine_age_group(age)
        print(f"The person is a(n) {group}.")
    except ValueError:
        print("Please enter a valid integer for age.")

if __name__ == "__main__":
    main()

    # Testing all 4 age groups:
    test_ages = [1, 5, 15, 25]
    print("\nTesting age groups:")
    for test_age in test_ages:
        print(f"Age {test_age}: {determine_age_group(test_age)}")
