# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz

# create and print numbered menu
print("{:^20}\n".format("Time Zone List") + "-" * 20)

for x in range(9):
    print("{}. {}".format(x + 1, pytz.all_timezones[x + 1]))



while True:
    location = int(input("\nSelect a Time Zone from the list above. (Zero to quit) \n> "))

    if location == 0:
        break
    if location in range(9):
        # print
        # time in timezone
        # local time
        # UTC time
        # format the date/time

        tz_to_display = pytz.timezone(pytz.all_timezones[location])

        local_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(pytz.all_timezones[location], local_time.strftime("%A %x %X %z"), local_time.tzname()))
        print("The local time is {}".format(datetime.datetime.now().strftime("%A %x %X")))
        print("The UTC time is {}".format(datetime.datetime.utcnow().strftime("%A %x %X")))
        print()
