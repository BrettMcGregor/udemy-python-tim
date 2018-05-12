import datetime
import time

# print("the epoch on this system starts at " + time.strftime("%c", time.gmtime(0)))
#
# print("the current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("\t Daylight saving time is in effect for this location")
# print("\t the DST timezone is " + time.tzname[1])
#
# print("Local time is " + time.strftime("%y-%m-%d %H:%M:%S", time.localtime()))
# print("UTC time is " + time.strftime("%y-%m-%d %H:%M:%S", time.gmtime()))

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
