import mysql.connector


def Add_category(self):
    # self.db = MySQLdb.connector(host='localhost' , user='root' , password='root' , db='library')
    # self.cur = self.db.cursor()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="library"
    )


self.cur.execute('''SELECT author_name FROM author''')