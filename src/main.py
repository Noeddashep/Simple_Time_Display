from src.countdown import user_interface
from src.date_information import table, world_clock_display


def main():
    print(table())
    user_input = input("What would you like to do?\n"
                       "Press 1 to select the time zone conversion\n"
                       "Press 2 to select the countdown\n"
                       "Press Enter to quit\n")
    while user_input:

        if user_input == "":
            break
        if user_input == "1":
            print(world_clock_display())
        if user_input == "2":
            print(user_interface())

        print(table())
        user_input = input("What would you like to do?\n"
                       "Press 1 to select the time zone conversion\n"
                       "Press 2 to select the countdown\n"
                       "Press Enter to quit\n")

if __name__ == '__main__':
    main()
