def convert_date(date_str):
    # Dictionary to map month numbers to month names
    months = {
        "01": "January", "02": "February", "03": "March",
        "04": "April", "05": "May", "06": "June",
        "07": "July", "08": "August", "09": "September",
        "10": "October", "11": "November", "12": "December"
    }

    try:
        parts = date_str.split("/")
        if len(parts) != 3:
            return "Invalid date format. Please enter mm/dd/yyyy."

        month, day, year = parts

        if month not in months:
            return "Invalid month entered."

        # Remove leading zeros from day for formatting
        day = str(int(day))

        return f"{months[month]} {day}, {year}"

    except Exception as e:
        return "Error processing date."

def main():
    date_input = input("Enter a date (mm/dd/yyyy): ")
    formatted_date = convert_date(date_input)
    print(formatted_date)

if __name__ == "__main__":
    main()
