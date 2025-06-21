def main():
    try:
        speed_input = input("Enter the speed of the vehicle in mph: ")
        hours_input = input("Enter the number of hours traveled: ")

        speed = float(speed_input)
        hours = int(hours_input)

        if speed < 0 or hours <= 0:
            print("Speed must be non-negative and hours must be a positive integer.")
            return

        print("\nHour\tDistance Traveled (miles)")
        print("-" * 35)

        for hour in range(1, hours + 1):
            distance = speed * hour
            print(f"{hour}\t{distance:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for speed and hours.")

if __name__ == "__main__":
    main()
