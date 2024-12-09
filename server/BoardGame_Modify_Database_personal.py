
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
        self.games_list = [dict(zip(columns, row)) for row in rows]
       
        # Convert list of dictionaries to a dictionary with game names as keys
        self.games_dict = {game['name']: game for game in self.games_list}



    def addgame(self, data):
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "wugsob-Poxger-duvna8",
            database = "my_database"
        )
        cursor = conn.cursor()

        # username = data[6]
        # boardgame_name = data[0]
        # name_check = "SELECT name FROM boardgames WHERE name = %s;"
        # cursor.execute(name_check, (boardgame_name,))
        # name_check_results = cursor.fetchall()
        # game_name = name_check_results[0][0]
        # print(game_name)
        
        # if game_name == boardgame_name:
        #     new_query = """
        #         INSERT INTO boardgames (name, minPlayerCount, maxPlayerCount, gametime, age, gamecount, owner)
        #         SELECT name, minPlayerCount, maxPlayerCount, gametime, age, gamecount, %s
        #         FROM boardgames WHERE name = %s;
        #         """
        #     cursor.execute(new_query, (username, boardgame_name))
        #     conn.commit()
        #     print("Added to database")
        # else:
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
            INSERT INTO users (email, password)
            VALUES (%s, %s);
        """

        cursor.execute(insert_query, data)

        conn.commit()
        cursor.close()
        conn.close()

    def login(self, data):
        
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "wugsob-Poxger-duvna8",
            database = "my_database"
        )
        cursor = conn.cursor()

        username = data[0]
        cursor.execute("SELECT email from users;") #selects all the rows from the username columns in the users table
        user_result = cursor.fetchall() #gathers/fetches all the rows
        if any(row[0] == username for row in user_result): #Checks if any rows first element in user result is equal to user input of username
            for index, row in enumerate(user_result, start=1): #loops each row while tracking index number. enumerate function. Starts at 1 for mysql structure
                if row[0] == username: #Checks if any rows first element in user result is equal to user input of username
                    row_number = {index} #if username is found, sets 'row_number' to the index value of where username was found
                    row_number = int(row_number.pop()) #changes the index from set to int
                    print("Username Found")
                    password = data[1] #password check
                    # Query to fetch the specific row using LIMIT and OFFSET
                    password_query = "SELECT password FROM users LIMIT 1 OFFSET %s;" #limit makes sure only 1 value is returned, offset
                    # Calculate offset (row_number - 1 since OFFSET is zero-based)
                    cursor.execute(password_query, (row_number - 1,)) #selects the password at the row_number
                    check_password = cursor.fetchone() #gathers/fetches value and stores it in check_password variable
                    check_password = ''.join(map(str, check_password)) #changes set to string
                    if password == check_password: #if matches, login successful
                        print("Login Successful!")
                        return True
                        cursor.close()
                        conn.close()
                        #modify menu driven program:
                        # Add data function:
                        # Add data to table/columns
        else:
            print("Username not found")
            return False

        # conn.commit()
        

    def deletegame(self, data):

        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "wugsob-Poxger-duvna8",
            database = "my_database"
        )
        cursor = conn.cursor()

        delete_query = "SELECT * FROM boardgames WHERE owner = %s;" #selects all rows where the value user in boardgames is placeholder
        value_to_find = data[0]
        cursor.execute(delete_query, (value_to_find,))

        delete_results = cursor.fetchall()

        delete_choice = data[1].upper()
        delete_query_final = "DELETE FROM boardgames WHERE name = %s AND owner = %s;"
        values = (delete_choice, data[0])
        cursor.execute(delete_query_final, values)
        conn.commit()
        cursor.close()
        conn.close()