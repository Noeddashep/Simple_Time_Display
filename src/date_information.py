from datetime import datetime
from typing import List

from tabulate import tabulate
import pytz


# display current time
def display_current_time() -> tuple[str, str | None]:
    """
    Displays the current date and time on the screen based on the system clock.

    return: a string that includes the current date and time and the name of the current time zone.
    """

    timezone_name = datetime.now().astimezone().tzname()
    current_time = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

    return current_time, timezone_name


# time zone conversion
def display_time_zone(time_zone: str) -> tuple[str, str, str, str]:
    """
    Gets a specific time zone and displays the current time and date in it, the day of the year, day of the week and
    the week number.

    param time_zone: a specific time zone

    return: a string containing the current time in that time zone the day of the year, the week and the week number
            relating to the requested time zone
    """

    timezone = datetime.now(pytz.timezone(time_zone))
    day_of_the_year = str(timezone.timetuple().tm_yday)
    day_of_the_week = str(timezone.strftime("%A"))
    week_number = str(timezone.isocalendar().week)

    return timezone.strftime("%d/%m/%Y - %H:%M:%S"), day_of_the_year, day_of_the_week, week_number


def display_all_time_zones() -> str:
    """
    A recap of all the time zones, in order to show them to the user and which he can use at a later time
    return: a string that displays a table with all time zones
    """

    time_zones = []
    for timezones in pytz.all_timezones:
        time_zones.append(timezones)

    table = [time_zones[i:i + 6] for i in range(0, len(time_zones), 6)]

    return tabulate(table, tablefmt="grid")


def world_clock_display() -> str:
    """
    This function allow the user to add and display multiple clocks for different time zones simultaneously.
    return: a table containing the current time and other data information in the time zones chosen by the user
    """

    time_zone = []
    print(display_all_time_zones())

    while True:
        add_time_zone = input("Do you want to add a time zone?\nPress enter to close the program or enter one of "
                              "the time zones in the table above and in the correct format (e.g. Europe/Rome): ")

        if add_time_zone == "":
            break

        if add_time_zone not in pytz.all_timezones:
            print(f"{add_time_zone} not found")
            continue

        if add_time_zone not in time_zone:
            time_zone.append(add_time_zone)

    print("\nYou closed the program!\n")

    return table(time_zone)


# display date information
def display_date_information() -> tuple[str, str, str]:
    """
    Displays an additional date information such as day of the week, day of the year, and week number.
    return: a string containing the day of the year, day of the week and the week number
    """

    day_of_the_year = str(datetime.now().timetuple().tm_yday)
    day_of_the_week = str(datetime.now().strftime("%A"))
    week_number = str(datetime.now().isocalendar().week)

    return day_of_the_year, day_of_the_week, week_number


def table(time_zone: List[str]) -> str:
    """
    A table that contains the current time and other date information.

    return: a string in the form of a table that include the current time, day of the week, day of the year and
    the week number for each time zone
    """

    current_time = display_current_time()
    data_info = display_date_information()
    data = [
        [current_time[1], current_time[0], data_info[1], data_info[0], data_info[2]]
    ]
    for zone in time_zone:
        timezone = display_time_zone(zone)
        data.append([zone, timezone[0], timezone[2], timezone[1], timezone[3]])
    head = ["Time zone", "Current time", "Day of the week", "Day of the year", "Week number"]

    return tabulate(data, headers=head, tablefmt="grid")