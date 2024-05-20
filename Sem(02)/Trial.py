import mysql.connector

# Establish a connection to the database
db = mysql.connector.connect(host='localhost', user='root', password='',database = 'management' )

# Create a cursor object
cursor = db.cursor()

# Create a new database
cursor.execute("CREATE DATABASE Management")

# Use the new database
cursor.execute("USE Management")

# Create a new table
cursor.execute("CREATE TABLE Employees (Name VARCHAR(255), Position VARCHAR(255))")

# Insert 5 rows of data
cursor.execute("INSERT INTO Employees (Name, Position) VALUES ('Arjit Sharma', 'Software Engineer')")
cursor.execute("INSERT INTO Employees (Name, Position) VALUES ('Apransh Yadav', 'Data Scientist')")
cursor.execute("INSERT INTO Employees (Name, Position) VALUES ('Bhaskar Parihar', 'Product Manager')")
cursor.execute("INSERT INTO Employees (Name, Position) VALUES ('Aman Kushwah', 'UX Designer')")
cursor.execute("INSERT INTO Employees (Name, Position) VALUES ('Ayush Saroj', 'QA Engineer')")
cursor.execute("INSERT INTO Employees (Name, Position) VALUES ('Bob', 'Analatics Engineer')")

# Update data
cursor.execute("UPDATE Employees SET Position = 'Senior Software Engineer' WHERE Name = 'Arjit Sharma'")

# Delete data
cursor.execute("DELETE FROM Employees WHERE Name = 'Ayush Saroj'")
# Commit the transaction
db.commit()

# Close the connection
db.close()
