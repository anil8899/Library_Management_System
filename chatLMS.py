from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
import mysql.connector
import sys

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="library_management"
    )

# Main Application Class
class LibraryApp(QMainWindow):
    def __init__(self):
        super(LibraryApp, self).__init__()
        loadUi("library.ui", self)  # Load the .ui file

        # Set up button connections
        self.addBookButton.clicked.connect(self.add_book)
        self.searchBookButton.clicked.connect(self.search_book)
        self.issueBookButton.clicked.connect(self.issue_book)
        self.returnBookButton.clicked.connect(self.return_book)
        self.addMemberButton.clicked.connect(self.add_member)
        self.searchMemberButton.clicked.connect(self.search_member)

        # Load book and member lists on startup
        self.load_books()
        self.load_members()

    def add_book(self):
        title = self.titleInput.text()
        author = self.authorInput.text()
        genre = self.genreInput.text()
        isbn = self.isbnInput.text()

        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO Books (title, author, genre, isbn) VALUES (%s, %s, %s, %s)", 
                       (title, author, genre, isbn))
        db.commit()
        db.close()

        QMessageBox.information(self, "Success", "Book added successfully!")
        self.load_books()

    def search_book(self):
        search_term = self.searchBookInput.text()
        db = connect_db()
        cursor = db.cursor()
        query = f"SELECT * FROM Books WHERE title LIKE '%{search_term}%' OR author LIKE '%{search_term}%'"
        cursor.execute(query)
        result = cursor.fetchall()
        db.close()

        self.bookTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.bookTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.bookTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def load_books(self):
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Books")
        result = cursor.fetchall()
        db.close()

        self.bookTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.bookTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.bookTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def add_member(self):
        name = self.memberNameInput.text()
        email = self.memberEmailInput.text()
        phone = self.memberPhoneInput.text()
        address = self.memberAddressInput.text()

        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO Members (name, email, phone, address) VALUES (%s, %s, %s, %s)", 
                       (name, email, phone, address))
        db.commit()
        db.close()

        QMessageBox.information(self, "Success", "Member added successfully!")
        self.load_members()

    def search_member(self):
        search_term = self.searchMemberInput.text()
        db = connect_db()
        cursor = db.cursor()
        query = f"SELECT * FROM Members WHERE name LIKE '%{search_term}%' OR email LIKE '%{search_term}%'"
        cursor.execute(query)
        result = cursor.fetchall()
        db.close()

        self.memberTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.memberTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.memberTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def load_members(self):
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Members")
        result = cursor.fetchall()
        db.close()

        self.memberTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.memberTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.memberTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def issue_book(self):
        book_id = self.bookIdInput.text()
        member_id = self.memberIdInput.text()

        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO Loans (book_id, member_id, loan_date) VALUES (%s, %s, CURDATE())", 
                       (book_id, member_id))
        cursor.execute("UPDATE Books SET available = FALSE WHERE book_id = %s", (book_id,))
        db.commit()
        db.close()

        QMessageBox.information(self, "Success", "Book issued successfully!")
        self.load_books()

    def return_book(self):
        book_id = self.returnBookIdInput.text()

        db = connect_db()
        cursor = db.cursor()
        cursor.execute("UPDATE Loans SET return_date = CURDATE() WHERE book_id = %s AND return_date IS NULL", (book_id,))
        cursor.execute("UPDATE Books SET available = TRUE WHERE book_id = %s", (book_id,))
        db.commit()
        db.close()

        QMessageBox.information(self, "Success", "Book returned successfully!")
        self.load_books()


# Main function to run the app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LibraryApp()
    window.show()
    sys.exit(app.exec_())
