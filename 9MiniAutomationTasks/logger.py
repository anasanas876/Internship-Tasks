from datetime import datetime
import logging

# Configure logging only once
logging.basicConfig(
    filename="program.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def manual_logger():
    print(f"Program started at {datetime.now()}")

    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    print(f"User entered two numbers at {datetime.now()}")

    result = number1 * number2

    print(f"The result is stored at {datetime.now()}")
    print(f"Program ended successfully at {datetime.now()}")

    return result


def logging_logger():
    number1 = int(input("Enter 1st Number: "))
    logging.info("User entered first number")

    number2 = int(input("Enter 2nd Number: "))
    logging.info("User entered second number")

    result = number1 * number2
    logging.info(f"Result = {result}")
    logging.info("Program ended successfully")

    print("Result =", result)


def view_logs():
    try:
        with open("program.log", "r") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print("No log file found.")


if __name__ == "__main__":
    print("Testing logger module")
    logging_logger()
    view_logs()