# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forgotpasswordkhENPI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)
from ui_SignUp import signup
class Ui_forgotPassword(object):
    def setupUi(self, forgotPassword):
        if not forgotPassword.objectName():
            forgotPassword.setObjectName(u"forgotPassword")
        forgotPassword.resize(480, 141)
        forgotPassword.setStyleSheet(u"font: 9pt \"Arial Rounded MT Bold\";\n"
"background-color: rgb(170, 85, 255);")
        self.textEdit_5 = QTextEdit(forgotPassword)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(180, 30, 271, 31))
        self.textEdit_5.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.label_7 = QLabel(forgotPassword)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 30, 141, 31))
        self.label_7.setStyleSheet(u"")
        self.pushButton = QPushButton(forgotPassword)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 80, 121, 24))

        self.retranslateUi(forgotPassword)

        QMetaObject.connectSlotsByName(forgotPassword)
    # setupUi

    def retranslateUi(self, forgotPassword):
        forgotPassword.setWindowTitle(QCoreApplication.translate("forgotPassword", u"Dialog", None))
        self.label_7.setText(QCoreApplication.translate("forgotPassword", u"Authentication Pin:", None))
        self.pushButton.setText(QCoreApplication.translate("forgotPassword", u"Done", None))
    # retranslateUi
class forgot_password(QDialog, Ui_forgotPassword):
    def __init__(self):
        super().__init__()
        self.setupUi(self)   
        self.signup_dialog = signup()
        self.pushButton.clicked.connect(self.open_signup)
    def open_signup(self):
        self.signup_dialog.show()