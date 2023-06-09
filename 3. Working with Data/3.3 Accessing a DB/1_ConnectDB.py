import sqlite3

# Open the database connection
db = sqlite3.connect("TESTDB")

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Execute SQL query using execute() method 
cursor.execute("SELECT VERSION")

# Fetch a single row using fetchone() method
data = cursor.fetchone()
print("Database Version : %s" %data)

# Disconnect from the server
db.close()