# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Edit_habit.ui'
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

class Ui_edit_habit(object):
    def setupUi(self, edit_habit):
        if not edit_habit.objectName():
            edit_habit.setObjectName(u"edit_habit")
        edit_habit.resize(780, 700)
        edit_habit.setStyleSheet(u"#edit_habit{\n"
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
"color: #EAE4D6"
                        "\n"
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
"#delete_2{\n"
"font: 10pt \"MS Serif\";\n"
"background-color: red;\n"
"border-radius: 10px;\n"
"color: white;\n"
"}\n"
"#undo{\n"
"font: 10pt \"MS Serif\";\n"
"background-color: #596020;\n"
"border-radius: 10px;\n"
"color: #EAE4D6;\n"
"}\n"
"#titletext{\n"
"bor"
                        "der-radius: 10px;\n"
"}\n"
"#notetext{\n"
"border-radius: 10px;\n"
"background-color: white;}\n"
"#time{\n"
"border-radius: 30px;\n"
"padding-left: 20px;\n"
"font: 20pt \"Imprint MT Shadow\";\n"
"}\n"
"QTimeEdit::down-button, QTimeEdit::up-button{\n"
"border: 1px solid white;\n"
"background-color: #596020;\n"
"border-radius: 23px;\n"
"}")
        self.Title = QLabel(edit_habit)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(380, 60, 341, 71))
        font = QFont()
        font.setFamilies([u"High Tower Text"])
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        self.Title.setFont(font)
        self.wed = QPushButton(edit_habit)
        self.wed.setObjectName(u"wed")
        self.wed.setGeometry(QRect(40, 340, 93, 40))
        self.mon = QPushButton(edit_habit)
        self.mon.setObjectName(u"mon")
        self.mon.setGeometry(QRect(60, 280, 93, 40))
        self.every = QPushButton(edit_habit)
        self.every.setObjectName(u"every")
        self.every.setGeometry(QRect(160, 460, 93, 40))
        self.back_4 = QLabel(edit_habit)
        self.back_4.setObjectName(u"back_4")
        self.back_4.setGeometry(QRect(20, -11, 261, 191))
        self.back_4.setSizeIncrement(QSize(0, 0))
        self.titletext = QLineEdit(edit_habit)
        self.titletext.setObjectName(u"titletext")
        self.titletext.setGeometry(QRect(440, 220, 311, 31))
        self.notetext = QTextEdit(edit_habit)
        self.notetext.setObjectName(u"notetext")
        self.notetext.setEnabled(True)
        self.notetext.setGeometry(QRect(440, 330, 321, 261))
        self.note = QLabel(edit_habit)
        self.note.setObjectName(u"note")
        self.note.setGeometry(QRect(360, 320, 61, 31))
        self.back = QLabel(edit_habit)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(280, 0, 541, 701))
        self.day = QLabel(edit_habit)
        self.day.setObjectName(u"day")
        self.day.setGeometry(QRect(100, 200, 131, 41))
        self.thurs = QPushButton(edit_habit)
        self.thurs.setObjectName(u"thurs")
        self.thurs.setGeometry(QRect(160, 340, 93, 40))
        self.sat = QPushButton(edit_habit)
        self.sat.setObjectName(u"sat")
        self.sat.setGeometry(QRect(180, 400, 93, 40))
        self.title = QLabel(edit_habit)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(360, 220, 71, 31))
        self.fri = QPushButton(edit_habit)
        self.fri.setObjectName(u"fri")
        self.fri.setGeometry(QRect(60, 400, 93, 40))
        self.save = QPushButton(edit_habit)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(540, 650, 93, 28))
        font1 = QFont()
        font1.setFamilies([u"MS Serif"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.save.setFont(font1)
        self.sun = QPushButton(edit_habit)
        self.sun.setObjectName(u"sun")
        self.sun.setGeometry(QRect(40, 460, 93, 40))
        self.tues = QPushButton(edit_habit)
        self.tues.setObjectName(u"tues")
        self.tues.setGeometry(QRect(180, 280, 93, 40))
        self.undo = QPushButton(edit_habit)
        self.undo.setObjectName(u"undo")
        self.undo.setGeometry(QRect(660, 650, 93, 28))
        self.back_5 = QLabel(edit_habit)
        self.back_5.setObjectName(u"back_5")
        self.back_5.setGeometry(QRect(20, 551, 261, 169))
        self.back_2 = QLabel(edit_habit)
        self.back_2.setObjectName(u"back_2")
        self.back_2.setGeometry(QRect(10, 180, 411, 371))
        self.back_3 = QLabel(edit_habit)
        self.back_3.setObjectName(u"back_3")
        self.back_3.setGeometry(QRect(230, 120, 411, 491))
        self.delete_2 = QPushButton(edit_habit)
        self.delete_2.setObjectName(u"delete_2")
        self.delete_2.setGeometry(QRect(420, 650, 93, 28))
        self.delete_2.setFont(font1)
        self.back.raise_()
        self.back_2.raise_()
        self.back_3.raise_()
        self.Title.raise_()
        self.wed.raise_()
        self.mon.raise_()
        self.every.raise_()
        self.back_4.raise_()
        self.titletext.raise_()
        self.notetext.raise_()
        self.note.raise_()
        self.day.raise_()
        self.thurs.raise_()
        self.sat.raise_()
        self.title.raise_()
        self.fri.raise_()
        self.save.raise_()
        self.sun.raise_()
        self.tues.raise_()
        self.undo.raise_()
        self.back_5.raise_()
        self.delete_2.raise_()

        self.retranslateUi(edit_habit)

        QMetaObject.connectSlotsByName(edit_habit)
    # setupUi

    def retranslateUi(self, edit_habit):
        edit_habit.setWindowTitle(QCoreApplication.translate("edit_habit", u"Form", None))
        self.Title.setText(QCoreApplication.translate("edit_habit", u"Edit Habit", None))
        self.wed.setText(QCoreApplication.translate("edit_habit", u"Wednesday", None))
        self.mon.setText(QCoreApplication.translate("edit_habit", u"Monday", None))
        self.every.setText(QCoreApplication.translate("edit_habit", u"Everyday", None))
        self.back_4.setText("")
        self.note.setText(QCoreApplication.translate("edit_habit", u"Note:", None))
        self.back.setText("")
        self.day.setText(QCoreApplication.translate("edit_habit", u"Active Day:", None))
        self.thurs.setText(QCoreApplication.translate("edit_habit", u"Thursday", None))
        self.sat.setText(QCoreApplication.translate("edit_habit", u"Saturday", None))
        self.title.setText(QCoreApplication.translate("edit_habit", u"Title:", None))
        self.fri.setText(QCoreApplication.translate("edit_habit", u"Friday", None))
        self.save.setText(QCoreApplication.translate("edit_habit", u"Save", None))
        self.sun.setText(QCoreApplication.translate("edit_habit", u"Sunday", None))
        self.tues.setText(QCoreApplication.translate("edit_habit", u"Tuesday", None))
        self.undo.setText(QCoreApplication.translate("edit_habit", u"Undo", None))
        self.back_5.setText("")
        self.back_2.setText("")
        self.back_3.setText("")
        self.delete_2.setText(QCoreApplication.translate("edit_habit", u"Delete", None))
    # retranslateUi

