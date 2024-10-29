import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="library"
)

mycursor = mydb.cursor()

mycursor.execute("select * from users ")

users = mycursor.fetchall()


for user_name in users:
    print(user_name)
    print('user_name :' + users[1])