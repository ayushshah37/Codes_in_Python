import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="root",
 )
# create db
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE AYUSH")
