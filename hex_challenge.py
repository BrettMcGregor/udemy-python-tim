# for i in range(17):
#     print("{0:>2} in hex is {0:>02x}".format(i))
#
# x = 0x20
# y = 0x0a
#
# print(x)
# print(y)
# print(x * y)
#
# print(0b101010)

# When converting a decimal number to binary, you look for the highest power
# of 2 smaller than the number and put a 1 in that column. You then take the
# remainder and repeat the process with the next highest power - putting a 1
# if it goes into the remainder and a zero otherwise. Keep repeating until you
# have dealt with all powers down to 2 ** 0 (i.e., 1).
#
# Write a program that requests a number from the keyboard, then prints out
# its binary representation.
#
# Obviously you could use a format string, but that is not allowed for this
# challenge.
#
# The program should cater for numbers up to 65535; i.e. (2 ** 16) - 1
#
# Hint: you will need integer division (//), and modulo (%) to get the remainder.
# You will also need ** to raise one number to the power of another:
# For example, 2 ** 8 raises 2 to the power 8.
#
# As an optional extra, avoid printing leading zeros.
#
# Once the program is working, modify it to print Octal rather than binary.

number = int(input("Please enter an integer between 1 and 65535: "))
remainder = number
binary = []
print("check: {0} in binary is {0:0b}".format(number))

# this block is not handling input of zero
for i in range(16, -1, -1):
    if 2**i > remainder:
        binary.append("0")
    else:
        binary.append("1")
        remainder -= 2**i

binary = "".join(binary)
binary = binary.lstrip("0")
print("{} in binary is {}".format(number, binary))

octal = []
remainder = number
for i in range(6, 0, -1):
    octal_o = remainder//(8 ** i)
    octal.append(octal_o)
    if remainder//(8 ** i) > 0:
        remainder -= (8 ** i) * (remainder//(8 ** i))
else:
    octal.append(remainder)

print("{0} in octal is {1}".format(number, ("".join(str(x) for x in octal)).lstrip("0")))
# print("{0} in octal is {0:0o}".format(number))
