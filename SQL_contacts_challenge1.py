# checkdb program

import sqlite3

db = sqlite3.connect("contacts.sqlite")
name = input("please enter a name: ")

for row in db.execute("SELECT * FROM contacts WHERE name = ?", (name,)):  # can iterate the database without a cursor
    print(row)

db.close()
