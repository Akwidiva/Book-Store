import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow
from addbook import Ui_MainWindow

class BookStoreApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.load_books()
        #self.pushButton_4.clicked.connect(self.buy_book)
        # self.pushButton_6.clicked.connect(self.add_to_card)
       
       
    """def load_books(self):
        response = requests.get('http://127.0.0.1:5000/books')
        if response.status_code == 200:
            books = response.json()
            
        else:
            print("Failed to fetch data")"""


    def add_to_card(self):
        title = self.lineEdit1.text()
        author = self.lineEdit_2.text()
        category = self.comboBox.currentText()
        date  = self.dateEdit.text()
        price = self.lineEdit_3.text()
        description = self.textEdit.toPlainText()
        
        if title and author:
            response = requests.post('http://127.0.0.1:5000/create_books', json={'title': title, 'author': author, 'categoty': category,'date': date, 'price': price, 'description':description })
            if response.status_code == 201:
                self.load_books()
                self.lineEdit_title.clear()
                self.lineEdit_author.clear()

    """def update_book(self):
            title = self.lineEdit5.text()
            author = self.lineEdit_6.text()
            category = self.lineEdit_9.text()
            date = self.dateEdit_2.text()
            price = self.lineEdit_7.text()
            image = self.lineEdit_8.text()
            description = self.textEdit_2.text()
            if title and author:
                response = requests.put(f'http://127.0.0.1:5000/books/{book_id}', json={'title': title, 'author': author,'category': category, 'date': date, 'price': price, 'image':image, 'description': description, })
                if response.status_code == 200:
                    self.load_books()"""

    """def delete_book(self):
        selected_row = self.tableWidget_books.currentRow()
        if selected_row >= 0:
            book_id = int(self.tableWidget_books.item(selected_row, 0).text())
            response = requests.delete(f'http://127.0.0.1:5000/books/{book_id}')
            if response.status_code == 204:
                self.load_books()"""

    """def populate_fields(self):
        selected_row = self.tableWidget_books.currentRow()
        if selected_row >= 0:
            self.lineEdit_title.setText(self.tableWidget_books.item(selected_row, 1).text())
            self.lineEdit_author.setText(self.tableWidget_books.item(selected_row, 2).text())"""

def main():
    app = QApplication(sys.argv)
    window = BookStoreApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
