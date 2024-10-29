from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import mysql.connector
import _mysql_connector

from PyQt5.uic import loadUiType
from sympy import false

ui,_=loadUiType('library.ui')


class MainApp(QMainWindow ,ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.Handle_Buttons()

    def Handle_UI_Changes(self):
        self.Hiding_Themes()
        self.tabWidget.tabBar().setVisible(False)

    def Handle_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_21.clicked.connect(self.Hiding_Themes)

        self.pushButton.clicked.connect(self.open_Day_to_day_tab)
        self.pushButton_2.clicked.connect(self.Open_Books_tab)
        self.pushButton_3.clicked.connect(self.Open_Users_tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_tab)

        self.pushButton_7.clicked.connect(self.Add_New_Book)

        self.pushButton_15.clicked.connect(self.Add_category)
        self.pushButton_16.clicked.connect(self.Add_Aurthor)
        self.pushButton_14.clicked.connect(self.Add_Publisher)

    def Show_Themes(self):
        self.groupBox_3.show()

    def Hiding_Themes(self):
        self.groupBox_3.hide()
##########################################
#############opening tabs ################
    def open_Day_to_day_tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Books_tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_Users_tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Settings_tab(self):
        self.tabWidget.setCurrentIndex(3)


##########################################
############# Books ################
    def Add_New_Book(self):

        self.db=MySQLdb.connector(host='localhost',user='root',password='root',db='library')
        self.cur=self.db.cursor()

        book_title=self.lineEdit_3.text()
        book_code=self.lineEdit_2.text()
        book_category=self.comboBox_3.currentText()
        book_Aurthor=self.comboBox_4.currentText()
        book_publisher=self.comboBox_5.currentText()
        book_price=self.lineEdit_4.text()

    def Search_Books(self):
        pass

    def Edit_Books(self):
        pass

    def Delete_Books(self):
        pass

##########################################
############# Users ################

    def Add_users(self):
        pass

    def Login(self):
        pass

    def Edit_users(self):
        pass

##########################################
############# settings ################
    def Add_category(self):

        #self.db = MySQLdb.connector(host='localhost' , user='root' , password='root' , db='library')
        #self.cur = self.db.cursor()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="library"
        )
        cursor = mydb.cursor()
        category_name =self.lineEdit_20.text()

        self.cur.execute('''
            insert into category (category_name) values (%s)
        ''' ,(category_name,))

        self.db.commit()
        self.statusBar().showMessage('New Categaory Added ')

    def Add_Aurthor(self):
        self.db = MySQLdb.connector(host='localhost', user='root', password='root', db='library')
        self.cur = self.db.cursor()

        aurthor_name = self.lineEdit_21.text()

        self.cur.execute('''
                    insert into aurthor (aurthor_name) values (%s)
                ''', (aurthor_name ,))

        self.db.commit()
        self.statusBar().showMessage('New Aurthor Added ')

    def Add_Publisher(self):
        self.db = MySQLdb.connector(host='localhost', user='root', password='root', db='library')
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_9.text()

        self.cur.execute('''
                    insert into publisher (publisher_name) values (%s)
                ''', (publisher_name,))

        self.db.commit()
        self.statusBar().showMessage('New Publisher Added ')



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()