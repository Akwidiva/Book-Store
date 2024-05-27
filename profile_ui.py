# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profileRdfeOP.ui'
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

class Ui_profile(object):
    def setupUi(self, profile):
        if not profile.objectName():
            profile.setObjectName(u"profile")
        profile.resize(336, 213)
        profile.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.pushButton = QPushButton(profile)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 30, 211, 41))
        self.pushButton.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.pushButton_2 = QPushButton(profile)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 90, 211, 41))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.pushButton_3 = QPushButton(profile)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(60, 140, 211, 41))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(85, 0, 127);")

        self.retranslateUi(profile)

        QMetaObject.connectSlotsByName(profile)
    # setupUi

    def retranslateUi(self, profile):
        profile.setWindowTitle(QCoreApplication.translate("profile", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("profile", u"Register/Login", None))
        self.pushButton_2.setText(QCoreApplication.translate("profile", u"Cart", None))
        self.pushButton_3.setText(QCoreApplication.translate("profile", u"Store", None))
    # retranslateUi
