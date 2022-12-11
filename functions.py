import mysql.connector as mysql
from connection import *


#create a database in mysql
def init_db():
    #new database
    new_db = """
            CREATE DATABASE pytst;
            
            """
    #new table in database
    new_table = """
            CREATE TABLE IF NOT EXISTS data(
                id AUTO_INCRIMENT,name VARCHAR(255),pass VARCHAR(255)
                );
                """

    #creating the query
    #setting new changes (commiting) 

    cursor.execute(new_db)
    dataBase.commit()
    cursor.execute(new_table)
    dataBase.commit()
    cursor.close()

init_db() #calling the function and creat a new database
dataBase.close()

#insert into database
def insert_to_db():
    add_home = """
            INSERT INTO data(user,password)
            VALUES(%s,%s);
            """
    
    cursur.execute(add_home,(data['user'],data['password']))
    dataBase.commit()
    cursor.close()