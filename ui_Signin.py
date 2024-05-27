# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SigninufqNnj.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QDialog, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)
from ui_forgotpassword import forgot_password
class Ui_Signin(object):
    def setupUi(self, Signin):
        if not Signin.objectName():
            Signin.setObjectName(u"Signin")
        Signin.resize(416, 155)
        Signin.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.label_2 = QLabel(Signin)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 30, 71, 31))
        self.label_2.setStyleSheet(u"")
        self.textEdit_2 = QTextEdit(Signin)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(110, 30, 271, 31))
        self.textEdit_2.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.textEdit_3 = QTextEdit(Signin)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(110, 70, 271, 31))
        self.textEdit_3.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.label_3 = QLabel(Signin)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 81, 31))
        self.label_3.setStyleSheet(u"")
        self.pushButton = QPushButton(Signin)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 120, 75, 24))
        self.commandLinkButton = QCommandLinkButton(Signin)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(40, 110, 185, 41))

        self.retranslateUi(Signin)

        QMetaObject.connectSlotsByName(Signin)
    # setupUi

    def retranslateUi(self, Signin):
        Signin.setWindowTitle(QCoreApplication.translate("Signin", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Signin", u"Email:", None))
        self.label_3.setText(QCoreApplication.translate("Signin", u"Password:", None))
        self.pushButton.setText(QCoreApplication.translate("Signin", u"Done", None))
        self.commandLinkButton.setText(QCoreApplication.translate("Signin", u"Forgot Password", None))
    # retranslateUi
class Signin(QDialog, Ui_Signin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.forgotpassword_dialog = forgot_password()
        self.pushButton.clicked.connect(self.refresh_homepage)
        self.commandLinkButton.clicked.connect(self.open_forgotpassword)  # Corrected this line
        
    def refresh_homepage(self):
        self.hide()
        self.parent().show()  # Show the homepage again
        
    def open_forgotpassword(self):
        self.forgotpassword_dialog.show()