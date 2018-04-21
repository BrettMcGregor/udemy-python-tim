# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains, and the length of each segment.
#
# An IP address consists of 4 numbers, separated from each other with a full stop. But
# your program should just count however many are entered
# Examples of the input you may get are:
#    127.0.0.1
#    .192.168.0.1
#    10.0.123456.255
#    172.16
#    255
#
# So your program should work even with invalid IP Addresses. We're just interested in the
# number of segments and how long each one is.
#
# Once you have a working program, here are some more suggestions for invalid input to test:
#    .123.45.678.91
#    123.4567.8.9.
#    123.156.289.10123456
#    10.10t.10.10
#    12.9.34.6.12.90
#    '' - that is, press enter without typing anything
#
# This challenge is intended to practise for loops and if/else statements, so although
# you could use other techniques (such as splitting the string up), that's not the
# approach we're looking for here.
#
# take user input - IP address
# a list, for testing
# IP_list1 = ["127.0.0.1", ".192.168.0.1","10.0.123456.255","172.16","255"]
# IP_list2 = [".123.45.678.91", "123.4567.8.9.", "123.156.289.10123456", "10.10t.10.10", "12.9.34.6.12.90", ""  ]
# for now, use single item from list

user_IP = input("Please enter an IP address: ")

# determine number of segments and length of each segment

segment = 0
length = 0

print(user_IP)
if user_IP == "":
    print("empty string")

for char in user_IP:
    length += 1
    if char == ".":
        length -= 1
        if length > 0:
            segment += 1
            print("Segment {} is {} characters in length".format(segment, length))
            length = 0
if length > 0:
    segment += 1
    print("Segment {} is {} characters in length".format(segment, length))
segment = 0
length = 0
