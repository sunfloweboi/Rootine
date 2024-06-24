# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add_habbit.ui'
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
    QSizePolicy, QTextEdit, QWidget)

class Ui_addhabbit(object):
    def setupUi(self, addhabbit):
        if not addhabbit.objectName():
            addhabbit.setObjectName(u"addhabbit")
        addhabbit.resize(780, 700)
        font = QFont()
        font.setFamilies([u"MS Serif"])
        font.setBold(True)
        font.setItalic(False)
        addhabbit.setFont(font)
        addhabbit.setStyleSheet(u"#addhabbit{\n"
"background-color: #596020;\n"
"}\n"
"#Title{\n"
"font: 40pt \"High Tower Text\";\n"
"color: #596020;\n"
"}\n"
"#back{\n"
"background-color: #EAE4D6;\n"
"border-radius: 50px;\n"
"}\n"
"#back_2{\n"
"background-color: #EAE4D6;\n"
"border-radius: 50px;\n"
"}\n"
"#back_3{\n"
"background-color: #EAE4D6;\n"
"}\n"
"#back_4{\n"
"background-color: #596020;\n"
"border-radius: 50px;\n"
"}\n"
"#back_5{\n"
"background-color: #596020;\n"
"border-radius: 50px;\n"
"}\n"
"#day{\n"
"font: 15pt \"Imprint MT Shadow\";\n"
"color: #596020;\n"
"}\n"
"#mon{\n"
"font: 10pt \"MS Serif\";\n"
"background-color: #596020;\n"
"border-radius: 20px;\n"
"color: #EAE4D6;\n"
"}\n"
"#tues{\n"
"font: 10pt \"MS Serif\";\n"
"background-color: #596020;\n"
"border-radius: 20px;\n"
"color: #EAE4D6;\n"
"}\n"
"#wed{\n"
"font: 10pt \"MS Serif\";\n"
"background-color: #596020;\n"
"border-radius: 20px;\n"
"color: #EAE4D6;\n"
"}\n"
"#thurs{\n"
"font: 10pt \"MS Serif\";\n"
"background-color: #596020;\n"
"border-radius: 20px;\n"
"color: #EAE4D6\n"
""
                        "}\n"
"#fri{\n"
"font: 10pt \"MS Serif\";\n"
"background-color: #596020;\n"
"border-radius: 20px;\n"
"color: #EAE4D6\n"
"}\n"
"#sat{\n"
"font: 10pt \"MS Serif\";\n"
"background-color: #596020;\n"
"border-radius: 20px;\n"
"color: #EAE4D6\n"
"}\n"
"#sun{\n"
"font: 10pt \"MS Serif\";\n"
"background-color: #596020;\n"
"border-radius: 20px;\n"
"color: #EAE4D6\n"
"}\n"
"#every{\n"
"font: 10pt \"MS Serif\";\n"
"background-color: #596020;\n"
"border-radius: 20px;\n"
"color: #EAE4D6\n"
"}\n"
"#title{\n"
"font: 15pt \"Imprint MT Shadow\";\n"
"color: #596020;\n"
"}\n"
"#note{\n"
"font: 15pt \"Imprint MT Shadow\";\n"
"color: #596020;\n"
"}\n"
"#save{\n"
"font: 10pt \"MS Serif\";\n"
"background-color: #EF8C24;\n"
"border-radius: 10px;\n"
"color: black;\n"
"}\n"
"#undo{\n"
"font: 10pt \"MS Serif\";\n"
"background-color: #596020;\n"
"border-radius: 10px;\n"
"color: #EAE4D6;\n"
"}\n"
"#titletext{\n"
"border-radius: 10px;\n"
"}\n"
"#notetext{\n"
"border-radius: 10px;\n"
"background-color: white;}\n"
"#time{\n"
"border-radius: 3"
                        "0px;\n"
"padding-left: 20px;\n"
"font: 20pt \"Imprint MT Shadow\";\n"
"}\n"
"QTimeEdit::down-button, QTimeEdit::up-button{\n"
"border: 1px solid white;\n"
"background-color: #596020;\n"
"border-radius: 23px;\n"
"}")
        self.back = QLabel(addhabbit)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(280, 0, 541, 701))
        self.back_2 = QLabel(addhabbit)
        self.back_2.setObjectName(u"back_2")
        self.back_2.setGeometry(QRect(10, 180, 411, 371))
        self.back_3 = QLabel(addhabbit)
        self.back_3.setObjectName(u"back_3")
        self.back_3.setGeometry(QRect(230, 120, 411, 491))
        self.back_4 = QLabel(addhabbit)
        self.back_4.setObjectName(u"back_4")
        self.back_4.setGeometry(QRect(20, -11, 261, 191))
        self.back_4.setSizeIncrement(QSize(0, 0))
        self.back_5 = QLabel(addhabbit)
        self.back_5.setObjectName(u"back_5")
        self.back_5.setGeometry(QRect(20, 551, 261, 169))
        self.Title = QLabel(addhabbit)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(380, 60, 341, 71))
        font1 = QFont()
        font1.setFamilies([u"High Tower Text"])
        font1.setPointSize(40)
        font1.setBold(False)
        font1.setItalic(False)
        self.Title.setFont(font1)
        self.day = QLabel(addhabbit)
        self.day.setObjectName(u"day")
        self.day.setGeometry(QRect(100, 200, 131, 41))
        self.mon = QPushButton(addhabbit)
        self.mon.setObjectName(u"mon")
        self.mon.setGeometry(QRect(60, 280, 93, 40))
        self.tues = QPushButton(addhabbit)
        self.tues.setObjectName(u"tues")
        self.tues.setGeometry(QRect(180, 280, 93, 40))
        self.thurs = QPushButton(addhabbit)
        self.thurs.setObjectName(u"thurs")
        self.thurs.setGeometry(QRect(160, 340, 93, 40))
        self.wed = QPushButton(addhabbit)
        self.wed.setObjectName(u"wed")
        self.wed.setGeometry(QRect(40, 340, 93, 40))
        self.sat = QPushButton(addhabbit)
        self.sat.setObjectName(u"sat")
        self.sat.setGeometry(QRect(180, 400, 93, 40))
        self.fri = QPushButton(addhabbit)
        self.fri.setObjectName(u"fri")
        self.fri.setGeometry(QRect(60, 400, 93, 40))
        self.sun = QPushButton(addhabbit)
        self.sun.setObjectName(u"sun")
        self.sun.setGeometry(QRect(40, 460, 93, 40))
        self.every = QPushButton(addhabbit)
        self.every.setObjectName(u"every")
        self.every.setGeometry(QRect(160, 460, 93, 40))
        self.title = QLabel(addhabbit)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(360, 220, 71, 31))
        self.note = QLabel(addhabbit)
        self.note.setObjectName(u"note")
        self.note.setGeometry(QRect(360, 320, 61, 31))
        self.titletext = QLineEdit(addhabbit)
        self.titletext.setObjectName(u"titletext")
        self.titletext.setGeometry(QRect(440, 220, 311, 31))
        self.notetext = QTextEdit(addhabbit)
        self.notetext.setObjectName(u"notetext")
        self.notetext.setEnabled(True)
        self.notetext.setGeometry(QRect(440, 330, 321, 261))
        self.save = QPushButton(addhabbit)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(540, 650, 93, 28))
        font2 = QFont()
        font2.setFamilies([u"MS Serif"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.save.setFont(font2)
        self.undo = QPushButton(addhabbit)
        self.undo.setObjectName(u"undo")
        self.undo.setGeometry(QRect(660, 650, 93, 28))
        self.back_3.raise_()
        self.back.raise_()
        self.back_2.raise_()
        self.back_4.raise_()
        self.back_5.raise_()
        self.Title.raise_()
        self.day.raise_()
        self.mon.raise_()
        self.tues.raise_()
        self.thurs.raise_()
        self.wed.raise_()
        self.sat.raise_()
        self.fri.raise_()
        self.sun.raise_()
        self.every.raise_()
        self.title.raise_()
        self.note.raise_()
        self.titletext.raise_()
        self.notetext.raise_()
        self.save.raise_()
        self.undo.raise_()

        self.retranslateUi(addhabbit)

        QMetaObject.connectSlotsByName(addhabbit)
    # setupUi

    def retranslateUi(self, addhabbit):
        addhabbit.setWindowTitle(QCoreApplication.translate("addhabbit", u"Form", None))
        self.back.setText("")
        self.back_2.setText("")
        self.back_3.setText("")
        self.back_4.setText("")
        self.back_5.setText("")
        self.Title.setText(QCoreApplication.translate("addhabbit", u"ADD Habit", None))
        self.day.setText(QCoreApplication.translate("addhabbit", u"Active Day:", None))
        self.mon.setText(QCoreApplication.translate("addhabbit", u"Monday", None))
        self.tues.setText(QCoreApplication.translate("addhabbit", u"Tuesday", None))
        self.thurs.setText(QCoreApplication.translate("addhabbit", u"Thursday", None))
        self.wed.setText(QCoreApplication.translate("addhabbit", u"Wednesday", None))
        self.sat.setText(QCoreApplication.translate("addhabbit", u"Saturday", None))
        self.fri.setText(QCoreApplication.translate("addhabbit", u"Friday", None))
        self.sun.setText(QCoreApplication.translate("addhabbit", u"Sunday", None))
        self.every.setText(QCoreApplication.translate("addhabbit", u"Everyday", None))
        self.title.setText(QCoreApplication.translate("addhabbit", u"Title:", None))
        self.note.setText(QCoreApplication.translate("addhabbit", u"Note:", None))
        self.save.setText(QCoreApplication.translate("addhabbit", u"Save", None))
        self.undo.setText(QCoreApplication.translate("addhabbit", u"Undo", None))
    # retranslateUi

