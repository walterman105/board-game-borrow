#
import mysql.connector

#connects to database
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Ilovemy48pets!",
    database = "my_database"
)
cursor = conn.cursor()


#Add data function:
#Add data to table/columns
insert_query = """
    INSERT INTO boardgames (name, minPlayerCount, maxPlayerCount, gametime, age, gamecount)
    VALUES (%s, %s, %s, %s, %s, %s);
"""
print("1. Add Game")
print("2. Display Database")
choice = input("Enter your choice: ")

if choice == "1":
    name = input("Enter the name of the game: ").upper()
    minPlayerCount = int(input("Enter the minimum player count: "))
    maxPlayerCount = int(input("Enter the maximum player count: "))
    time = int(input("Enter the amount of minutes the game usually takes: "))
    age = int(input("Enter the minimum recommended age to play the game: "))

    data = (name, minPlayerCount, maxPlayerCount, time, age, 1)
    cursor.execute(insert_query, data)


elif choice == "2":
    #View data in table/columns
    select_query = "SELECT * FROM boardgames;"
    cursor.execute(select_query)
    columns = [desc[0] for desc in cursor.description]
    results = cursor.fetchall()
    print(" | ".join(columns))
    print("-------------------------------")
    for row in results:
        print(" | ".join(map(str,row)))
        print("-------------------------------")

#example of how to add column
'''
#Altar the users table, adding a new column 'birthdate'
cursor.execute("""ALTER TABLE board games
ADD COLUMN relesaseDate DATE""")
'''

conn.commit()
cursor.close()
conn.close()
#print("Data inserted successfully")