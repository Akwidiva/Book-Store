# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SignUpigoTtY.ui'
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

class Ui_Signup(object):
    def setupUi(self, Signup):
        if not Signup.objectName():
            Signup.setObjectName(u"Signup")
        Signup.resize(480, 280)
        Signup.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"font: 10pt \"Arial Rounded MT Bold\";")
        self.label = QLabel(Signup)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 71, 31))
        self.label.setStyleSheet(u"")
        self.textEdit = QTextEdit(Signup)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(150, 30, 271, 31))
        self.textEdit.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.textEdit_2 = QTextEdit(Signup)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(150, 70, 271, 31))
        self.textEdit_2.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.label_2 = QLabel(Signup)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 71, 31))
        self.label_2.setStyleSheet(u"")
        self.textEdit_3 = QTextEdit(Signup)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(150, 110, 271, 31))
        self.textEdit_3.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.label_3 = QLabel(Signup)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 110, 71, 31))
        self.label_3.setStyleSheet(u"")
        self.label_4 = QLabel(Signup)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 150, 141, 31))
        self.label_4.setStyleSheet(u"")
        self.textEdit_4 = QTextEdit(Signup)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(150, 150, 271, 31))
        self.textEdit_4.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.pushButton = QPushButton(Signup)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 250, 121, 24))
        self.label_5 = QLabel(Signup)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 200, 141, 31))
        self.label_5.setStyleSheet(u"")
        self.textEdit_5 = QTextEdit(Signup)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(150, 200, 271, 31))
        self.textEdit_5.setStyleSheet(u"background-color: rgb(85, 0, 127);")

        self.retranslateUi(Signup)

        QMetaObject.connectSlotsByName(Signup)
    # setupUi

    def retranslateUi(self, Signup):
        Signup.setWindowTitle(QCoreApplication.translate("Signup", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Signup", u" Name:", None))
        self.label_2.setText(QCoreApplication.translate("Signup", u"Email:", None))
        self.label_3.setText(QCoreApplication.translate("Signup", u"Password:", None))
        self.label_4.setText(QCoreApplication.translate("Signup", u"Confirm Password:", None))
        self.pushButton.setText(QCoreApplication.translate("Signup", u"Done", None))
        self.label_5.setText(QCoreApplication.translate("Signup", u"Authentication Pin:", None))
    # retranslateUi
class signup(QDialog, Ui_Signup):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.pushButton.clicked.connect(self.refresh_homepage)
        
    def refresh_homepage(self):
        self.hide()
        self.parent().show()  # Show the homepage again
