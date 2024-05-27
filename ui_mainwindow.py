# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowJVvAD.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

import ui_mainwindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(792, 1161)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 190, 47, 13))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 380, 61, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 380, 71, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 70, 91, 16))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 130, 131, 16))
        self.textEdit_7 = QTextEdit(self.centralwidget)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(10, 150, 301, 31))
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 190, 91, 20))
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 320, 81, 16))
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 450, 151, 16))
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 350, 211, 16))
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 530, 331, 31))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 90, 301, 31))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 480, 491, 31))
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(10, 30, 291, 31))
        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(10, 410, 181, 31))
        self.textEdit_4 = QTextEdit(self.centralwidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(260, 410, 221, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 570, 581, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 220, 511, 31))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 260, 251, 41))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(300, 260, 221, 41))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 47, 13))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 792, 21))
        self.menucheck_out = QMenu(self.menubar)
        self.menucheck_out.setObjectName(u"menucheck_out")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menucheck_out.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"first name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"last name", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Region", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"town/city", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"your order", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"payment method", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"phone number", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"pay using mobile money", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u" i have read and agreed to the websites terms and conditions", None))
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Bamenda", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"southwest", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"centre", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Adamawa", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Goundere", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"yaounde", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Douala", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"proceed to payment", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"products", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"amount", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"total", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.menucheck_out.setTitle(QCoreApplication.translate("MainWindow", u"check out", None))
    # retranslateUi

