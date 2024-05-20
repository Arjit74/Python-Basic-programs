import mysql.connector as ms

# Establish a connection to the database
db = ms.connect(host='localhost', user='root', password='' )

# Create a cursor object
cur = db.cursor()

# Create a new database
cur.execute("CREATE DATABASE Ambition")

# Use the new database
cur.execute("USE Ambition")

# Create a new table
cur.execute("CREATE TABLE Student (Name VARCHAR(255), Collage VARCAHR(255)")
 
# Insert 5 rows of data
cur.execute("INSERT INTO Employees (Name, Position) VALUES ('Arjit Sharma', 'Software Engineer')")
cur.execute("INSERT INTO Employees (Name, Position) VALUES ('Apransh Yadav', 'Data Scientist')")
cur.execute("INSERT INTO Employees (Name, Position) VALUES ('Bhaskar Parihar', 'Product Manager')")
cur.execute("INSERT INTO Employees (Name, Position) VALUES ('Aman Kushwah', 'UX Designer')")
cur.execute("INSERT INTO Employees (Name, Position) VALUES ('Ayush Saroj', 'QA Engineer')")
cur.execute("INSERT INTO Employees (Name, Position) VALUES ('Bob', 'Analatics Engineer')")
