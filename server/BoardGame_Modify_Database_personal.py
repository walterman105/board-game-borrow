
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
            INSERT INTO boardgames (name, minPlayerCount, maxPlayerCount, gametime, age, gamecount, owner)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """

        cursor.execute(insert_query, data)

        conn.commit()
        cursor.close()
        conn.close()

    def adduser(self, data):
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
            INSERT INTO users (Username, Email, Password, UserID)
            VALUES (%s, %s, %s, %s);
        """

        cursor.execute(insert_query, data)

        conn.commit()
        cursor.close()
        conn.close()

    def checkusers(self):
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "wugsob-Poxger-duvna8",
            database = "my_database"
        )
        cursor = conn.cursor()

        Users = "SELECT Username FROM users"

        cursor.execute(Users)
        rows = cursor.fetchall()

#         print(rows)

# d = Database()
# d.checkusers()