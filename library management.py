from datetime import datetime

# Dictionary to store books
books = {
    "Python": True,
    "Math": True,
    "Science": True
}

# Issued book records
issued_books = {}

# -------- Add Book --------
def add_book():
    name = input(" Enter book name: ").title()
    if name in books:
        print(" Book already exists.")
    else:
        books[name] = True
        print(f" '{name}' added successfully.")


# -------- Show Books --------
def show_books():
    print("\n Available Books:")
    available = False
    for book, status in books.items():
        if status:
            print(f" {book}")
            available = True

    if not available:
        print(" No books available.")


# -------- Issue Book --------
def issue_book():
    show_books()
    print("-" * 30)

    name = input(" Enter book name to issue: ").title()

    if name in books and books[name]:
        student = input(" Enter student name: ").title()
        days = int(input(" Enter number of days: "))

        issue_date = datetime.now()

        issued_books[name] = {
            "student": student,
            "days": days,
            "issue_date": issue_date
        }

        books[name] = False

        print(f"\n Book issued successfully to {student}")
        print(f" Return within {days} days to avoid fine.")

    else:
        print(" Book not available.")


# -------- Fine Calculation --------
def calculate_fine(extra_days):
    fine = 0

    for day in range(1, extra_days + 1):
        if day <= 7:
            fine += 10
        elif day <= 14:
            fine += 20
        else:
            fine += 60

    return fine


# -------- Return Book --------
def return_book():
    name = input(" Enter book name to return: ").title()

    if name in issued_books:
        record = issued_books[name]
        return_date = datetime.now()

        days_used = (return_date - record["issue_date"]).days
        allowed_days = record["days"]

        print(f"\n Days Used: {days_used}")
        print(f" Allowed Days: {allowed_days}")

        if days_used > allowed_days:
            extra_days = days_used - allowed_days
            fine = calculate_fine(extra_days)

            print(f" Late by {extra_days} days")
            print(f" Fine to pay: ₹{fine}")
        else:
            print(" Book returned on time. No fine.")

        books[name] = True
        del issued_books[name]

        print(f" '{name}' returned successfully.")

    else:
        print(" Record not found.")


# -------- Main Menu --------
def library():
    while True:
        print("\n" + "=" * 40)
        print(" LIBRARY MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Add Book")
        print("2. Show Available Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        print("=" * 40)

        try:
            choice = int(input(" Enter your choice: "))
        except ValueError:
            print(" Please enter a valid number.")
            continue

        if choice == 1:
            add_book()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print(" Thank you for using the system!")
            break
        else:
            print(" Invalid choice. Try again.")


# Run Program
library()