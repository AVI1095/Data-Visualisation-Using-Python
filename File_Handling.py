# File handling program for student records
from datetime import datetime
def writer():
    try:
        name = input('Enter name: ')
        if not name.isalpha():
            print('Enter a valid name.')
            return
        roll_no = input('Enter roll no: ')
        if not roll_no.isdigit():
            print('Enter a valid roll no.')
            return
        dob = input('Enter date of birth (dd-mm-yyyy): ')
        try:
            datetime.strptime(dob, '%d-%m-%Y')
        except ValueError:
            print("Invalid date format! Please enter as dd-mm-yyyy.")
            return
        record = f"{name},{roll_no},{dob}\n"
        with open("student.txt", "a") as file:
            file.write(record)
        print("Record added successfully.")
    except Exception as e:
        print(f"Error while writing record: {e}")

def reader():
    print("Name\t\tRoll no\t\tDate of Birth")

    with open("student.txt", "r") as file:
        for line in file:
            Splitted = line.strip().split(",")
            name = Splitted[0].strip()
            roll_no = Splitted[1].strip()
            dob = Splitted[2].strip()
            print(f"{name}\t\t\t{roll_no}\t\t\t{dob}")

def age():
    user_inp = input("roll no of student: ")
    found = False

    with open("student.txt", "r") as file:
        for line in file:
            Splitted = line.strip().split(",")
            name = Splitted[0].strip()
            roll_no = Splitted[1].strip()
            dob = Splitted[2].strip()

            if user_inp == roll_no:
                dob_to_calc = datetime.strptime(dob, '%d-%m-%Y')
                today = datetime.today()

                age = today.year - dob_to_calc.year - ((today.month, today.day) < (dob_to_calc.month, dob_to_calc.day))

                print(f"{name}'s age is: {age} years old.")
                found = True
                break

    if not found:
        print(f"Roll number {user_inp} not found in the database.")

    print("-" * 20)


while True:
    print("\n--- Main Menu ---")
    print("1. Add new student record")
    print("2. View all records")
    print("3. Calculate student's age")
    print("4. Exit")

    ch = int(input('Enter your choice (1-4): '))

    if ch == 1:
        num = int(input("How many records would you like to enter? "))
        for i in range(num):
            print(f"\nrecord :{i + 1}")
            writer()
    elif ch == 2:
        reader()
    elif ch == 3:
        age()
    elif ch == 4:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")