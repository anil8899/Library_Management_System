from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import mysql.connector
from PyQt5.uic import loadUiType

ui, _ = loadUiType('library.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI_Changes()
        self.Handle_Buttons()

        self.show_categories()
        self.show_Author()
        self.show_Publisher()

        self.show_category_combobox()
        self.show_author_combobox()
        self.show_publisher_combobox()



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
        self.pushButton_16.clicked.connect(self.Add_Author)
        self.pushButton_14.clicked.connect(self.Add_Publisher)

    def Show_Themes(self):
        self.groupBox_3.show()

    def Hiding_Themes(self):
        self.groupBox_3.hide()

    ##########################################
    ############# Opening Tabs ##############
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
        self.db = mysql.connector.connect(host='localhost', user='root', password='root', database='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_3.text()
        book_code = self.lineEdit_2.text()
        book_category = self.comboBox_3.currentText()
        book_author = self.comboBox_4.currentText()  # Fixed typo "Aurthor" -> "Author"
        book_publisher = self.comboBox_5.currentText()
        book_price = self.lineEdit_4.text()

        # Logic to insert the book data into the database
        self.cur.execute('''
            INSERT INTO books (book_title, book_code, book_category, book_author, book_publisher, book_price)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (book_title, book_code, book_category, book_author, book_publisher, book_price))

        self.db.commit()

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
    ############# Settings ################
    def Add_category(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='root', database='library')
        self.cur = self.db.cursor()

        category_name = self.lineEdit_20.text()

        self.cur.execute('''
            INSERT INTO category (category_name) VALUES (%s)
        ''', (category_name,))  # Tuple should have a trailing comma

        self.db.commit()
        self.statusBar().showMessage('New Category Added')
        self.lineEdit_20.setText('')
        self.show_categories()

    def show_categories(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='root', database='library')
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT category_name FROM category''')
        data = self.cur.fetchall()

     # You might want to display this data in your UI instead of printing it

        if data :
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row , form in enumerate(data):
                for column, item in enumerate(form) :
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)

    def Add_Author(self):  # Fixed typo "Aurthor" -> "Author"
        self.db = mysql.connector.connect(host='localhost', user='root', password='root', database='library')
        self.cur = self.db.cursor()

        author_name = self.lineEdit_21.text()

        self.cur.execute('''
            INSERT INTO author (Author_name) VALUES (%s)
        ''', (author_name,))

        self.db.commit()
        self.statusBar().showMessage('New Author Added')
        self.lineEdit_21.setText('')
        self.show_Author()

    def show_Author(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='root', database='library')
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT Author_name FROM author''')
        data = self.cur.fetchall()

     # You might want to display this data in your UI instead of printing it

        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)

    def Add_Publisher(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='root', database='library')
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_9.text()

        self.cur.execute('''
            INSERT INTO publisher (publisher_name) VALUES (%s)
        ''', (publisher_name,))

        self.db.commit()

        self.statusBar().showMessage('New Publisher Added')
        self.lineEdit_9.setText('')
        self.show_Publisher()

    def show_Publisher(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='root', database='library')
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT publisher_name FROM publisher''')
        data = self.cur.fetchall()

        # You might want to display this data in your UI instead of printing it

        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)


##########################################
 ############# show Setting data in UI ################
    def show_category_combobox(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='root', database='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' select category_name from category ''')
        data = self.cur.fetchall()

        for category in data:
            print(category[0])
            self.comboBox_3.addItem(category[0])

    def show_author_combobox(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='root', database='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' select Author_name from author ''')
        data = self.cur.fetchall()

        for author in data:

             self.comboBox_4.addItem(author[0])

    def show_publisher_combobox(self):
        self.db = mysql.connector.connect(host='localhost', user='root', password='root', database='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' select publisher_name from publisher ''')
        data = self.cur.fetchall()

        for publisher in data:
            self.comboBox_5.addItem(publisher[0])


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
