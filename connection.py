import mysql.connector as mysql


dataBase = mysql.connect(
    host = "localhost",
    user = "root",
    password = ""
)

cursor = dataBase.cursor()




