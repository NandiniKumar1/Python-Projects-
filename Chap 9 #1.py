# Define dictionaries for course information
course_rooms = {
    "CS101": "3004",
    "CS102": "4501",
    "CS103": "6755",
    "NT110": "1244",
    "CM241": "1411"
}

course_instructors = {
    "CS101": "Haynes",
    "CS102": "Alvarado",
    "CS103": "Rich",
    "NT110": "Burke",
    "CM241": "Lee"
}

course_times = {
    "CS101": "8:00 a.m.",
    "CS102": "9:00 a.m.",
    "CS103": "10:00 a.m.",
    "NT110": "11:00 a.m.",
    "CM241": "1:00 p.m."
}

# Ask user for input
course_number = input("Enter a course number (e.g., CS101): ").strip().upper()

# Display course details if found
if course_number in course_rooms:
    print(f"Course: {course_number}")
    print(f"Room Number: {course_rooms[course_number]}")
    print(f"Instructor: {course_instructors[course_number]}")
    print(f"Meeting Time: {course_times[course_number]}")
else:
    print("That course number was not found.")
