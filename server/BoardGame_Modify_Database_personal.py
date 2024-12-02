
import mysql.connector

class Database:
    def __init__(self):

        self.games_dict = {}

    def show_games(self):
        #connects to database
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "wugsob-Poxger-duvna8",
            database = "my_database"
        )
        cursor = conn.cursor()

        # View data in table/columns
        select_query = "SELECT * FROM boardgames;"
        cursor.execute(select_query)
            
        # Fetch all rows from the query result
        rows = cursor.fetchall()
        
        # Get column names from cursor description
        columns = [desc[0] for desc in cursor.description]
            
        # Convert rows to a list of dictionaries1
        games_list = [dict(zip(columns, row)) for row in rows]
            
        # Convert list of dictionaries to a dictionary with game names as keys
        self.games_dict = {game['name']: game for game in games_list}


    def addgame(self, data):
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "wugsob-Poxger-duvna8",
            database = "my_database"
        )
        cursor = conn.cursor()
        #Add data function:
        #Add data to table/columns
        insert_query = """
            INSERT INTO boardgames (name, minPlayerCount, maxPlayerCount, gametime, age, gamecount)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        # name = input("Enter the name of the game: ").upper()
        # minPlayerCount = int(input("Enter the minimum player count: "))
        # maxPlayerCount = int(input("Enter the maximum player count: "))
        # time = int(input("Enter the amount of minutes the game usually takes: "))
        # age = int(input("Enter the minimum recommended age to play the game: "))

        cursor.execute(insert_query, data)

        conn.commit()
        cursor.close()
        conn.close()

        
        # print("1. Add Game")
        # print("2. Display Database")
        # choice = input("Enter your choice: ")

        # if choice == "1":
        #     add_game()

        # elif choice == "2":
        #     show_games()

        # conn.commit()
        # cursor.close()
        # conn.close()
        # #print("Data inserted successfully")

# while True:
#     print("1. Add Game")
#     print("2. Display Database")
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         Database.add_game("Catan", 3, 4, 60, 10)

#     elif choice == "2":
#         Database.show_games()

#     else:
#         print("Invalid choice")
#         break



