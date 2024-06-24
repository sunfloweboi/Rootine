# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'temp.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1080, 699)
        Form.setStyleSheet(u"#sidebartitle{\n"
"font-size: 20px;\n"
"}\n"
"#Form{\n"
"background-color: #EAE4D6;\n"
"}\n"
"#Home{\n"
"background-color: #596020;\n"
"}\n"
"#hidenav{\n"
"background-color: white;\n"
"}\n"
"#shownav{\n"
"}")
        self.page_stackedWidget = QStackedWidget(Form)
        self.page_stackedWidget.setObjectName(u"page_stackedWidget")
        self.page_stackedWidget.setGeometry(QRect(290, 40, 771, 611))
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.layoutWidget = QWidget(self.Home)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(-60, 10, 791, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.searchbar = QLineEdit(self.layoutWidget)
        self.searchbar.setObjectName(u"searchbar")

        self.horizontalLayout.addWidget(self.searchbar)

        self.search_btn = QPushButton(self.layoutWidget)
        self.search_btn.setObjectName(u"search_btn")
        icon = QIcon()
        icon.addFile(u"../../../Downloads/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.search_btn)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.profile_btn = QPushButton(self.layoutWidget)
        self.profile_btn.setObjectName(u"profile_btn")
        icon1 = QIcon()
        icon1.addFile(u"../../../Downloads/man.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_btn.setIcon(icon1)
        self.profile_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.profile_btn)

        self.page_stackedWidget.addWidget(self.Home)
        self.User = QWidget()
        self.User.setObjectName(u"User")
        self.page_stackedWidget.addWidget(self.User)
        self.Progress = QWidget()
        self.Progress.setObjectName(u"Progress")
        self.page_stackedWidget.addWidget(self.Progress)
        self.Calendar = QWidget()
        self.Calendar.setObjectName(u"Calendar")
        self.calendarWidget = QCalendarWidget(self.Calendar)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(200, 170, 392, 236))
        self.page_stackedWidget.addWidget(self.Calendar)
        self.shownav = QWidget(Form)
        self.shownav.setObjectName(u"shownav")
        self.shownav.setGeometry(QRect(20, 40, 61, 611))
        self.shownav.setStyleSheet(u"backgroun-color: white;")
        self.iconpic_2 = QLabel(self.shownav)
        self.iconpic_2.setObjectName(u"iconpic_2")
        self.iconpic_2.setGeometry(QRect(10, 30, 51, 51))
        self.iconpic_2.setPixmap(QPixmap(u"../../../Downloads/logo.png"))
        self.iconpic_2.setScaledContents(True)
        self.layoutWidget1 = QWidget(self.shownav)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 220, 61, 371))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fhome_btn_2 = QPushButton(self.layoutWidget1)
        self.fhome_btn_2.setObjectName(u"fhome_btn_2")
        icon2 = QIcon()
        icon2.addFile(u"resource/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fhome_btn_2.setIcon(icon2)
        self.fhome_btn_2.setFlat(True)

        self.verticalLayout.addWidget(self.fhome_btn_2)

        self.user_btn = QPushButton(self.layoutWidget1)
        self.user_btn.setObjectName(u"user_btn")
        icon3 = QIcon()
        icon3.addFile(u"resource/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.user_btn.setIcon(icon3)
        self.user_btn.setFlat(True)

        self.verticalLayout.addWidget(self.user_btn)

        self.progress_btn = QPushButton(self.layoutWidget1)
        self.progress_btn.setObjectName(u"progress_btn")
        icon4 = QIcon()
        icon4.addFile(u"resource/progress.png", QSize(), QIcon.Normal, QIcon.Off)
        self.progress_btn.setIcon(icon4)
        self.progress_btn.setFlat(True)

        self.verticalLayout.addWidget(self.progress_btn)

        self.calendar_btn = QPushButton(self.layoutWidget1)
        self.calendar_btn.setObjectName(u"calendar_btn")
        icon5 = QIcon()
        icon5.addFile(u"resource/calendar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calendar_btn.setIcon(icon5)
        self.calendar_btn.setFlat(True)

        self.verticalLayout.addWidget(self.calendar_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.logout_btn = QPushButton(self.layoutWidget1)
        self.logout_btn.setObjectName(u"logout_btn")
        icon6 = QIcon()
        icon6.addFile(u"resource/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_btn.setIcon(icon6)
        self.logout_btn.setFlat(True)

        self.verticalLayout.addWidget(self.logout_btn)

        self.hidenav = QFrame(Form)
        self.hidenav.setObjectName(u"hidenav")
        self.hidenav.setGeometry(QRect(20, 40, 191, 611))
        self.iconpic = QLabel(self.hidenav)
        self.iconpic.setObjectName(u"iconpic")
        self.iconpic.setGeometry(QRect(10, 30, 61, 61))
        self.iconpic.setPixmap(QPixmap(u"../../../Downloads/logo.png"))
        self.iconpic.setScaledContents(True)
        self.sidebartitle = QLabel(self.hidenav)
        self.sidebartitle.setObjectName(u"sidebartitle")
        self.sidebartitle.setGeometry(QRect(80, 50, 101, 31))
        font = QFont()
        font.setPointSize(15)
        self.sidebartitle.setFont(font)
        self.sidebartitle.setStyleSheet(u"font-size: 15pt;")
        self.layoutWidget2 = QWidget(self.hidenav)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 220, 171, 371))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fhome_btn = QPushButton(self.layoutWidget2)
        self.fhome_btn.setObjectName(u"fhome_btn")
        self.fhome_btn.setStyleSheet(u"")
        self.fhome_btn.setIcon(icon2)
        self.fhome_btn.setFlat(True)

        self.verticalLayout_2.addWidget(self.fhome_btn)

        self.fuser_btn = QPushButton(self.layoutWidget2)
        self.fuser_btn.setObjectName(u"fuser_btn")
        self.fuser_btn.setIcon(icon3)
        self.fuser_btn.setFlat(True)

        self.verticalLayout_2.addWidget(self.fuser_btn)

        self.fprogress_btn = QPushButton(self.layoutWidget2)
        self.fprogress_btn.setObjectName(u"fprogress_btn")
        self.fprogress_btn.setIcon(icon4)
        self.fprogress_btn.setFlat(True)

        self.verticalLayout_2.addWidget(self.fprogress_btn)

        self.fcalendar_btn = QPushButton(self.layoutWidget2)
        self.fcalendar_btn.setObjectName(u"fcalendar_btn")
        self.fcalendar_btn.setIcon(icon5)
        self.fcalendar_btn.setFlat(True)

        self.verticalLayout_2.addWidget(self.fcalendar_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.flogout_btn = QPushButton(self.layoutWidget2)
        self.flogout_btn.setObjectName(u"flogout_btn")
        self.flogout_btn.setIcon(icon6)
        self.flogout_btn.setFlat(True)

        self.verticalLayout_2.addWidget(self.flogout_btn)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 71, 611))
        self.label.setStyleSheet(u"background-color: white;")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 271, 611))
        self.label_2.setStyleSheet(u"background-color: #596020;")
        self.nav_btn = QPushButton(Form)
        self.nav_btn.setObjectName(u"nav_btn")
        self.nav_btn.setGeometry(QRect(250, 60, 33, 29))
        icon7 = QIcon()
        icon7.addFile(u"../../../Downloads/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nav_btn.setIcon(icon7)
        self.nav_btn.setCheckable(True)
        self.label_2.raise_()
        self.label.raise_()
        self.page_stackedWidget.raise_()
        self.shownav.raise_()
        self.hidenav.raise_()
        self.nav_btn.raise_()

        self.retranslateUi(Form)
        self.nav_btn.toggled.connect(self.shownav.setVisible)
        self.nav_btn.toggled.connect(self.hidenav.setHidden)

        self.page_stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.search_btn.setText("")
        self.profile_btn.setText("")
        self.iconpic_2.setText("")
        self.fhome_btn_2.setText("")
        self.user_btn.setText("")
        self.progress_btn.setText("")
        self.calendar_btn.setText("")
        self.logout_btn.setText("")
        self.iconpic.setText("")
        self.sidebartitle.setText(QCoreApplication.translate("Form", u"Side Bar", None))
        self.fhome_btn.setText(QCoreApplication.translate("Form", u"Home", None))
        self.fuser_btn.setText(QCoreApplication.translate("Form", u"User Profile", None))
        self.fprogress_btn.setText(QCoreApplication.translate("Form", u"Habit Progress", None))
        self.fcalendar_btn.setText(QCoreApplication.translate("Form", u"Calendar", None))
        self.flogout_btn.setText(QCoreApplication.translate("Form", u"Logout", None))
        self.label.setText("")
        self.label_2.setText("")
        self.nav_btn.setText("")
    # retranslateUi

