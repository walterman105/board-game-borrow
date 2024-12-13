import mysql.connector

#connects to database
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Ilovemy48pets!",
    database = "my_database"
)
cursor = conn.cursor()

insert_query = """
    INSERT INTO users (usernames, passwords)
    VALUES (%s, %s);
"""

running = True

while running:
    print("1. Add User")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        data = (username, password)
        cursor.execute(insert_query, data)

    elif choice == "2":
        running = False

    else:
        print("Type 1 or 2")

conn.commit()
cursor.close()
conn.close()

