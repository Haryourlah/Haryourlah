import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE studentdatabase")
