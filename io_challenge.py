# Write a program to append the times tables to our jabberwocky poem
# in sample.txt. We want the tables from 2 to 12 (similar to the output
# from the For loops part 2 lecture in section 6).
#
# The first column of numbers should be right justified. As an example,
# the 2 times table should look like this:
#   1 times 2 is 2
#   2 times 2 is 4
#   3 times 2 is 6
#   4 times 2 is 8
#   5 times 2 is 10
#   6 times 2 is 12
#   7 times 2 is 14
#   8 times 2 is 16
#   9 times 2 is 18
#  10 times 2 is 20
#  11 times 2 is 22
#  12 times 2 is 24


# program to generate formatted multiplication tables


def multiplication_tables(start, stop):
    for i in range(start, stop + 1):
        for j in range(1, 13):
            print("{:>3} times {} is {}".format(j, i, i * j), file=test_file)
        print("-" * 20, file=test_file)


# open file to append

with open("C:\Projects\Python\\udemy-python-tim\sample.txt", "a") as test_file:
    multiplication_tables(2, 12)
