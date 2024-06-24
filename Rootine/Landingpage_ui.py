# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Landingpage.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QSizePolicy,
    QWidget)

class Ui_LandingPage(object):
    def setupUi(self, LandingPage):
        if not LandingPage.objectName():
            LandingPage.setObjectName(u"LandingPage")
        LandingPage.resize(1083, 700)
        font = QFont()
        font.setFamilies([u"Imprint MT Shadow"])
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        LandingPage.setFont(font)
        LandingPage.setStyleSheet(u"QWidget{\n"
"background-color: rgb(234, 228, 214);\n"
"font: 8pt \"Imprint MT Shadow\";\n"
"item-align: center;}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #EF8C24;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.title = QLabel(LandingPage)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(300, 270, 511, 161))
        font1 = QFont()
        font1.setFamilies([u"Imprint MT Shadow"])
        font1.setBold(False)
        font1.setItalic(False)
        self.title.setFont(font1)
        self.title.setStyleSheet(u"font-size: 150px;\n"
"text-align: center;\n"
"color: #403E2C;\n"
"")
        self.label_3 = QLabel(LandingPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-90, 190, 165, 106))
        self.label_3.setStyleSheet(u"background-color: #EF8c24;\n"
"border-radius: 50px;")
        self.label_4 = QLabel(LandingPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, -20, 165, 106))
        self.label_4.setStyleSheet(u"background-color: #596020;\n"
"border-radius: 50px;")
        self.label_5 = QLabel(LandingPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(-50, 120, 165, 106))
        self.label_5.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_6 = QLabel(LandingPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 10, 165, 106))
        self.label_6.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_7 = QLabel(LandingPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 130, 165, 106))
        self.label_7.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_9 = QLabel(LandingPage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(260, -20, 165, 106))
        self.label_9.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_10 = QLabel(LandingPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(-70, 260, 165, 106))
        self.label_10.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_11 = QLabel(LandingPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 80, 165, 106))
        self.label_11.setStyleSheet(u"background-color: #435d59;\n"
"border-radius: 50px;")
        self.label_12 = QLabel(LandingPage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(-40, 340, 141, 101))
        self.label_12.setStyleSheet(u"background-color: #435d59;\n"
"border-radius: 50px;")
        self.label_13 = QLabel(LandingPage)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(40, 220, 165, 106))
        self.label_13.setStyleSheet(u"background-color: #435d59;\n"
"border-radius: 50px;")
        self.label_14 = QLabel(LandingPage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(-60, -10, 165, 106))
        self.label_14.setStyleSheet(u"background-color: #435d59;\n"
"border-radius: 50px;")
        self.label_15 = QLabel(LandingPage)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(-40, 60, 165, 106))
        self.label_15.setStyleSheet(u"background-color: #596020;\n"
"border-radius: 50px;")
        self.label_16 = QLabel(LandingPage)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(40, -60, 165, 106))
        self.label_16.setStyleSheet(u"background-color: #EF8c24;\n"
"border-radius: 50px;")
        self.label_17 = QLabel(LandingPage)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 180, 165, 106))
        self.label_17.setStyleSheet(u"background-color: #596020;\n"
"border-radius: 50px;")
        self.label_18 = QLabel(LandingPage)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(160, 70, 165, 106))
        self.label_18.setStyleSheet(u"background-color: #596020;\n"
"border-radius: 50px;")
        self.label_19 = QLabel(LandingPage)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(170, 120, 165, 106))
        self.label_19.setStyleSheet(u"background-color: #EF8c24;\n"
"border-radius: 50px;")
        self.label_20 = QLabel(LandingPage)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(980, 600, 165, 106))
        self.label_20.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_21 = QLabel(LandingPage)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(860, 400, 165, 106))
        self.label_21.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_22 = QLabel(LandingPage)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(790, 640, 165, 106))
        self.label_22.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_23 = QLabel(LandingPage)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(950, 440, 165, 106))
        self.label_23.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_24 = QLabel(LandingPage)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(850, 540, 165, 106))
        self.label_24.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_25 = QLabel(LandingPage)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(900, 300, 165, 106))
        self.label_25.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_26 = QLabel(LandingPage)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(930, 340, 165, 106))
        self.label_26.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_27 = QLabel(LandingPage)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(900, 600, 165, 106))
        self.label_27.setStyleSheet(u"background-color: #435d59;\n"
"border-radius: 50px;")
        self.label_28 = QLabel(LandingPage)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(900, 380, 165, 106))
        self.label_28.setStyleSheet(u"background-color: #435d59;\n"
"border-radius: 50px;")
        self.label_29 = QLabel(LandingPage)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(980, 520, 165, 106))
        self.label_29.setStyleSheet(u"background-color: #596020;\n"
"border-radius: 50px;")
        self.label_30 = QLabel(LandingPage)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(970, 260, 165, 106))
        self.label_30.setStyleSheet(u"background-color: #596020;\n"
"border-radius: 50px;")
        self.label_8 = QLabel(LandingPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(770, 560, 165, 106))
        self.label_8.setStyleSheet(u"background-color: #EF8c24;\n"
"border-radius: 50px;")
        self.label_31 = QLabel(LandingPage)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(1000, 350, 165, 106))
        self.label_31.setStyleSheet(u"background-color: #EF8c24;\n"
"border-radius: 50px;")
        self.label_32 = QLabel(LandingPage)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(670, 620, 165, 106))
        self.label_32.setStyleSheet(u"background-color: #435d59;\n"
"border-radius: 50px;")
        self.label_33 = QLabel(LandingPage)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(810, 470, 165, 106))
        self.label_33.setStyleSheet(u"background-color: #435d59;\n"
"border-radius: 50px;\n"
"")
        self.label_34 = QLabel(LandingPage)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(-20, 290, 165, 106))
        self.label_34.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.progressBar = QProgressBar(LandingPage)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(390, 490, 341, 23))
        self.progressBar.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"border-style: none;\n"
"border-radius: 10px;\n"
"text-align: center;\n"
"QProgressBar::chunk{background-color: #EF8C24;}\n"
"")
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.label_34.raise_()
        self.label_33.raise_()
        self.label_32.raise_()
        self.label_24.raise_()
        self.label_8.raise_()
        self.label_22.raise_()
        self.label_27.raise_()
        self.label_19.raise_()
        self.label_18.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_10.raise_()
        self.label_17.raise_()
        self.title.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.label_11.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_5.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_28.raise_()
        self.label_23.raise_()
        self.label_29.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.progressBar.raise_()

        self.retranslateUi(LandingPage)

        QMetaObject.connectSlotsByName(LandingPage)
    # setupUi

    def retranslateUi(self, LandingPage):
        LandingPage.setWindowTitle(QCoreApplication.translate("LandingPage", u"Form", None))
        self.title.setText(QCoreApplication.translate("LandingPage", u"Rootine", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("LandingPage", u"gh", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText("")
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip(QCoreApplication.translate("LandingPage", u"gh", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText("")
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip(QCoreApplication.translate("LandingPage", u"gh", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText("")
#if QT_CONFIG(tooltip)
        self.label_14.setToolTip(QCoreApplication.translate("LandingPage", u"gh", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText("")
        self.label_15.setText("")
        self.label_16.setText("")
        self.label_17.setText("")
        self.label_18.setText("")
        self.label_19.setText("")
        self.label_20.setText("")
        self.label_21.setText("")
        self.label_22.setText("")
        self.label_23.setText("")
        self.label_24.setText("")
        self.label_25.setText("")
        self.label_26.setText("")
#if QT_CONFIG(tooltip)
        self.label_27.setToolTip(QCoreApplication.translate("LandingPage", u"gh", None))
#endif // QT_CONFIG(tooltip)
        self.label_27.setText("")
#if QT_CONFIG(tooltip)
        self.label_28.setToolTip(QCoreApplication.translate("LandingPage", u"gh", None))
#endif // QT_CONFIG(tooltip)
        self.label_28.setText("")
        self.label_29.setText("")
        self.label_30.setText("")
        self.label_8.setText("")
        self.label_31.setText("")
#if QT_CONFIG(tooltip)
        self.label_32.setToolTip(QCoreApplication.translate("LandingPage", u"gh", None))
#endif // QT_CONFIG(tooltip)
        self.label_32.setText("")
#if QT_CONFIG(tooltip)
        self.label_33.setToolTip(QCoreApplication.translate("LandingPage", u"gh", None))
#endif // QT_CONFIG(tooltip)
        self.label_33.setText("")
        self.label_34.setText("")
    # retranslateUi

