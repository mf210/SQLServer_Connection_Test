import pyodbc

def test_sql_server_connection(server, port, database, username, password):
    try:
        # Define the connection string with port
        conn_str = f'DRIVER=SQL Server;SERVER={server},{port};DATABASE={database};UID={username};PWD={password}'

        # Attempt to establish a connection
        conn = pyodbc.connect(conn_str)
        
        # If successful, print connection established message
        print("Connection to SQL Server established successfully!")
        
        # Close the connection
        conn.close()
        
        return True
    except pyodbc.Error as e:
        # If connection fails, print error message
        print("Error connecting to SQL Server:", e)
        return False


server = '192.168.1.1'
port = '12826' 
database = 'datatbase'
username = 'username'
password = 'password'

# Test the connection
test_sql_server_connection(server, port, database, username, password)
