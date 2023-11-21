from datetime import datetime
from tabulate import tabulate
import pytz


# display current time
def display_current_time():
    current_time = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    return current_time


# time zone conversion
def display_time_zone(time_zone):
    timezone = datetime.now(pytz.timezone(time_zone))
    return timezone.strftime("%H:%M:%S")


def display_all_time_zones():
    time_zones = []
    for timezones in pytz.all_timezones:
        time_zones.append(timezones)

    table = [time_zones[i:i + 6] for i in range(0, len(time_zones), 6)]
    return tabulate(table, tablefmt="grid")


def world_clock_display():
    time_zone = ""
    add_time_zone = input("Do you want to add a time zone? Press y to add a time zone or press Enter to quit: ")
    while add_time_zone:
        try:
            if add_time_zone.lower() == "y":
                print(display_all_time_zones())
                user_time_zone = input(
                    "\nEnter one of the time zones in the table above and in the correct format (e.g., Europe/Rome: ")
                while user_time_zone not in pytz.all_timezones:
                    user_time_zone = input(
                        "\nEnter one of the time zones in the table above and in the correct format(e.g., "
                        "Europe/Rome: ")
                time_zone += f"Current time in {user_time_zone}: {display_time_zone(user_time_zone)}\n"
                add_time_zone = input("Do you want to add a time zone? Press y to add a time zone or press Enter to quit: ")
            if add_time_zone == "":
                break

        except ValueError:
            add_time_zone = input("Do you want to add a time zone? Press y to add a time zone or press Enter to quit: ")

    print("You closed the program!\n")
    return time_zone


# display date information
def display_date_information():
    day_of_the_year = str(datetime.now().timetuple().tm_yday)
    day_of_the_week = str(datetime.now().strftime("%A"))
    week_number = str(datetime.now().isocalendar().week)
    return day_of_the_year, day_of_the_week, week_number


def table():
    data_info = display_date_information()
    data = [
        [display_current_time(), data_info[1], data_info[0], data_info[2]]
    ]
    head = ["Current time", "Day of the week", "Day of the year", "Week number"]
    return tabulate(data, headers=head, tablefmt="grid")