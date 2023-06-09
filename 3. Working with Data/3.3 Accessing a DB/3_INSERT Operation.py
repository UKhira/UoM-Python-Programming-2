import sqlite3;

# Open database connection
db = sqlite3.connect("TESTDB")

# Prepare a cursor object using cursor method
cursor = db.cursor()

# Prepare a SQL query to INSERT record into the database
sql = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, GENDER, 
INCOME) VALUES('Udith', 'Kavishka'. '22', 'M', '2000')"""

try :
    # Execute SQL command
    cursor.execute(sql)
    
    # Commit your changes into database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()
    
# Disconnect from server
db.close()