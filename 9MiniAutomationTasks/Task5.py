# Task 5
from organizer import organize_files
from logger import view_logs
from monitor import file_monitoring
from reminder import start_timer

while True:
    print("\n===== FILE AUTOMATION TOOL =====")
    print("1. Organize Files")
    print("2. View Logs")
    print("3. Monitor Files")
    print("4. Start Reminder")
    print("5. Exit")

    try:
        user = int(input("Enter a number for the corresponding action: "))

        if user == 1:
            organize_files()

        elif user == 2:
            view_logs()

        elif user == 3:
            file_monitoring()

        elif user == 4:
            start_timer()

        elif user == 5:
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    except ValueError:
        print("Please enter a valid number.")