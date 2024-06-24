# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Edit_task.ui'
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

class Ui_edittask(object):
    def setupUi(self, edittask):
        if not edittask.objectName():
            edittask.setObjectName(u"edittask")
        edittask.resize(780, 700)
        edittask.setStyleSheet(u"#edittask{\n"
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
""
                        "#work{\n"
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
"border-radius"
                        ": 20px;\n"
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
"border-radius: 20px;\n"
"}\n"
"#low_lev::hover{\n"
"background-color: #596020;\n"
"border-radius: 20px;\n"
"}\n"
"#dele{\n"
"font: 10pt \"MS Serif\";\n"
"background-color: red;\n"
"border-radius: 10px;\n"
"color: white;\n"
"}")
        self.urgent_lev = QPushButton(edittask)
        self.urgent_lev.setObjectName(u"urgent_lev")
        self.urgent_lev.setGeometry(QRect(60, 290, 211, 50))
        self.label_3 = QLabel(edittask)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 330, 55, 16))
        self.med_lev = QPushButton(edittask)
        self.med_lev.setObjectName(u"med_lev")
        self.med_lev.setGeometry(QRect(60, 390, 211, 50))
        self.note = QLabel(edittask)
        self.note.setObjectName(u"note")
        self.note.setGeometry(QRect(350, 400, 71, 31))
        self.urgent = QLabel(edittask)
        self.urgent.setObjectName(u"urgent")
        self.urgent.setGeometry(QRect(80, 230, 171, 41))
        self.low_lev = QPushButton(edittask)
        self.low_lev.setObjectName(u"low_lev")
        self.low_lev.setGeometry(QRect(60, 440, 211, 50))
        self.back6 = QLabel(edittask)
        self.back6.setObjectName(u"back6")
        self.back6.setGeometry(QRect(60, 290, 211, 201))
        self.home = QPushButton(edittask)
        self.home.setObjectName(u"home")
        self.home.setGeometry(QRect(510, 570, 71, 28))
        self.notetext = QTextEdit(edittask)
        self.notetext.setObjectName(u"notetext")
        self.notetext.setGeometry(QRect(440, 390, 301, 141))
        self.save = QPushButton(edittask)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(540, 650, 93, 28))
        font = QFont()
        font.setFamilies([u"High Tower Text"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.save.setFont(font)
        self.errand = QPushButton(edittask)
        self.errand.setObjectName(u"errand")
        self.errand.setGeometry(QRect(590, 570, 71, 28))
        self.work = QPushButton(edittask)
        self.work.setObjectName(u"work")
        self.work.setGeometry(QRect(430, 570, 71, 28))
        self.time = QDateTimeEdit(edittask)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(380, 180, 371, 71))
        self.time.setCalendarPopup(True)
        self.Title = QLabel(edittask)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(440, 50, 231, 71))
        self.back = QLabel(edittask)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(280, 10, 541, 701))
        self.others = QPushButton(edittask)
        self.others.setObjectName(u"others")
        self.others.setGeometry(QRect(670, 570, 71, 28))
        self.back5 = QLabel(edittask)
        self.back5.setObjectName(u"back5")
        self.back5.setGeometry(QRect(60, 561, 221, 191))
        self.tag = QLabel(edittask)
        self.tag.setObjectName(u"tag")
        self.tag.setGeometry(QRect(340, 570, 71, 31))
        self.back4 = QLabel(edittask)
        self.back4.setObjectName(u"back4")
        self.back4.setGeometry(QRect(60, -1, 221, 191))
        self.back2 = QLabel(edittask)
        self.back2.setObjectName(u"back2")
        self.back2.setGeometry(QRect(10, 190, 411, 371))
        self.undo = QPushButton(edittask)
        self.undo.setObjectName(u"undo")
        self.undo.setGeometry(QRect(660, 650, 93, 28))
        self.title = QLabel(edittask)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(350, 320, 71, 31))
        self.titletext = QLineEdit(edittask)
        self.titletext.setObjectName(u"titletext")
        self.titletext.setGeometry(QRect(440, 320, 311, 31))
        self.high_lev = QPushButton(edittask)
        self.high_lev.setObjectName(u"high_lev")
        self.high_lev.setGeometry(QRect(60, 340, 211, 50))
        self.back3 = QLabel(edittask)
        self.back3.setObjectName(u"back3")
        self.back3.setGeometry(QRect(210, 140, 411, 471))
        self.dele = QPushButton(edittask)
        self.dele.setObjectName(u"dele")
        self.dele.setGeometry(QRect(420, 650, 93, 28))
        font1 = QFont()
        font1.setFamilies([u"MS Serif"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.dele.setFont(font1)
        self.label = QLabel(edittask)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(710, 200, 55, 31))
        self.label.setStyleSheet(u"color: white;\n"
"font-size: 30px;")
        self.back3.raise_()
        self.back2.raise_()
        self.back6.raise_()
        self.back.raise_()
        self.urgent_lev.raise_()
        self.label_3.raise_()
        self.med_lev.raise_()
        self.note.raise_()
        self.urgent.raise_()
        self.low_lev.raise_()
        self.home.raise_()
        self.notetext.raise_()
        self.save.raise_()
        self.errand.raise_()
        self.work.raise_()
        self.time.raise_()
        self.Title.raise_()
        self.others.raise_()
        self.back5.raise_()
        self.tag.raise_()
        self.back4.raise_()
        self.undo.raise_()
        self.title.raise_()
        self.titletext.raise_()
        self.high_lev.raise_()
        self.dele.raise_()
        self.label.raise_()

        self.retranslateUi(edittask)

        QMetaObject.connectSlotsByName(edittask)
    # setupUi

    def retranslateUi(self, edittask):
        edittask.setWindowTitle(QCoreApplication.translate("edittask", u"Form", None))
        self.urgent_lev.setText(QCoreApplication.translate("edittask", u"Urgent", None))
        self.label_3.setText("")
        self.med_lev.setText(QCoreApplication.translate("edittask", u"Medium", None))
        self.note.setText(QCoreApplication.translate("edittask", u"Note:", None))
        self.urgent.setText(QCoreApplication.translate("edittask", u"Urgency Level", None))
        self.low_lev.setText(QCoreApplication.translate("edittask", u"Low", None))
        self.back6.setText("")
        self.home.setText(QCoreApplication.translate("edittask", u"home", None))
        self.save.setText(QCoreApplication.translate("edittask", u"Save", None))
        self.errand.setText(QCoreApplication.translate("edittask", u"errand", None))
        self.work.setText(QCoreApplication.translate("edittask", u"work", None))
        self.Title.setText(QCoreApplication.translate("edittask", u"Edit Task", None))
        self.back.setText("")
        self.others.setText(QCoreApplication.translate("edittask", u"other", None))
        self.back5.setText("")
        self.tag.setText(QCoreApplication.translate("edittask", u"Tag:", None))
        self.back4.setText("")
        self.back2.setText("")
        self.undo.setText(QCoreApplication.translate("edittask", u"Undo", None))
        self.title.setText(QCoreApplication.translate("edittask", u"Title:", None))
        self.high_lev.setText(QCoreApplication.translate("edittask", u"High", None))
        self.back3.setText("")
        self.dele.setText(QCoreApplication.translate("edittask", u"Delete", None))
        self.label.setText(QCoreApplication.translate("edittask", u"V", None))
    # retranslateUi

