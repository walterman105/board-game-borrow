import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'root',      # Replace with your MySQL username
    'password': 'Ilovemy48pets!',   # Replace with your MySQL password
    'host': 'localhost',           # Adjust if needed (e.g., an IP address)
    'raise_on_warnings': True
}

try:
    # Establish the connection
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Create a new database
    cursor.execute("CREATE DATABASE IF NOT EXISTS my_database")
    print("Database 'my_database' created successfully.")

    # SQL query to insert data
    add_data_query = """INSERT INTO your_table_name (column1, column2, column3)
    VALUES (%s, %s, %s)
    """
    # Replace values with actual data you want to insert
    data = ('value1', 'value2', 'value3')

    #execute the query
    cursor.execute(add_data_query, data)

    # Commit the changes
    conn.commit()
    print(f"{cursor.rowcount} record(s) inserted.")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)
finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()