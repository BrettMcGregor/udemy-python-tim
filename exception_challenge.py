import sys


def get_int():
    while True:
        try:
            user = input("Please enter two integers > ")
            a, b = user.split()
            print(int(a) / int(b))
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        except ValueError:
            print("Wrong data type. Integers only.")
        except EOFError:
            print("User exiting the program.")
            sys.exit(0)
        else:
            print("The else is only executed if no other "
                  "earlier condition is true.")
        finally:
            print("the finally clause always executes")


get_int()
