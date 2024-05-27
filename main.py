from PySide6.QtWidgets import QApplication, QDialog
from homepage import Ui_Homepage
from bookdetails import Ui_bookdetails1
from profile_ui import Ui_profile
from ui_Signin_up import SigninUp
from ui_Signin import Signin
class HomePage(QDialog, Ui_Homepage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.book_details = BookDetails()
        self.profile_page = Profile()  # Create an instance of the Profile page
        
        
        # Connect group box clicks to open corresponding page in BookDetails
        self.groupBox.clicked.connect(lambda: self.open_book_details_page(0))
        self.groupBox_2.clicked.connect(lambda: self.open_book_details_page(1))
        self.groupBox_3.clicked.connect(lambda: self.open_book_details_page(2))
        self.groupBox_4.clicked.connect(lambda: self.open_book_details_page(3))
        self.groupBox_5.clicked.connect(lambda: self.open_book_details_page(4))
        self.groupBox_6.clicked.connect(lambda: self.open_book_details_page(5))
        self.groupBox_7.clicked.connect(lambda: self.open_book_details_page(6))
        self.groupBox_8.clicked.connect(lambda: self.open_book_details_page(7))
        self.groupBox_9.clicked.connect(lambda: self.open_book_details_page(8))
        self.groupBox_10.clicked.connect(lambda: self.open_book_details_page(9))
        
           # Connect pushButton_2 to open the profile page
        self.pushButton_2.clicked.connect(self.open_profile_page)
       

    def open_book_details_page(self, index):
        self.book_details.stackedWidget.setCurrentIndex(index)
        self.book_details.show()
    def open_profile_page(self):
        self.profile_page.show()
class BookDetails(QDialog, Ui_bookdetails1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()

    def setup_connections(self):
        # Connect all back buttons to refresh homepage
        self.pushButton_15.clicked.connect(self.refresh_homepage)
        self.pushButton_16.clicked.connect(self.refresh_homepage)
        self.pushButton_17.clicked.connect(self.refresh_homepage)
        self.pushButton_18.clicked.connect(self.refresh_homepage)
        self.pushButton_19.clicked.connect(self.refresh_homepage)
        self.pushButton_20.clicked.connect(self.refresh_homepage)
        self.pushButton_21.clicked.connect(self.refresh_homepage)
        self.pushButton_22.clicked.connect(self.refresh_homepage)
        self.pushButton_23.clicked.connect(self.refresh_homepage)
        self.pushButton_24.clicked.connect(self.refresh_homepage)

    def refresh_homepage(self):
        self.hide()
        self.parent().show()  # Show the homepage again

class Profile(QDialog, Ui_profile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.signin_up_dialog = SigninUp()  # Create an instance of SigninUp
        self.pushButton.clicked.connect(self.open_signin_up)  # Connect the button to open SigninUp

    def open_signin_up(self):
        self.signin_up_dialog.show()   
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    homepage = HomePage()
    homepage.show()
    sys.exit(app.exec())
