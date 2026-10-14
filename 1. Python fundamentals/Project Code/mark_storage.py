#tuple
marks = (85, 92, 78, 90, 67, 92, 88)

while True:

    print("\n========== STUDENT MARKS REPORT ==========")
    print("1. View All Marks")
    print("2. Total Marks")
    print("3. Average Marks")
    print("4. Highest Mark")
    print("5. Lowest Mark")
    print("6. Search a Mark")
    print("7. Count a Mark")
    print("8. Find Position of a Mark")
    print("9. Display Marks in Sorted Order")
    print("10. Display First 3 Marks")
    print("11. Display Last 3 Marks")
    print("12. Exit")

    choice = input("\nEnter your choice: ")

    # View All Marks
    if choice == "1":

        print("\nStudent Marks:")

        for i in range(len(marks)):
            print(f"Subject {i + 1}: {marks[i]}")

    # Total Marks
    elif choice == "2":

        print(f"\nTotal Marks = {sum(marks)}")

    # Average Marks
    elif choice == "3":

        average = sum(marks) / len(marks)

        print(f"\nAverage Marks = {average:.2f}")

    # Highest Mark
    elif choice == "4":

        print(f"\nHighest Mark = {max(marks)}")

    # Lowest Mark
    elif choice == "5":

        print(f"\nLowest Mark = {min(marks)}")

    # Search a Mark
    elif choice == "6":

        mark = int(input("Enter mark to search: "))

        if mark in marks:
            print(f"{mark} is found.")
        else:
            print(f"{mark} is not found.")

    # Count a Mark
    elif choice == "7":

        mark = int(input("Enter mark: "))

        print(f"{mark} appears {marks.count(mark)} time(s).")

    # Find Position
    elif choice == "8":

        mark = int(input("Enter mark: "))

        if mark in marks:

            position = marks.index(mark)

            print(f"{mark} found at Subject {position + 1}")

        else:

            print("Mark not found.")

    # Sorted Marks
    elif choice == "9":

        sorted_marks = sorted(marks)

        print("\nMarks in Ascending Order:")

        for mark in sorted_marks:
            print(mark)

    # First 3 Marks
    elif choice == "10":

        print("\nFirst 3 Marks:")

        how_many_marks_to_see = int(input())

        for mark in marks[:3]:
            print(mark)

    # Last 3 Marks
    elif choice == "11":

        print("\nLast 3 Marks:")

        for mark in marks[-3:]:
            print(mark)

    # Exit
    elif choice == "12":

        print("\nThank you!")

        break

    else:

        print("\nInvalid Choice!")