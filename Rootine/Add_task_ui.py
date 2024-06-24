# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add_task.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_addtask(object):
    def setupUi(self, addtask):
        if not addtask.objectName():
            addtask.setObjectName(u"addtask")
        addtask.resize(780, 700)
        addtask.setStyleSheet(u"#addtask{\n"
"background-color: #EAE4D6;\n"
"}\n"
"#Title{\n"
"font: 30pt \"High Tower Text\";\n"
"color: #EAE4D6;\n"
"}\n"
"#back{\n"
"background-color: #596020;\n"
"border-radius: 50px;\n"
"}\n"
"#back2{\n"
"background-color: #596020;\n"
"border-radius: 50px;\n"
"}\n"
"#back3{\n"
"background-color: #596020;\n"
"}\n"
"#back4{\n"
"background-color: #EAE4D6;\n"
"border-radius: 50px;\n"
"}\n"
"#back5{\n"
"background-color: #EAE4D6;\n"
"border-radius: 50px;\n"
"}\n"
"#back6{\n"
"background-color:  #EAE4D6;\n"
"border-radius: 20px;\n"
"}\n"
"#title{\n"
"font: 15pt \"Imprint MT Shadow\";\n"
"color: #EAE4D6;\n"
"}\n"
"#note{\n"
"font: 15pt \"Imprint MT Shadow\";\n"
"color: #EAE4D6;\n"
"}\n"
"#tag{\n"
"font: 15pt \"Imprint MT Shadow\";\n"
"color: #EAE4D6;\n"
"}\n"
"#save{\n"
"font: 10pt \"High Tower Text\";\n"
"background-color: #EF8C24;\n"
"border-radius: 10px;\n"
"color: black;\n"
"}\n"
"#undo{\n"
"font: 10pt \"High Tower Text\";\n"
"background-color: #EAE4D6;\n"
"border-radius: 10px;\n"
"color: #black;\n"
"}\n"
"#"
                        "work{\n"
"font: 10pt \"High Tower Text\";\n"
"background-color: #EAE4D6;\n"
"border-radius: 10px;\n"
"color: #black;\n"
"}\n"
"#home{\n"
"font: 10pt \"High Tower Text\";\n"
"background-color: #EAE4D6;\n"
"border-radius: 10px;\n"
"color: #black;\n"
"}\n"
"#errand{\n"
"font: 10pt \"High Tower Text\";\n"
"background-color: #EAE4D6;\n"
"border-radius: 10px;\n"
"color: #black;\n"
"}\n"
"#others{\n"
"font: 10pt \"High Tower Text\";\n"
"background-color: #EAE4D6;\n"
"border-radius: 10px;\n"
"color: #black;\n"
"}\n"
"#titletext{\n"
"border-radius: 10px;\n"
"}\n"
"#notetext{\n"
"border-radius: 10px;\n"
"background-color: white;\n"
"}\n"
"#time{\n"
"border-radius: 10px;\n"
"padding-left: 30px;\n"
"font: 15pt \"Imprint MT Shadow\";\n"
"}\n"
"QDateTimeEdit::drop-down{\n"
"background-color: #CFC9BB;\n"
"border-radius: 10px;\n"
"width: 60px;\n"
"}\n"
"#urgent{\n"
"font: 15pt \"Imprint MT Shadow\";\n"
"color: #EAE4D6;\n"
"}\n"
"#urgent_lev{\n"
"background-color: #EAE4D6;\n"
"font: 18pt \"High Tower Text\";\n"
"border-radius:"
                        " 20px;\n"
"}\n"
"#urgent_lev::hover{\n"
"background-color: #D65151;\n"
"border-radius: 20px;\n"
"}\n"
"#high_lev{\n"
"background-color: #EAE4D6;\n"
"font: 18pt \"High Tower Text\";\n"
"\n"
"border-radius: 20px;\n"
"}\n"
"#high_lev::hover{\n"
"background-color: #EF8C24;\n"
"border-radius: 20px;\n"
"}\n"
"#med_lev{\n"
"background-color: #EAE4D6;\n"
"font: 18pt \"High Tower Text\";\n"
"\n"
"border-radius: 20px;\n"
"}\n"
"#med_lev::hover{\n"
"background-color: #D6CA51;\n"
"border-radius: 20px;\n"
"}\n"
"#low_lev{\n"
"background-color: #EAE4D6;\n"
"font: 18pt \"High Tower Text\";\n"
"\n"
"border-radius: 20px;\n"
"}\n"
"#low_lev::hover{\n"
"background-color: #596020;\n"
"border-radius: 20px;\n"
"}")
        self.Title = QLabel(addtask)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(440, 40, 231, 71))
        self.back = QLabel(addtask)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(280, 0, 541, 701))
        self.back2 = QLabel(addtask)
        self.back2.setObjectName(u"back2")
        self.back2.setGeometry(QRect(10, 180, 411, 371))
        self.back6 = QLabel(addtask)
        self.back6.setObjectName(u"back6")
        self.back6.setGeometry(QRect(60, 280, 211, 201))
        self.back3 = QLabel(addtask)
        self.back3.setObjectName(u"back3")
        self.back3.setGeometry(QRect(210, 130, 411, 471))
        self.back4 = QLabel(addtask)
        self.back4.setObjectName(u"back4")
        self.back4.setGeometry(QRect(60, -11, 221, 191))
        self.back5 = QLabel(addtask)
        self.back5.setObjectName(u"back5")
        self.back5.setGeometry(QRect(60, 551, 221, 191))
        self.save = QPushButton(addtask)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(540, 640, 93, 28))
        font = QFont()
        font.setFamilies([u"High Tower Text"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.save.setFont(font)
        self.undo = QPushButton(addtask)
        self.undo.setObjectName(u"undo")
        self.undo.setGeometry(QRect(660, 640, 93, 28))
        self.time = QDateTimeEdit(addtask)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(380, 170, 371, 71))
        self.time.setCalendarPopup(True)
        self.title = QLabel(addtask)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(350, 310, 71, 31))
        self.note = QLabel(addtask)
        self.note.setObjectName(u"note")
        self.note.setGeometry(QRect(350, 390, 71, 31))
        self.titletext = QLineEdit(addtask)
        self.titletext.setObjectName(u"titletext")
        self.titletext.setGeometry(QRect(440, 310, 311, 31))
        self.notetext = QTextEdit(addtask)
        self.notetext.setObjectName(u"notetext")
        self.notetext.setGeometry(QRect(440, 380, 301, 141))
        self.urgent = QLabel(addtask)
        self.urgent.setObjectName(u"urgent")
        self.urgent.setGeometry(QRect(80, 220, 171, 41))
        self.tag = QLabel(addtask)
        self.tag.setObjectName(u"tag")
        self.tag.setGeometry(QRect(340, 560, 71, 31))
        self.work = QPushButton(addtask)
        self.work.setObjectName(u"work")
        self.work.setGeometry(QRect(430, 560, 71, 28))
        self.home = QPushButton(addtask)
        self.home.setObjectName(u"home")
        self.home.setGeometry(QRect(510, 560, 71, 28))
        self.errand = QPushButton(addtask)
        self.errand.setObjectName(u"errand")
        self.errand.setGeometry(QRect(590, 560, 71, 28))
        self.others = QPushButton(addtask)
        self.others.setObjectName(u"others")
        self.others.setGeometry(QRect(670, 560, 71, 28))
        self.label_3 = QLabel(addtask)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 320, 55, 16))
        self.urgent_lev = QPushButton(addtask)
        self.urgent_lev.setObjectName(u"urgent_lev")
        self.urgent_lev.setGeometry(QRect(60, 280, 211, 50))
        self.high_lev = QPushButton(addtask)
        self.high_lev.setObjectName(u"high_lev")
        self.high_lev.setGeometry(QRect(60, 330, 211, 50))
        self.med_lev = QPushButton(addtask)
        self.med_lev.setObjectName(u"med_lev")
        self.med_lev.setGeometry(QRect(60, 380, 211, 50))
        self.low_lev = QPushButton(addtask)
        self.low_lev.setObjectName(u"low_lev")
        self.low_lev.setGeometry(QRect(60, 430, 211, 50))
        self.label = QLabel(addtask)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(710, 190, 55, 31))
        self.label.setStyleSheet(u"color: white;\n"
"font-size: 30px;")
        self.back.raise_()
        self.back3.raise_()
        self.Title.raise_()
        self.back2.raise_()
        self.back6.raise_()
        self.back4.raise_()
        self.back5.raise_()
        self.save.raise_()
        self.undo.raise_()
        self.time.raise_()
        self.title.raise_()
        self.note.raise_()
        self.titletext.raise_()
        self.notetext.raise_()
        self.urgent.raise_()
        self.tag.raise_()
        self.work.raise_()
        self.home.raise_()
        self.errand.raise_()
        self.others.raise_()
        self.label_3.raise_()
        self.urgent_lev.raise_()
        self.high_lev.raise_()
        self.med_lev.raise_()
        self.low_lev.raise_()
        self.label.raise_()

        self.retranslateUi(addtask)

        QMetaObject.connectSlotsByName(addtask)
    # setupUi

    def retranslateUi(self, addtask):
        addtask.setWindowTitle(QCoreApplication.translate("addtask", u"Form", None))
        self.Title.setText(QCoreApplication.translate("addtask", u"ADD Task", None))
        self.back.setText("")
        self.back2.setText("")
        self.back6.setText("")
        self.back3.setText("")
        self.back4.setText("")
        self.back5.setText("")
        self.save.setText(QCoreApplication.translate("addtask", u"Save", None))
        self.undo.setText(QCoreApplication.translate("addtask", u"Undo", None))
        self.title.setText(QCoreApplication.translate("addtask", u"Title:", None))
        self.note.setText(QCoreApplication.translate("addtask", u"Note:", None))
        self.urgent.setText(QCoreApplication.translate("addtask", u"Urgency Level", None))
        self.tag.setText(QCoreApplication.translate("addtask", u"Tag:", None))
        self.work.setText(QCoreApplication.translate("addtask", u"work", None))
        self.home.setText(QCoreApplication.translate("addtask", u"home", None))
        self.errand.setText(QCoreApplication.translate("addtask", u"errand", None))
        self.others.setText(QCoreApplication.translate("addtask", u"other", None))
        self.label_3.setText("")
        self.urgent_lev.setText(QCoreApplication.translate("addtask", u"Urgent", None))
        self.high_lev.setText(QCoreApplication.translate("addtask", u"High", None))
        self.med_lev.setText(QCoreApplication.translate("addtask", u"Medium", None))
        self.low_lev.setText(QCoreApplication.translate("addtask", u"Low", None))
        self.label.setText(QCoreApplication.translate("addtask", u"V", None))
    # retranslateUi

