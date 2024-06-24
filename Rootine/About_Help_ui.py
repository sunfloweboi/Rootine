# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'About_Help.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_about(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(401, 699)
        Form.setStyleSheet(u"QWidget{\n"
"background-color: rgb(234, 228, 214);\n"
"}\n"
"#Title{\n"
"font: 20pt \"Imprint MT Shadow\";\n"
"\n"
"}\n"
"#Title_2{\n"
"font: 20pt \"Imprint MT Shadow\";\n"
"\n"
"}")
        self.Title_2 = QLabel(Form)
        self.Title_2.setObjectName(u"Title_2")
        self.Title_2.setGeometry(QRect(130, 80, 221, 31))
        self.Title = QLabel(Form)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(40, 300, 191, 51))
        self.label_35 = QLabel(Form)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(-30, -60, 165, 106))
        self.label_35.setStyleSheet(u"background-color: #EF8c24;\n"
"border-radius: 50px;")
        self.label_36 = QLabel(Form)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(-100, -70, 165, 106))
        self.label_36.setStyleSheet(u"background-color: #435d59;\n"
"border-radius: 50px;")
        self.label_37 = QLabel(Form)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(-80, 10, 165, 106))
        self.label_37.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 120, 241, 111))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 360, 361, 141))
        self.label_38 = QLabel(Form)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(310, 570, 141, 101))
        self.label_38.setStyleSheet(u"background-color: #435d59;\n"
"border-radius: 50px;")
        self.label_39 = QLabel(Form)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(240, 620, 165, 106))
        self.label_39.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_40 = QLabel(Form)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(320, 600, 165, 106))
        self.label_40.setStyleSheet(u"background-color: #EF8c24;\n"
"border-radius: 50px;")
        self.Title_2.raise_()
        self.Title.raise_()
        self.label_35.raise_()
        self.label_37.raise_()
        self.label_36.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_38.raise_()
        self.label_39.raise_()
        self.label_40.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Title_2.setText(QCoreApplication.translate("Form", u"Our Developer", None))
        self.Title.setText(QCoreApplication.translate("Form", u"Our Project", None))
        self.label_35.setText("")
#if QT_CONFIG(tooltip)
        self.label_36.setToolTip(QCoreApplication.translate("Form", u"gh", None))
#endif // QT_CONFIG(tooltip)
        self.label_36.setText("")
        self.label_37.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"65011277 Chanasorn Howattanakulphong\n"
"65011320 Kanokjan Singhsuwan\n"
"65011381 Napatr Sapprasert\n"
"", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Our goal is to develop a comprehensive Habit Tracker \n"
" application that empowers users to establish, track, \n"
" and maintain positive habits effectively. This app aims to \n"
" provide a user-friendly interface coupled with a range\n"
" of features to cater to diverse habit-tracking needs.\n"
" The app will use Qt as the interface and ZODB as \n"
" the database with Python as main language.", None))
#if QT_CONFIG(tooltip)
        self.label_38.setToolTip(QCoreApplication.translate("Form", u"gh", None))
#endif // QT_CONFIG(tooltip)
        self.label_38.setText("")
        self.label_39.setText("")
        self.label_40.setText("")
    # retranslateUi

