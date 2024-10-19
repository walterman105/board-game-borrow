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
name = input("Enter the name of the game: ").upper()
minPlayerCount = int(input("Enter the minimum player count: "))
maxPlayerCount = int(input("Enter the maximum player count: "))
time = int(input("Enter the amount of minutes the game usually takes: "))
age = int(input("Enter the minimum recommended age to play the game: "))


data = (name, minPlayerCount, maxPlayerCount, time, age, 1)
cursor.execute(insert_query, data)


#View data in table/columns
select_query = "SELECT * FROM boardgames;"
cursor.execute(select_query)
results = cursor.fetchall()
for row in results:
    print(row)

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