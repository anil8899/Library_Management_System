import mysql.connector

db=mysql.connector.connect(
        host='localhost',       # or your MySQL host
        user='root',    # MySQL username
        password='root',# MySQL password
        database='library'

)
print('Connected to MySQL database',db)



