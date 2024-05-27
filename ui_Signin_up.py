# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Signin_uphCkWeH.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QWidget)
import resource_rc
from ui_Signin import Signin
from ui_SignUp import signup
class Ui_Signin_up(object):
    def setupUi(self, Signin_up):
        if not Signin_up.objectName():
            Signin_up.setObjectName(u"Signin_up")
        Signin_up.resize(396, 138)
        Signin_up.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.pushButton = QPushButton(Signin_up)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 30, 211, 41))
        self.pushButton.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        icon = QIcon(QIcon.fromTheme(u"accessories-character-map"))
        self.pushButton.setIcon(icon)
        self.pushButton_2 = QPushButton(Signin_up)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 80, 211, 41))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.pushButton_2.setIcon(icon)
  # Connect the button to open SigninUp
    

        self.retranslateUi(Signin_up)
   
        QMetaObject.connectSlotsByName(Signin_up)
    # setupUi
 
    def retranslateUi(self, Signin_up):
        Signin_up.setWindowTitle(QCoreApplication.translate("Signin_up", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Signin_up", u"SignUp", None))
        self.pushButton_2.setText(QCoreApplication.translate("Signin_up", u"SignIn", None))
    # retranslateUi
class SigninUp(QDialog, Ui_Signin_up):
    def __init__(self):
        super().__init__()
        self.setupUi(self)   
        self.signup_dialog = signup()  # Create an instance of SignUp
        self.signin_dialog = Signin()  # Create an instance of SigninUp
        
        self.pushButton.clicked.connect(self.open_signup)  # Connect the button to open SignUp
        self.pushButton_2.clicked.connect(self.open_signin)  # Connect the button to open SignIn

    def open_signin(self):
        self.signin_dialog.show()

    
    def open_signup(self):
        self.signup_dialog.show()
