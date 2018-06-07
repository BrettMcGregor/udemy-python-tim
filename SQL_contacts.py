import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES ('Tim', 6545678, 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@myemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

print("fetchall:", cursor.fetchall())  # .fetchall() returns all records as a list (not a good idea for large db)

cursor.execute("SELECT * FROM contacts")

print()
print("fetchone:", cursor.fetchone())  # .fetchone() returns next record as a list
print()

cursor.execute("SELECT * FROM contacts")  # run the query again because the cursor generator is out of rows

for row in cursor:
    print(row)

print()

cursor.execute("SELECT * FROM contacts")  # run the query again because the cursor generator is out of rows
for name, phone, email in cursor:   # unpacking the tuple (contents of each row)
    print(name)
    print(phone)
    print(email)
    print("-"*40)

cursor.close()

db.commit()  # commits the transaction(s) to the database

db.close()

