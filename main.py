from src.countdown import user_interface
from src.date_information import table, world_clock_display


def main():
    """
    Main function, prints a table that contains the current time and other date information.
    Calls several functions, allowing the user to use the countdown or compare different time zones
    """

    print(table([]))

    while True:

        user_input = input("\nWhat would you like to do?\n"
                           "Press 1 to select the time zone conversion\n"
                           "Press 2 to select the countdown\n"
                           "Press Enter to quit\n")

        if user_input not in ("1", "2", ""):
            print(f"{user_input} not found")

        if user_input == "":
            print("You closed the program!")
            break

        if user_input == "1":
            print(world_clock_display())

        if user_input == "2":
            print(user_interface())

        continue


if __name__ == '__main__':
    main()
