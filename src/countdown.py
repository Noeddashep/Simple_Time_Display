import threading
import time
from typing import List


def countdown(user_seconds: int, time_units: List[str]) -> None:
    """
    Using a while loop allows to display the countdown on the screen based on the duration of time as seconds and the
    time units obtained as arguments.

    param user_seconds: the duration of time as seconds

    param time_units: a list containing the time units as string
    """

    global total_seconds, running
    total_seconds = user_seconds

    while total_seconds >= 0:
        timer = ""
        if not running:
            break

        days = total_seconds // 86400
        hours = (total_seconds // 3600) % 24
        minutes = (total_seconds // 60) % 60
        seconds = total_seconds % 60

        if 'days' in time_units:

            if days < 10:
                timer += f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}"
            else:
                timer += f"{days}:{hours:02}:{minutes:02}:{seconds:02}"

        if "hours" in time_units:

            if len(timer) < 1:
                hours = total_seconds // 3600
                if hours < 10:
                    timer += f"{hours:02}:{minutes:02}:{seconds:02}"
                else:
                    timer += f"{hours:02}:{minutes:02}:{seconds:02}"

        if "minutes" in time_units:

            if len(timer) < 1:
                minutes = total_seconds // 60
                if minutes < 10:
                    timer += f"{minutes:02}:{seconds:02}"
                else:
                    timer += f"{minutes}:{seconds:02}"

        if "seconds" in time_units:

            if len(timer) < 1:
                seconds = total_seconds
                if seconds < 10:
                    timer += f"{seconds:02}"
                else:
                    timer += f"{seconds}"

        print(timer)
        time.sleep(1)
        total_seconds -= 1


def start(seconds: int, time_units: List[str]) -> None:
    """
    Make the running variable as True allows to start the countdown as a separate running flow
    param seconds: the duration of time as seconds
    param time_units: a list containing the time units as string
    """

    global running
    running = True
    threat_start = threading.Thread(target=countdown, args=(seconds, time_units,))
    threat_start.start()


def stop() -> None:
    """
    Make the running variable as False allows to stop the countdown
    """

    global running
    running = False


def user_seconds() -> int:
    """
    Asks the user the duration of time
    return: the duration of time as integer
    """

    total_seconds = input("Enter the time to include in your countdown in seconds:\n")
    while total_seconds:

        try:
            total_seconds = int(total_seconds)

            if total_seconds > 0:
                break

            else:
                print('You must enter a value greater than zero!')
                total_seconds = input("Enter the time to include in your countdown in seconds:\n")

        except ValueError:
            print('Only integers are accepted!')
            total_seconds = input("Enter the time to include in your countdown in seconds:\n")

    return total_seconds


def user_interface() -> None:
    """
    the function allows to interact with the user by allowing him to start the countdown, stop it, restart it and
    exit to the program
    """

    global running, total_seconds
    running = False
    total_seconds = user_seconds()
    time_unit = time_units()
    print("Press s to start the countdown, then press Enter if you want to stop it.")

    while True:
        user_input = input()

        while user_input.lower() not in ("r", "", "s", "q"):
            print("Press:\n"
                  "- r if you want to reset countdown;\n"
                  "- s to start the countdown, then press Enter if you want to stop it;\n"
                  "- q to exit the program")
            user_input = input()

        if user_input.lower() == 's':

            if not running:
                start(total_seconds, time_unit)
            else:
                print("The countdown has already started")

        if user_input == "":

            if running:
                stop()
                print("Paused")
                print("Press:\n"
                      "- r if you want to reset countdown;\n"
                      "- s to start the countdown, then press Enter if you want to stop it;\n"
                      "- q to exit the program")

            else:
                print("Press:\n"
                      "- r if you want to reset countdown;\n"
                      "- s to start the countdown, then press Enter if you want to stop it;\n"
                      "- q to exit the program")

        if user_input.lower() == "r":
            total_seconds = user_seconds()
            time_unit = time_units()
            print("Press s to start the countdown, then press Enter if you want to stop it")

        if user_input.lower() == "q":
            break


def time_units() -> List[str]:
    """
    The function allows the user to add the time units he wants and which will be returned by the function as a list
    return: a list containing the time units as string
    """

    time_units = []
    user_time = input("Add one of the following time units: (days, hours, minutes, seconds)\n"
                      "Time units: ")

    while user_time.lower() not in ("days", "hours", "minutes", "seconds"):

        print(f"No time units found for ({user_time})")
        user_time = input("Add one of the following time units: (days, hours, minutes, seconds)\n"
                          "Time units: ")

    while user_time:

        if user_time.lower() == "days":

            if user_time not in time_units:
                time_units.append(user_time)
            else:
                print(f"{user_time} already added")

        elif user_time.lower() == "hours":

            if user_time not in time_units:
                time_units.append(user_time)
            else:
                print(f"{user_time} already added")

        elif user_time.lower() == "minutes":

            if user_time not in time_units:
                time_units.append(user_time)
            else:
                print(f"{user_time} already added")

        elif user_time.lower() == "seconds":

            if user_time not in time_units:
                time_units.append(user_time)
            else:
                print(f"{user_time} already added")

        if len(time_units) == 4:
            print("All time units have been added")
            break

        quit_program = input(
            "Press q to save your time units and exit the program, or press Enter to continue entering them:\n")

        while quit_program not in ("", "q"):
            quit_program = input(
                "Press q to save your time units and exit the program, or press Enter to continue entering them:\n")

        if quit_program.lower() == "q":
            break

        user_time = input("Add one of the following time units: (days, hours, minutes, seconds)\n"
                          "Time units: ")

        while user_time.lower() not in ("days", "hours", "minutes", "seconds"):
            print(f"No time units found for ({user_time})")
            user_time = input("Add one of the following time units: (days, hours, minutes, seconds)\n"
                              "Time units: ")

    return time_units
