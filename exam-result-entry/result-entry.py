# Constants
QUIT = 999       # Sentinel value to stop entering marks
MIN = 0          # Minimum valid mark
MAX = 100        # Maximum valid mark

def read_marks():
    """
    Continuously prompts the teacher to enter student marks.
    - Only accepts numbers between MIN and MAX.
    - Allows the teacher to quit by entering QUIT.
    Returns:
        total (float): Sum of all valid marks
        count (int): Number of valid marks entered
    """
    total = 0.0
    count = 0

    while True:
        try:
            # Prompt user for a mark and convert it to float
            mark = float(input("Please enter exam marks: "))
        except ValueError:
            # Handle invalid input (not a number)
            print("Not a number, please enter a valid mark.")
            continue

        # Check if user wants to quit
        if mark == QUIT:
            break

        # Check if the mark is within valid range
        if mark < MIN or mark > MAX:
            print("ERROR: grade must be between 0 and 100")
            continue

        # Add valid mark to total and increment count
        total += mark
        count += 1

    return total, count


def class_average(total, count):
    """
    Calculates and prints the class average based on total marks and count.
    Args:
        total (float): Sum of valid marks
        count (int): Number of valid marks
    Returns:
        average (float or None): Average mark, or None if no valid marks entered
    """
    if count == 0:
        # No valid marks entered
        print("No results entered")
        return None
    else:
        # Calculate average
        average = total / count
        # Print formatted average
        print(f"Average mark for {count} students is: {average:.1f}")
        return average


def main():
    """
    Main program flow:
    - Reads marks from the user
    - Calculates and prints the class average
    """
    total, count = read_marks()
    average = class_average(total, count)


if __name__ == "__main__":
    main()
