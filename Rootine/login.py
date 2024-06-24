# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1080, 700)
        Form.setStyleSheet(u"background-color: #EAE4D6;\n"
"\n"
"")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(121, 70, 600, 530))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-color: white;\n"
"border-top-left-radius: 50px;")
        self.signupSide = QLabel(Form)
        self.signupSide.setObjectName(u"signupSide")
        self.signupSide.setGeometry(QRect(720, 70, 251, 531))
        self.signupSide.setAutoFillBackground(False)
        self.signupSide.setStyleSheet(u"background-color: #D6CA51;\n"
"border-bottom-right-radius: 50px;\n"
"")
        self.signupSide.setPixmap(QPixmap(u"../../../Downloads/sign-up.png"))
        self.signupSide.setScaledContents(True)
        self.loginTitle = QLabel(Form)
        self.loginTitle.setObjectName(u"loginTitle")
        self.loginTitle.setGeometry(QRect(330, 80, 281, 141))
        self.loginTitle.setStyleSheet(u"background-color: white;\n"
"font: 50pt \"Imprint MT Shadow\";\n"
"\n"
"")
        self.textlabel = QLabel(Form)
        self.textlabel.setObjectName(u"textlabel")
        self.textlabel.setGeometry(QRect(200, 220, 131, 31))
        self.textlabel.setStyleSheet(u"background-color: white;\n"
"font: 15pt \"High Tower Text\";")
        self.textlabel2 = QLabel(Form)
        self.textlabel2.setObjectName(u"textlabel2")
        self.textlabel2.setGeometry(QRect(200, 330, 131, 31))
        self.textlabel2.setStyleSheet(u"background-color: white;\n"
"font: 15pt \"High Tower Text\";")
        self.usernameinp = QLineEdit(Form)
        self.usernameinp.setObjectName(u"usernameinp")
        self.usernameinp.setGeometry(QRect(200, 260, 441, 41))
        self.usernameinp.setStyleSheet(u"border-left: 20px solid #EAE4D6;\n"
"border-top: 20px solid #EAE4D6;\n"
"\n"
"background-color: #EAE4D6;\n"
"border-radius: 20px;\n"
"")
        self.passwordinp = QLineEdit(Form)
        self.passwordinp.setObjectName(u"passwordinp")
        self.passwordinp.setGeometry(QRect(200, 370, 441, 41))
        self.passwordinp.setStyleSheet(u"border-left: 20px solid #EAE4D6;\n"
"border-top: 20px solid #EAE4D6;\n"
"\n"
"background-color: #EAE4D6;\n"
"border-radius: 20px;")
        self.showpsw = QCheckBox(Form)
        self.showpsw.setObjectName(u"showpsw")
        self.showpsw.setGeometry(QRect(210, 440, 131, 20))
        self.showpsw.setStyleSheet(u"background-color: white;\n"
"font: 10pt \"High Tower Text\";")
        self.loginbutton = QPushButton(Form)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(210, 490, 93, 28))
        font = QFont()
        font.setFamilies([u"High Tower Text"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.loginbutton.setFont(font)
        self.loginbutton.setStyleSheet(u"background-color: #EF8C24;\n"
"font: 10pt;\n"
"border-radius: 10px;")
        self.signup = QPushButton(Form)
        self.signup.setObjectName(u"signup")
        self.signup.setGeometry(QRect(720, 70, 251, 531))
        self.signup.setFlat(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.signupSide.setText("")
        self.loginTitle.setText(QCoreApplication.translate("Form", u"Login", None))
        self.textlabel.setText(QCoreApplication.translate("Form", u"Username", None))
        self.textlabel2.setText(QCoreApplication.translate("Form", u"Password", None))
        self.showpsw.setText(QCoreApplication.translate("Form", u"Show Password", None))
        self.loginbutton.setText(QCoreApplication.translate("Form", u"Login", None))
        self.signup.setText("")
    # retranslateUi

