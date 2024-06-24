# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign-up.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1080, 703)
        Form.setStyleSheet(u"QLineEdit{\n"
"padding-left: 20px;\n"
"}\n"
"QWidget{\n"
"background-color: #EAE4D6;\n"
"}\n"
"")
        self.loginSide = QLabel(Form)
        self.loginSide.setObjectName(u"loginSide")
        self.loginSide.setGeometry(QRect(120, 60, 251, 531))
        self.loginSide.setAutoFillBackground(False)
        self.loginSide.setStyleSheet(u"border-top-left-radius: 20px;\n"
"")
        self.loginSide.setPixmap(QPixmap(u"../../../Downloads/login.png"))
        self.loginSide.setScaledContents(True)
        self.passwordinp = QLineEdit(Form)
        self.passwordinp.setObjectName(u"passwordinp")
        self.passwordinp.setGeometry(QRect(420, 350, 481, 41))
        self.passwordinp.setStyleSheet(u"\n"
"\n"
"background-color: #EAE4D6;\n"
"border-radius: 20px;")
        self.usernameinp = QLineEdit(Form)
        self.usernameinp.setObjectName(u"usernameinp")
        self.usernameinp.setGeometry(QRect(420, 260, 191, 41))
        self.usernameinp.setStyleSheet(u"\n"
"\n"
"background-color: #EAE4D6;\n"
"border-radius: 20px;\n"
"")
        self.signupbutton = QPushButton(Form)
        self.signupbutton.setObjectName(u"signupbutton")
        self.signupbutton.setGeometry(QRect(430, 500, 93, 28))
        font = QFont()
        font.setFamilies([u"High Tower Text"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.signupbutton.setFont(font)
        self.signupbutton.setStyleSheet(u"background-color: #EF8C24;\n"
"font: 10pt;\n"
"border-radius: 10px;")
        self.username = QLabel(Form)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(420, 220, 131, 31))
        self.username.setStyleSheet(u"background-color: #D6CA51;\n"
"font: 15pt \"High Tower Text\";")
        self.password = QLabel(Form)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(420, 320, 181, 31))
        self.password.setStyleSheet(u"background-color: #D6CA51;\n"
"font: 12pt \"High Tower Text\";")
        self.signupTitle = QLabel(Form)
        self.signupTitle.setObjectName(u"signupTitle")
        self.signupTitle.setGeometry(QRect(530, 80, 301, 141))
        self.signupTitle.setStyleSheet(u"background-color: #D6CA51;\n"
"font: 50pt \"Imprint MT Shadow\";\n"
"\n"
"")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(370, 60, 601, 531))
        self.label.setStyleSheet(u"background-color: #D6CA51;\n"
"border-bottom-right-radius: 50px;")
        self.emailinp = QLineEdit(Form)
        self.emailinp.setObjectName(u"emailinp")
        self.emailinp.setGeometry(QRect(640, 260, 271, 41))
        self.emailinp.setStyleSheet(u"\n"
"\n"
"background-color: #EAE4D6;\n"
"border-radius: 20px;\n"
"")
        self.email = QLabel(Form)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(640, 220, 131, 31))
        self.email.setStyleSheet(u"background-color: #D6CA51;\n"
"font: 15pt \"High Tower Text\";")
        self.passwordinp_2 = QLineEdit(Form)
        self.passwordinp_2.setObjectName(u"passwordinp_2")
        self.passwordinp_2.setGeometry(QRect(420, 430, 481, 41))
        self.passwordinp_2.setStyleSheet(u"\n"
"\n"
"background-color: #EAE4D6;\n"
"border-radius: 20px;")
        self.password_2 = QLabel(Form)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setGeometry(QRect(420, 400, 161, 31))
        self.password_2.setStyleSheet(u"background-color: #D6CA51;\n"
"font: 12pt \"High Tower Text\";")
        self.login_btn = QPushButton(Form)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(120, 60, 251, 531))
        self.login_btn.setFlat(True)
        self.label.raise_()
        self.loginSide.raise_()
        self.passwordinp.raise_()
        self.usernameinp.raise_()
        self.signupbutton.raise_()
        self.username.raise_()
        self.password.raise_()
        self.signupTitle.raise_()
        self.emailinp.raise_()
        self.email.raise_()
        self.passwordinp_2.raise_()
        self.password_2.raise_()
        self.login_btn.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.loginSide.setText("")
        self.passwordinp.setText("")
        self.signupbutton.setText(QCoreApplication.translate("Form", u"signup", None))
        self.username.setText(QCoreApplication.translate("Form", u"Username", None))
        self.password.setText(QCoreApplication.translate("Form", u"Create Password", None))
        self.signupTitle.setText(QCoreApplication.translate("Form", u"Sign-up", None))
        self.label.setText("")
        self.email.setText(QCoreApplication.translate("Form", u"Email", None))
        self.password_2.setText(QCoreApplication.translate("Form", u"Re-enter Password", None))
        self.login_btn.setText("")
    # retranslateUi

