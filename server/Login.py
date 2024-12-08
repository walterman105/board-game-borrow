import mysql.connector

#connects to database
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Ilovemy48pets!",
    database = "my_database"
)
cursor = conn.cursor()

running = True
while running:
    print("1. Login")
    print("2. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        username = input("Enter username: ")
        cursor.execute("SELECT usernames from users;") #selects all the rows from the username columns in the users table
        user_result = cursor.fetchall() #gathers/fetches all the rows
        if any(row[0] == username for row in user_result): #Checks if any rows first element in user result is equal to user input of username
            for index, row in enumerate(user_result, start=1): #loops each row while tracking index number. enumerate function. Starts at 1 for mysql structure
                if row[0] == username: #Checks if any rows first element in user result is equal to user input of username
                    row_number = {index} #if username is found, sets 'row_number' to the index value of where username was found
                    row_number = int(row_number.pop()) #changes the index from set to int
                    print("Username Found")
                    password = input("Enter password: ") #password check
                    # Query to fetch the specific row using LIMIT and OFFSET
                    password_query = "SELECT passwords FROM users LIMIT 1 OFFSET %s;" #limit makes sure only 1 value is returned, offset
                    # Calculate offset (row_number - 1 since OFFSET is zero-based)
                    cursor.execute(password_query, (row_number - 1,)) #selects the password at the row_number
                    check_password = cursor.fetchone() #gathers/fetches value and stores it in check_password variable
                    check_password = ''.join(map(str, check_password)) #changes set to string
                    if password == check_password: #if matches, login successful
                        print("Login Successful!")
                        #modify menu driven program:
                        # Add data function:
                        # Add data to table/columns
                        boardgame_query = """
                            INSERT INTO boardgames (name, minPlayerCount, maxPlayerCount, gametime, age, gamecount, user)
                            VALUES (%s, %s, %s, %s, %s, %s, %s);
                        """
                        while True:
                            print("1. Add Game")
                            print("2. Delete Game")
                            print("3. Display Database")
                            print("4. Exit")
                            choice = input("Enter your choice: ")

                            if choice == "1":
                                boardgame_name = input("Enter the name of the game: ").upper()
                                name_check = "SELECT name FROM boardgames WHERE name = %s;"
                                cursor.execute(name_check, (boardgame_name,))
                                name_check_results = cursor.fetchall()
                                game_name = name_check_results[0][0]
                                print(game_name)
                                if game_name == boardgame_name:
                                    print("Game is already in database. Add another copy?")
                                    print("1. Yes")
                                    print("2. No")
                                    selection = input("Enter your decision: ")
                                    if selection == "1":
                                        new_query = """
                                        INSERT INTO boardgames (name, minPlayerCount, maxPlayerCount, gametime, age, gamecount, user)
                                        SELECT name, minPlayerCount, maxPlayerCount, gametime, age, gamecount, %s
                                        FROM boardgames WHERE name = %s;
                                        """
                                        cursor.execute(new_query, (username, boardgame_name))
                                        conn.commit()
                                        print("Added to database")
                                    elif selection == "2":
                                        print("------------")
                                else:
                                    minPlayerCount = int(input("Enter the minimum player count: "))
                                    maxPlayerCount = int(input("Enter the maximum player count: "))
                                    time = int(input("Enter the amount of minutes the game usually takes: "))
                                    age = int(input("Enter the minimum recommended age to play the game: "))
                                    user = username

                                    data = (boardgame_name, minPlayerCount, maxPlayerCount, time, age, 1, user)
                                    cursor.execute(boardgame_query, data)
                                    conn.commit()
                                    print("Game Added")
                                    print("--------------------------")

                            elif choice == "2":
                                delete_query = "SELECT * FROM boardgames WHERE user = %s;" #selects all rows where the value user in boardgames is placeholder
                                value_to_find = username
                                cursor.execute(delete_query, (value_to_find,))

                                delete_results = cursor.fetchall()
                                for row in delete_results:
                                    print(row)
                                while True:
                                    print("1. Continue Delete")
                                    print("2. Quit")
                                    decision = input("Enter your choice: ")
                                    if decision == "1":
                                        delete_choice = input("Type the name of the game you would like to delete: ").upper()
                                        delete_query_final = "DELETE FROM boardgames WHERE name = %s AND user = %s;"
                                        values = (delete_choice, username)
                                        cursor.execute(delete_query_final, values)
                                        conn.commit()
                                        print("Delete Successful")
                                        print("------------------------------------")
                                    elif choice == "2":
                                        break
                            elif choice == "3":
                                # View data in table/columns
                                select_query = "SELECT * FROM boardgames;"
                                cursor.execute(select_query)
                                columns = [desc[0] for desc in cursor.description]
                                results = cursor.fetchall()
                                print(" | ".join(columns))
                                print("-------------------------------")
                                for row in results:
                                    print(" | ".join(map(str, row)))
                                    print("-------------------------------")

                            elif choice == "4":
                                break


                    else:
                        print("Password Failed") #no match

        else:
            print("Username not found")

    elif choice == "2":
        running = False
    else:
        print("Type 1 or 2")

conn.commit()
cursor.close()
conn.close()