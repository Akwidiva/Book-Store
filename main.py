import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from bookstore_ui import Ui_MainWindow

class BookStoreApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_books()
        self.pushButton_add.clicked.connect(self.add_book)
        self.pushButton_update.clicked.connect(self.update_book)
        self.pushButton_delete.clicked.connect(self.delete_book)
        self.tableWidget_books.itemSelectionChanged.connect(self.populate_fields)

    def load_books(self):
        response = requests.get('http://127.0.0.1:5000/books')
        if response.status_code == 200:
            books = response.json()
            self.tableWidget_books.setRowCount(0)
            for book in books:
                row_position = self.tableWidget_books.rowCount()
                self.tableWidget_books.insertRow(row_position)
                self.tableWidget_books.setItem(row_position, 0, QTableWidgetItem(str(book['id'])))
                self.tableWidget_books.setItem(row_position, 1, QTableWidgetItem(book['title']))
                self.tableWidget_books.setItem(row_position, 2, QTableWidgetItem(book['author']))
        else:
            print("Failed to fetch data")

    def add_book(self):
        title = self.lineEdit_title.text()
        author = self.lineEdit_author.text()
        if title and author:
            response = requests.post('http://127.0.0.1:5000/books', json={'title': title, 'author': author})
            if response.status_code == 201:
                self.load_books()
                self.lineEdit_title.clear()
                self.lineEdit_author.clear()

    def update_book(self):
        selected_row = self.tableWidget_books.currentRow()
        if selected_row >= 0:
            book_id = int(self.tableWidget_books.item(selected_row, 0).text())
            title = self.lineEdit_title.text()
            author = self.lineEdit_author.text()
            if title and author:
                response = requests.put(f'http://127.0.0.1:5000/books/{book_id}', json={'title': title, 'author': author})
                if response.status_code == 200:
                    self.load_books()

    def delete_book(self):
        selected_row = self.tableWidget_books.currentRow()
        if selected_row >= 0:
            book_id = int(self.tableWidget_books.item(selected_row, 0).text())
            response = requests.delete(f'http://127.0.0.1:5000/books/{book_id}')
            if response.status_code == 204:
                self.load_books()

    def populate_fields(self):
        selected_row = self.tableWidget_books.currentRow()
        if selected_row >= 0:
            self.lineEdit_title.setText(self.tableWidget_books.item(selected_row, 1).text())
            self.lineEdit_author.setText(self.tableWidget_books.item(selected_row, 2).text())

def main():
    app = QApplication(sys.argv)
    window = BookStoreApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
