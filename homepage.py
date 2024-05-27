
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, Signal,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QScrollBar, QMessageBox, QGroupBox,
    QSizePolicy, QWidget)
import resource_rc
import sqlite3
import resource_rc


class ClickableGroupBox(QGroupBox):
    clicked = Signal()

    def __init__(self, parent=None):
        super(ClickableGroupBox, self).__init__(parent)
       
    def mousePressEvent(self, event):
        self.clicked.emit()
        super(ClickableGroupBox, self).mousePressEvent(event)

class Ui_Homepage(object):
    def setupUi(self, Homepage):
        if not Homepage.objectName():
            Homepage.setObjectName(u"Homepage")
        Homepage.resize(768, 563)
        Homepage.setAutoFillBackground(False)
        Homepage.setStyleSheet(u"font: 9pt \"Arial Rounded MT Bold\";\n"
"background-color: rgb(170, 85, 255);\n"
"center {\n"
"    margin-left: auto;\n"
"    margin-right: auto;\n"
"}\n"
"")
        self.frame = QFrame(Homepage)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 721, 51))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 10, 511, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(590, 10, 41, 31))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"files/003-search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(16, 20))
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(680, 10, 31, 31))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        icon1 = QIcon()
        icon1.addFile(u"files/002-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 10, 91, 31))
        self.comboBox.setStyleSheet(u"background-color: rgb(85, 0, 127);\n"
"image: url(:/pics/files/005-book.png);")
        self.pushButton_12 = QPushButton(self.frame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(640, 10, 31, 31))
        self.pushButton_12.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        icon2 = QIcon()
        icon2.addFile(u":/pics/arrow (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon2)
        self.verticalScrollBar = QScrollBar(Homepage)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(740, 0, 21, 541))
        self.verticalScrollBar.setStyleSheet(u"\n"
"background-color: rgb(85, 0, 127);")
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.groupBox = ClickableGroupBox(Homepage)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 80, 151, 231))
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 30, 101, 101))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet(u"image: url(:/pics/files/coverpage/b201806081528456308.jpg);")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 200, 101, 24))
        self.pushButton.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        icon3 = QIcon()
        icon3.addFile(u"files/001-shopping-cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.widget_22 = QWidget(self.groupBox)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setGeometry(QRect(20, 170, 31, 21))
        self.widget_22.setAutoFillBackground(False)
        self.widget_22.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.widget_23 = QWidget(self.groupBox)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setGeometry(QRect(50, 170, 31, 21))
        self.widget_23.setAutoFillBackground(False)
        self.widget_23.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.widget_48 = QWidget(self.groupBox)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setGeometry(QRect(80, 170, 31, 21))
        self.widget_48.setAutoFillBackground(False)
        self.widget_48.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/rating.png);")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 130, 141, 41))
        self.groupBox_2 = ClickableGroupBox(Homepage)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(180, 80, 141, 231))
        self.widget_4 = QWidget(self.groupBox_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 20, 101, 111))
        self.widget_4.setStyleSheet(u"\n"
"image: url(:/pics/files/coverpage/'Batman 251 by Neal Adams' Poster by DC Comics _ Displate - Copy.jpg);")
        self.pushButton_9 = QPushButton(self.groupBox_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(20, 200, 101, 24))
        self.pushButton_9.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.pushButton_9.setIcon(icon3)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 140, 91, 21))
        self.widget_25 = QWidget(self.groupBox_2)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setGeometry(QRect(20, 170, 31, 21))
        self.widget_25.setAutoFillBackground(False)
        self.widget_25.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.widget_49 = QWidget(self.groupBox_2)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setGeometry(QRect(80, 170, 31, 21))
        self.widget_49.setAutoFillBackground(False)
        self.widget_49.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/rating.png);")
        self.widget_24 = QWidget(self.groupBox_2)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setGeometry(QRect(50, 170, 31, 21))
        self.widget_24.setAutoFillBackground(False)
        self.widget_24.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.groupBox_3 = ClickableGroupBox(Homepage)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(330, 80, 141, 231))
        self.widget_8 = QWidget(self.groupBox_3)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(20, 20, 101, 111))
        self.widget_8.setStyleSheet(u"\n"
"image: url(:/pics/files/coverpage/9781472260086.jpg);")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 140, 101, 21))
        self.widget_29 = QWidget(self.groupBox_3)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setGeometry(QRect(30, 170, 31, 21))
        self.widget_29.setAutoFillBackground(False)
        self.widget_29.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.widget_27 = QWidget(self.groupBox_3)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setGeometry(QRect(60, 170, 31, 21))
        self.widget_27.setAutoFillBackground(False)
        self.widget_27.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.widget_50 = QWidget(self.groupBox_3)
        self.widget_50.setObjectName(u"widget_50")
        self.widget_50.setGeometry(QRect(90, 170, 31, 21))
        self.widget_50.setAutoFillBackground(False)
        self.widget_50.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/rating.png);")
        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 200, 101, 24))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.pushButton_3.setIcon(icon3)
        self.groupBox_4 = ClickableGroupBox(Homepage)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 310, 141, 221))
        self.widget_31 = QWidget(self.groupBox_4)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setGeometry(QRect(40, 160, 31, 21))
        self.widget_31.setAutoFillBackground(False)
        self.widget_31.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.widget_33 = QWidget(self.groupBox_4)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setGeometry(QRect(10, 160, 31, 21))
        self.widget_33.setAutoFillBackground(False)
        self.widget_33.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.widget_3 = QWidget(self.groupBox_4)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 20, 101, 101))
        self.widget_3.setStyleSheet(u"image: url(:/pics/files/coverpage/b201806081528456239.jpg);")
        self.pushButton_7 = QPushButton(self.groupBox_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(10, 190, 101, 24))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.pushButton_7.setIcon(icon3)
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 130, 131, 21))
        self.widget_54 = QWidget(self.groupBox_4)
        self.widget_54.setObjectName(u"widget_54")
        self.widget_54.setGeometry(QRect(70, 160, 31, 21))
        self.widget_54.setAutoFillBackground(False)
        self.widget_54.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/rating.png);")
        self.groupBox_5 = ClickableGroupBox(Homepage)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(180, 320, 131, 211))
        self.widget_34 = QWidget(self.groupBox_5)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setGeometry(QRect(10, 150, 31, 21))
        self.widget_34.setAutoFillBackground(False)
        self.widget_34.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.widget_37 = QWidget(self.widget_34)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setGeometry(QRect(30, -10, 71, 41))
        self.widget_37.setAutoFillBackground(False)
        self.widget_37.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.widget_5 = QWidget(self.groupBox_5)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(10, 20, 101, 101))
        self.widget_5.setStyleSheet(u"\n"
"image: url(:/pics/files/coverpage/5117CIwLSFL._SX331_BO1204203200_.jpg);")
        self.widget_35 = QWidget(self.groupBox_5)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setGeometry(QRect(70, 150, 31, 21))
        self.widget_35.setAutoFillBackground(False)
        self.widget_35.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.pushButton_8 = QPushButton(self.groupBox_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(10, 180, 101, 24))
        self.pushButton_8.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.pushButton_8.setIcon(icon3)
        self.widget_38 = QWidget(self.groupBox_5)
        self.widget_38.setObjectName(u"widget_38")
        self.widget_38.setGeometry(QRect(40, 150, 31, 21))
        self.widget_38.setAutoFillBackground(False)
        self.widget_38.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.widget_39 = QWidget(self.widget_38)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setGeometry(QRect(30, -10, 71, 41))
        self.widget_39.setAutoFillBackground(False)
        self.widget_39.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 120, 111, 21))
        self.groupBox_6 = ClickableGroupBox(Homepage)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(330, 310, 141, 221))
        self.pushButton_1 = QPushButton(self.groupBox_6)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(10, 190, 111, 20))
        self.pushButton_1.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.pushButton_1.setIcon(icon3)
        self.widget_16 = QWidget(self.groupBox_6)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setGeometry(QRect(20, 20, 101, 101))
        self.widget_16.setStyleSheet(u"image: url(:/pics/files/coverpage/b201806111528741778.jpg);")
        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 130, 81, 21))
        self.widget_55 = QWidget(self.groupBox_6)
        self.widget_55.setObjectName(u"widget_55")
        self.widget_55.setGeometry(QRect(60, 160, 31, 21))
        self.widget_55.setAutoFillBackground(False)
        self.widget_55.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/rating.png);")
        self.widget_36 = QWidget(self.groupBox_6)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setGeometry(QRect(30, 160, 31, 21))
        self.widget_36.setAutoFillBackground(False)
        self.widget_36.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.widget_56 = QWidget(self.groupBox_6)
        self.widget_56.setObjectName(u"widget_56")
        self.widget_56.setGeometry(QRect(90, 160, 31, 21))
        self.widget_56.setAutoFillBackground(False)
        self.widget_56.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/rating.png);")
        self.groupBox_7 = ClickableGroupBox(Homepage)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(480, 80, 120, 231))
        self.widget_6 = QWidget(self.groupBox_7)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(10, 20, 101, 101))
        self.widget_6.setStyleSheet(u"image: url(:/pics/files/coverpage/Atomic Habits.jpg);")
        self.widget_28 = QWidget(self.groupBox_7)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setGeometry(QRect(20, 170, 31, 21))
        self.widget_28.setAutoFillBackground(False)
        self.widget_28.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.widget_26 = QWidget(self.groupBox_7)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setGeometry(QRect(50, 170, 31, 21))
        self.widget_26.setAutoFillBackground(False)
        self.widget_26.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.pushButton_5 = QPushButton(self.groupBox_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 200, 101, 24))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.pushButton_5.setIcon(icon3)
        self.label_4 = QLabel(self.groupBox_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 130, 81, 31))
        self.widget_51 = QWidget(self.groupBox_7)
        self.widget_51.setObjectName(u"widget_51")
        self.widget_51.setGeometry(QRect(80, 170, 31, 21))
        self.widget_51.setAutoFillBackground(False)
        self.widget_51.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/rating.png);")
        self.groupBox_8 = ClickableGroupBox(Homepage)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(610, 80, 120, 231))
        self.widget_30 = QWidget(self.groupBox_8)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setGeometry(QRect(10, 170, 31, 21))
        self.widget_30.setAutoFillBackground(False)
        self.widget_30.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.widget_7 = QWidget(self.groupBox_8)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(10, 30, 101, 101))
        self.widget_7.setStyleSheet(u"image: url(:/pics/files/category/Beauty and the Beast (Classic Reprint).jpg);")
        self.label_5 = QLabel(self.groupBox_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 130, 111, 21))
        self.widget_52 = QWidget(self.groupBox_8)
        self.widget_52.setObjectName(u"widget_52")
        self.widget_52.setGeometry(QRect(70, 170, 31, 21))
        self.widget_52.setAutoFillBackground(False)
        self.widget_52.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.widget_32 = QWidget(self.groupBox_8)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setGeometry(QRect(40, 170, 31, 21))
        self.widget_32.setAutoFillBackground(False)
        self.widget_32.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.pushButton_6 = QPushButton(self.groupBox_8)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(10, 200, 101, 24))
        self.pushButton_6.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.pushButton_6.setIcon(icon3)
        self.groupBox_9 = ClickableGroupBox(Homepage)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(480, 310, 120, 221))
        self.widget_57 = QWidget(self.groupBox_9)
        self.widget_57.setObjectName(u"widget_57")
        self.widget_57.setGeometry(QRect(50, 160, 31, 21))
        self.widget_57.setAutoFillBackground(False)
        self.widget_57.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/rating.png);")
        self.widget_58 = QWidget(self.groupBox_9)
        self.widget_58.setObjectName(u"widget_58")
        self.widget_58.setGeometry(QRect(80, 160, 31, 21))
        self.widget_58.setAutoFillBackground(False)
        self.widget_58.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/rating.png);")
        self.widget_40 = QWidget(self.groupBox_9)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setGeometry(QRect(10, 160, 31, 21))
        self.widget_40.setAutoFillBackground(False)
        self.widget_40.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.widget_41 = QWidget(self.widget_40)
        self.widget_41.setObjectName(u"widget_41")
        self.widget_41.setGeometry(QRect(30, -10, 71, 41))
        self.widget_41.setAutoFillBackground(False)
        self.widget_41.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.pushButton_10 = QPushButton(self.groupBox_9)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(10, 190, 101, 24))
        self.pushButton_10.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.pushButton_10.setIcon(icon3)
        self.widget_17 = QWidget(self.groupBox_9)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setGeometry(QRect(10, 30, 101, 101))
        self.widget_17.setStyleSheet(u"\n"
"image: url(:/pics/files/coverpage/513e7BP39PL._SX330_BO1204203200_.jpg);")
        self.label_9 = QLabel(self.groupBox_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 130, 121, 21))
        self.groupBox_10 = ClickableGroupBox(Homepage)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(610, 320, 120, 211))
        self.widget_18 = QWidget(self.groupBox_10)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setGeometry(QRect(10, 20, 101, 101))
        self.widget_18.setStyleSheet(u"image: url(:/pics/files/coverpage/41UwqWhI4L._SX329_BO1204203200_.jpg);")
        self.widget_46 = QWidget(self.groupBox_10)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setGeometry(QRect(20, 150, 31, 21))
        self.widget_46.setAutoFillBackground(False)
        self.widget_46.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.widget_47 = QWidget(self.widget_46)
        self.widget_47.setObjectName(u"widget_47")
        self.widget_47.setGeometry(QRect(30, -10, 71, 41))
        self.widget_47.setAutoFillBackground(False)
        self.widget_47.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.pushButton_11 = QPushButton(self.groupBox_10)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(10, 180, 101, 24))
        self.pushButton_11.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.pushButton_11.setIcon(icon3)
        self.widget_53 = QWidget(self.groupBox_10)
        self.widget_53.setObjectName(u"widget_53")
        self.widget_53.setGeometry(QRect(80, 150, 31, 21))
        self.widget_53.setAutoFillBackground(False)
        self.widget_53.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.label_1 = QLabel(self.groupBox_10)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(20, 120, 91, 21))
        self.widget_44 = QWidget(self.groupBox_10)
        self.widget_44.setObjectName(u"widget_44")
        self.widget_44.setGeometry(QRect(50, 150, 31, 21))
        self.widget_44.setAutoFillBackground(False)
        self.widget_44.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
        self.widget_45 = QWidget(self.widget_44)
        self.widget_45.setObjectName(u"widget_45")
        self.widget_45.setGeometry(QRect(30, -10, 71, 41))
        self.widget_45.setAutoFillBackground(False)
        self.widget_45.setStyleSheet(u"background-color: rgb(170, 85, 255);\n"
"image: url(:/pics/star.png);")
          
        self.pushButton_4.clicked.connect(self.handle_search)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.comboBox.currentIndexChanged.connect(self.filter_by_genre)
        self.pushButton_12.clicked.connect(self.refresh_homepage) 

        self.retranslateUi(Homepage)

        QMetaObject.connectSlotsByName(Homepage)
    # setupUi

    def retranslateUi(self, Homepage):
        Homepage.setWindowTitle(QCoreApplication.translate("Homepage", u"Dialog", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Homepage", u"Search for the book Nerd", None))
        self.pushButton_4.setText("")
        self.pushButton_2.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("Homepage", u"Genre", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Homepage", u"Academics", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Homepage", u"Money", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Homepage", u"Classic", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Homepage", u"Selfhelp", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("Homepage", u"Genre", None))
        self.pushButton_12.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Homepage", u"GroupBox", None))
#if QT_CONFIG(whatsthis)
        self.widget.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("Homepage", u"O.O.Programming C++", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Homepage", u"GroupBox", None))
        self.pushButton_9.setText("")
        self.label_2.setText(QCoreApplication.translate("Homepage", u"BatMan Comics", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Homepage", u"GroupBox", None))
        self.label_3.setText(QCoreApplication.translate("Homepage", u"Art Matters", None))
        self.pushButton_3.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("Homepage", u"GroupBox", None))
        self.pushButton_7.setText("")
        self.label_6.setText(QCoreApplication.translate("Homepage", u"Discrete Mathematics", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Homepage", u"GroupBox", None))
        self.pushButton_8.setText("")
        self.label_7.setText(QCoreApplication.translate("Homepage", u"Money and Wealth", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Homepage", u"GroupBox", None))
        self.pushButton_1.setText("")
        self.label_8.setText(QCoreApplication.translate("Homepage", u"Think Python", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Homepage", u"GroupBox", None))
        self.pushButton_5.setText("")
        self.label_4.setText(QCoreApplication.translate("Homepage", u"Atomic Habits", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Homepage", u"GroupBox", None))
        self.label_5.setText(QCoreApplication.translate("Homepage", u"Beauty and Beast", None))
        self.pushButton_6.setText("")
        self.groupBox_9.setTitle(QCoreApplication.translate("Homepage", u"GroupBox", None))
        self.pushButton_10.setText("")
        self.label_9.setText(QCoreApplication.translate("Homepage", u"Intelligent Investor", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("Homepage", u"GroupBox", None))
        self.pushButton_11.setText("")
        self.label_1.setText(QCoreApplication.translate("Homepage", u"Power of Zero", None))
    # retranslateUi
      
    def handle_search(self):
        self.conn = sqlite3.connect('Book.db')
        self.cursor = self.conn.cursor()
        search_text = self.lineEdit_2.text()

        # Perform the database query to search for the book
        self.cursor.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + search_text + '%',))

        book_details = self.cursor.fetchone()

        if book_details:
                # Assuming the 'groupbox' column is the third column in your query result
                group_box_name = book_details[6]  # Adjust index based on your actual column order
                # List of all group boxes
                group_boxes = [
                self.groupBox, self.groupBox_2, self.groupBox_3, self.groupBox_4,
                self.groupBox_5, self.groupBox_6, self.groupBox_7, self.groupBox_8,
                self.groupBox_9, self.groupBox_10
                ]
                for group_box in group_boxes:
                        if group_box.objectName() == group_box_name:
                                #group_box.setGeometry(100, 70, group_box.width(), group_box.height())
                                group_box.show()
                        else:
                                group_box.hide()
        else:
                # If no book found, display a message to the user
                QMessageBox.information(self, "Search Result", "No book found with that title.")
    
    def filter_by_genre(self):
        # Connect to the database
        self.conn = sqlite3.connect('Book.db')
        self.cursor = self.conn.cursor()

        # Get the selected genre from the combo box
        selected_genre = self.comboBox.currentText()

        # Perform the database query to search for books with the selected genre
        self.cursor.execute("SELECT * FROM books WHERE genre LIKE ?", ('%' + selected_genre + '%',))
        book_details = self.cursor.fetchall()

        # Define group boxes
        group_boxes = {
                "groupBox": self.groupBox, 
                "groupBox_2": self.groupBox_2, 
                "groupBox_3": self.groupBox_3, 
                "groupBox_4": self.groupBox_4,
                "groupBox_5": self.groupBox_5, 
                "groupBox_6": self.groupBox_6, 
                "groupBox_7": self.groupBox_7, 
                "groupBox_8": self.groupBox_8,
                "groupBox_9": self.groupBox_9, 
                "groupBox_10": self.groupBox_10
        }

        # Hide all group boxes initially
        for group_box in group_boxes.values():
                group_box.hide()

        # Check if any book details were found
        if book_details:
                # Show the relevant group boxes based on the genre
                for book in book_details:
                        group_box_name = book[6]  # Assuming group_box_name is the 7th field in the table
                        if group_box_name in group_boxes:
                                group_box = group_boxes[group_box_name]
                              #  group_box.setGeometry(100, 70, group_box.width(), group_box.height())
                                group_box.show()
        else:
                # If no book found, display a message to the user
                QMessageBox.information(self, "Search Result", "No book found with that genre.")

        # Close the database connection
        self.conn.close()
        
    def refresh_homepage(self):
        # Define group boxes
        group_boxes = {
            "groupBox": self.groupBox, 
            "groupBox_2": self.groupBox_2, 
            "groupBox_3": self.groupBox_3, 
            "groupBox_4": self.groupBox_4,
            "groupBox_5": self.groupBox_5, 
            "groupBox_6": self.groupBox_6, 
            "groupBox_7": self.groupBox_7, 
            "groupBox_8": self.groupBox_8,
            "groupBox_9": self.groupBox_9, 
            "groupBox_10": self.groupBox_10
        }

        # Show all group boxes without changing their position
        for group_box in group_boxes.values():
            group_box.show()
   