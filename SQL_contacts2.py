import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "newemail@update.com"
phone = input("please enter a phone number: ")

# update_sql = f"UPDATE contacts SET email = '{new_email}' WHERE contacts.phone = {phone}"
update_sql = f"UPDATE contacts SET email = ? WHERE contacts.phone = ?"  # ? are placeholders for parameter substitutions
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email,phone))  # the tuple at end of line are parameters to be substituted
# update_cursor.executescript(update_sql)  # .executescript will run multiple statements in a single call
print(f"{update_cursor.rowcount} rows updated")

update_cursor.connection.commit()  # using cursor property to commit the changes
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):  # can iterate the database without a cursor
    print(name)
    print(phone)
    print(email)
    print("-" * 20)


db.close()
