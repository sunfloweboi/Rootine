# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mainwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1066, 700)
        Form.setMaximumSize(QSize(1066, 700))
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
"#top{\n"
"background-color:white;\n"
"}\n"
"QLabel{\n"
"color: #403E2C;\n"
"}")
        self.page_stackedWidget = QStackedWidget(Form)
        self.page_stackedWidget.setObjectName(u"page_stackedWidget")
        self.page_stackedWidget.setGeometry(QRect(70, 60, 1011, 641))
        self.page_stackedWidget.setStyleSheet(u"#Home{\n"
"background-color: #EAE4D6;\n"
"}\n"
"#User{\n"
"background-color: #EAE4D6;\n"
"}\n"
"#Progress{\n"
"background-color: white;\n"
"}\n"
"#Calendar{\n"
"background-color: #EAE4D6;\n"
"}\n"
"#line{\n"
"border-top: 2px solid #403E2C;\n"
"}\n"
"#line_2{\n"
"border: 2px solid #403E2C;\n"
"border-top: 0px;\n"
"border-right: 0px;\n"
"}\n"
"#Progress_title{\n"
"font: 20pt \"High Tower Text\";\n"
"color: white;\n"
"}\n"
"#statistic_btn{\n"
"font: 20pt \"High Tower Text\";\n"
"border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"background-color: #EAE4D6;\n"
"}\n"
"#history_btn{\n"
"font: 20pt \"High Tower Text\";\n"
"border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"background-color: #7A7761;\n"
"}\n"
"#statistic { \n"
"background-color: #EAE4D6; \n"
"}\n"
"#history{\n"
"background-color: #7A7761;\n"
"}\n"
"#historyview{\n"
"background-color: #7A7761;\n"
"}\n"
"#detail{\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.homescreen = QLabel(self.Home)
        self.homescreen.setObjectName(u"homescreen")
        self.homescreen.setGeometry(QRect(50, 30, 941, 601))
        self.homescreen.setStyleSheet(u"#homescreen{\n"
"background-color: #EAE4D6;\n"
"border-radius: 20px;\n"
"border: 2px solid #596020;\n"
"}")
        self.task_screen = QLabel(self.Home)
        self.task_screen.setObjectName(u"task_screen")
        self.task_screen.setGeometry(QRect(560, 40, 421, 551))
        self.task_screen.setStyleSheet(u"#task_screen{\n"
"background-color: #EAE4D6;\n"
"border-radius: 20px;\n"
"border: 2px solid #596020;\n"
"}\n"
"")
        self.dailies_btn = QPushButton(self.Home)
        self.dailies_btn.setObjectName(u"dailies_btn")
        self.dailies_btn.setGeometry(QRect(630, 70, 121, 41))
        self.dailies_btn.setStyleSheet(u"#dailies_btn{\n"
"border-radius: 20px;\n"
"background-color: #EF8c24;\n"
"\n"
"}")
        self.todo_btn = QPushButton(self.Home)
        self.todo_btn.setObjectName(u"todo_btn")
        self.todo_btn.setGeometry(QRect(780, 70, 121, 41))
        self.todo_btn.setStyleSheet(u"#todo_btn{\n"
"border-radius: 20px;\n"
"background-color: white;\n"
"}")
        self.stackedWidget = QStackedWidget(self.Home)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(580, 120, 391, 461))
        self.stackedWidget.setStyleSheet(u"background-color: #EAE4D6;")
        self.dailies_page = QWidget()
        self.dailies_page.setObjectName(u"dailies_page")
        self.adddailies = QPushButton(self.dailies_page)
        self.adddailies.setObjectName(u"adddailies")
        self.adddailies.setGeometry(QRect(42, 20, 291, 28))
        self.adddailies.setStyleSheet(u"#adddailies{\n"
"border-radius: 10px;\n"
"background-color: #E5E5E5;\n"
"border: 1px solid black;\n"
"}\n"
"#adddailies::hover{\n"
"border-radius: 10px;\n"
"background-color: #CFC9BB;\n"
"border: 1px solid black;\n"
"}")
        self.habit_list = QScrollArea(self.dailies_page)
        self.habit_list.setObjectName(u"habit_list")
        self.habit_list.setGeometry(QRect(0, 50, 391, 361))
        self.habit_list.setStyleSheet(u"#habit_list{\n"
"border: none;\n"
"}\n"
"")
        self.habit_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.habit_list.setWidgetResizable(True)
        self.habitlist = QWidget()
        self.habitlist.setObjectName(u"habitlist")
        self.habitlist.setGeometry(QRect(0, 0, 389, 359))
        self.verticalLayout_3 = QVBoxLayout(self.habitlist)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.habit_list.setWidget(self.habitlist)
        self.stackedWidget.addWidget(self.dailies_page)
        self.habit_list.raise_()
        self.adddailies.raise_()
        self.todo_page = QWidget()
        self.todo_page.setObjectName(u"todo_page")
        self.addtodo = QPushButton(self.todo_page)
        self.addtodo.setObjectName(u"addtodo")
        self.addtodo.setGeometry(QRect(42, 20, 291, 28))
        self.addtodo.setStyleSheet(u"#addtodo{\n"
"border-radius: 10px;\n"
"background-color: #E5E5E5;\n"
"border: 1px solid black;\n"
"}\n"
"#addtodo::hover{\n"
"border-radius: 10px;\n"
"background-color: #CFC9BB;\n"
"border: 1px solid black;\n"
"}")
        self.todo_list = QScrollArea(self.todo_page)
        self.todo_list.setObjectName(u"todo_list")
        self.todo_list.setGeometry(QRect(0, 60, 391, 351))
        self.todo_list.setStyleSheet(u"#todo_list{\n"
"border: none;\n"
"}")
        self.todo_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.todo_list.setWidgetResizable(True)
        self.todolist = QWidget()
        self.todolist.setObjectName(u"todolist")
        self.todolist.setGeometry(QRect(0, 0, 389, 349))
        self.todo_list.setWidget(self.todolist)
        self.stackedWidget.addWidget(self.todo_page)
        self.tree = QLabel(self.Home)
        self.tree.setObjectName(u"tree")
        self.tree.setGeometry(QRect(180, 280, 271, 291))
        self.tree.setPixmap(QPixmap(u"resource/tree.png"))
        self.tree.setScaledContents(True)
        self.label_40 = QLabel(self.Home)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(550, 55, 421, 551))
        self.label_40.setStyleSheet(u"background-color: #EF8c24;\n"
"border-radius: 20px;")
        self.label_39 = QLabel(self.Home)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(540, 70, 421, 551))
        self.label_39.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 20px;\n"
"")
        self.lineEdit_6 = QLineEdit(self.Home)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(260, 580, 113, 22))
        self.lineEdit_6.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.lineEdit_6.setStyleSheet(u"background-color: #EAE4D6;\n"
"border: 2px solid #596020;\n"
"border-radius:5px;\n"
"right:0;\n"
"padding-right: 10px;")
        self.lineEdit_6.setReadOnly(True)
        self.page_stackedWidget.addWidget(self.Home)
        self.homescreen.raise_()
        self.label_39.raise_()
        self.label_40.raise_()
        self.task_screen.raise_()
        self.todo_btn.raise_()
        self.stackedWidget.raise_()
        self.dailies_btn.raise_()
        self.tree.raise_()
        self.lineEdit_6.raise_()
        self.User = QWidget()
        self.User.setObjectName(u"User")
        self.profile = QPushButton(self.User)
        self.profile.setObjectName(u"profile")
        self.profile.setGeometry(QRect(180, 60, 101, 101))
        self.profile.setStyleSheet(u"#profile{\n"
"background-color: white;\n"
"border-radius: 50px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"resource/profile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profile.setIcon(icon)
        self.profile.setIconSize(QSize(50, 50))
        self.profile.setFlat(False)
        self.head1 = QLabel(self.User)
        self.head1.setObjectName(u"head1")
        self.head1.setGeometry(QRect(320, 100, 81, 16))
        font = QFont()
        font.setPointSize(10)
        self.head1.setFont(font)
        self.head2 = QLabel(self.User)
        self.head2.setObjectName(u"head2")
        self.head2.setGeometry(QRect(320, 140, 81, 16))
        self.head2.setFont(font)
        self.title1 = QLabel(self.User)
        self.title1.setObjectName(u"title1")
        self.title1.setGeometry(QRect(320, 40, 201, 41))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setUnderline(True)
        self.title1.setFont(font1)
        self.title1.setStyleSheet(u"")
        self.lineEdit = QLineEdit(self.User)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(410, 100, 191, 22))
        self.lineEdit.setStyleSheet(u"background-color:#EAE4D6;\n"
"border: none;")
        self.lineEdit_2 = QLineEdit(self.User)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(410, 140, 191, 22))
        self.lineEdit_2.setStyleSheet(u"background-color:#EAE4D6;\n"
"border: none;")
        self.title2 = QLabel(self.User)
        self.title2.setObjectName(u"title2")
        self.title2.setGeometry(QRect(590, 250, 401, 41))
        self.title2.setFont(font1)
        self.title2.setStyleSheet(u"")
        self.facebook = QPushButton(self.User)
        self.facebook.setObjectName(u"facebook")
        self.facebook.setGeometry(QRect(790, 310, 101, 61))
        icon1 = QIcon()
        icon1.addFile(u"resource/facebook.png", QSize(), QIcon.Normal, QIcon.Off)
        self.facebook.setIcon(icon1)
        self.facebook.setIconSize(QSize(50, 50))
        self.facebook.setFlat(True)
        self.ig = QPushButton(self.User)
        self.ig.setObjectName(u"ig")
        self.ig.setGeometry(QRect(700, 310, 91, 61))
        icon2 = QIcon()
        icon2.addFile(u"resource/instagram.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ig.setIcon(icon2)
        self.ig.setIconSize(QSize(50, 50))
        self.ig.setFlat(True)
        self.title2_2 = QLabel(self.User)
        self.title2_2.setObjectName(u"title2_2")
        self.title2_2.setGeometry(QRect(650, 40, 81, 41))
        self.title2_2.setFont(font1)
        self.title2_2.setStyleSheet(u"")
        self.title2_3 = QLabel(self.User)
        self.title2_3.setObjectName(u"title2_3")
        self.title2_3.setGeometry(QRect(160, 190, 411, 41))
        self.title2_3.setFont(font1)
        self.title2_3.setStyleSheet(u"")
        self.title2_4 = QLabel(self.User)
        self.title2_4.setObjectName(u"title2_4")
        self.title2_4.setGeometry(QRect(160, 410, 411, 41))
        self.title2_4.setFont(font1)
        self.title2_4.setStyleSheet(u"")
        self.label_3 = QLabel(self.User)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 250, 241, 31))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.User)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 300, 371, 31))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.User)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 360, 251, 31))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.User)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 460, 101, 41))
        self.label_6.setFont(font)
        self.about = QPushButton(self.User)
        self.about.setObjectName(u"about")
        self.about.setGeometry(QRect(160, 550, 101, 61))
        icon3 = QIcon()
        icon3.addFile(u"resource/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.about.setIcon(icon3)
        self.about.setIconSize(QSize(50, 50))
        self.about.setFlat(True)
        self.help = QPushButton(self.User)
        self.help.setObjectName(u"help")
        self.help.setGeometry(QRect(260, 550, 101, 61))
        icon4 = QIcon()
        icon4.addFile(u"resource/question.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help.setIcon(icon4)
        self.help.setIconSize(QSize(50, 50))
        self.help.setFlat(True)
        self.label_7 = QLabel(self.User)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(160, 500, 41, 41))
        self.label_7.setFont(font)
        self.label_8 = QLabel(self.User)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(290, 460, 141, 41))
        self.label_8.setFont(font)
        self.label_9 = QLabel(self.User)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(290, 500, 141, 41))
        self.label_9.setFont(font)
        self.label_10 = QLabel(self.User)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(650, 90, 101, 31))
        self.label_10.setFont(font)
        self.lineEdit_5 = QLineEdit(self.User)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(750, 93, 141, 22))
        self.lineEdit_5.setStyleSheet(u"background-color:#EAE4D6;\n"
"border: none;")
        self.view_btn = QPushButton(self.User)
        self.view_btn.setObjectName(u"view_btn")
        self.view_btn.setGeometry(QRect(890, 70, 101, 61))
        icon5 = QIcon()
        icon5.addFile(u"resource/eye.png", QSize(), QIcon.Normal, QIcon.Off)
        self.view_btn.setIcon(icon5)
        self.view_btn.setIconSize(QSize(20, 20))
        self.view_btn.setFlat(True)
        self.pushButton = QPushButton(self.User)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(750, 130, 91, 34))
        self.pushButton.setStyleSheet(u"background-color: #EF8C24;\n"
"border-radius: 10px;\n"
"color:  #EAE4D6;")
        icon6 = QIcon()
        icon6.addFile(u"resource/undo-arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)
        self.gmail = QPushButton(self.User)
        self.gmail.setObjectName(u"gmail")
        self.gmail.setGeometry(QRect(600, 310, 101, 61))
        icon7 = QIcon()
        icon7.addFile(u"resource/gmail.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gmail.setIcon(icon7)
        self.gmail.setIconSize(QSize(50, 50))
        self.gmail.setFlat(True)
        self.label_21 = QLabel(self.User)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(710, 470, 165, 106))
        self.label_21.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_31 = QLabel(self.User)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(850, 420, 165, 106))
        self.label_31.setStyleSheet(u"background-color: #EF8c24;\n"
"border-radius: 50px;")
        self.label_30 = QLabel(self.User)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(890, 360, 165, 106))
        self.label_30.setStyleSheet(u"background-color: #596020;\n"
"border-radius: 50px;")
        self.label_25 = QLabel(self.User)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(580, 570, 165, 106))
        self.label_25.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_23 = QLabel(self.User)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(800, 510, 165, 106))
        self.label_23.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_26 = QLabel(self.User)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(780, 410, 165, 106))
        self.label_26.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_33 = QLabel(self.User)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(660, 540, 165, 106))
        self.label_33.setStyleSheet(u"background-color: #435d59;\n"
"border-radius: 50px;\n"
"")
        self.label_28 = QLabel(self.User)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(750, 450, 165, 106))
        self.label_28.setStyleSheet(u"background-color: #435d59;\n"
"border-radius: 50px;")
        self.label_32 = QLabel(self.User)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(870, 540, 165, 106))
        self.label_32.setStyleSheet(u"background-color: #596020;\n"
"border-radius: 50px;")
        self.label_27 = QLabel(self.User)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(950, 470, 165, 106))
        self.label_27.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 50px;\n"
"")
        self.label_34 = QLabel(self.User)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(740, 560, 165, 106))
        self.label_34.setStyleSheet(u"background-color: #EF8c24;\n"
"border-radius: 50px;")
        self.page_stackedWidget.addWidget(self.User)
        self.profile.raise_()
        self.head1.raise_()
        self.head2.raise_()
        self.title1.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.title2.raise_()
        self.facebook.raise_()
        self.ig.raise_()
        self.title2_2.raise_()
        self.title2_3.raise_()
        self.title2_4.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.about.raise_()
        self.help.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.lineEdit_5.raise_()
        self.view_btn.raise_()
        self.pushButton.raise_()
        self.gmail.raise_()
        self.label_21.raise_()
        self.label_30.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_33.raise_()
        self.label_28.raise_()
        self.label_27.raise_()
        self.label_23.raise_()
        self.label_31.raise_()
        self.label_34.raise_()
        self.label_32.raise_()
        self.Progress = QWidget()
        self.Progress.setObjectName(u"Progress")
        self.line = QFrame(self.Progress)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-10, 90, 561, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.Progress_title = QLabel(self.Progress)
        self.Progress_title.setObjectName(u"Progress_title")
        self.Progress_title.setGeometry(QRect(150, 20, 211, 41))
        self.frame = QFrame(self.Progress)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 90, 551, 561))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.analWidget = QStackedWidget(self.Progress)
        self.analWidget.setObjectName(u"analWidget")
        self.analWidget.setGeometry(QRect(550, 80, 451, 561))
        self.analWidget.setStyleSheet(u"")
        self.statistic = QWidget()
        self.statistic.setObjectName(u"statistic")
        self.sunday = QPushButton(self.statistic)
        self.sunday.setObjectName(u"sunday")
        self.sunday.setGeometry(QRect(70, 70, 93, 91))
        self.sunday.setStyleSheet(u"border-radius: 45px;\n"
"background-color: #EF8C24;\n"
"color: white;")
        self.tuesday = QPushButton(self.statistic)
        self.tuesday.setObjectName(u"tuesday")
        self.tuesday.setGeometry(QRect(190, 20, 93, 91))
        self.tuesday.setStyleSheet(u"border-radius: 45px;\n"
"background-color: #D6CA51;")
        self.monday = QPushButton(self.statistic)
        self.monday.setObjectName(u"monday")
        self.monday.setGeometry(QRect(190, 120, 93, 91))
        self.monday.setStyleSheet(u"border-radius: 45px;\n"
"background-color: #435D59;\n"
"color: white;")
        self.saturday = QPushButton(self.statistic)
        self.saturday.setObjectName(u"saturday")
        self.saturday.setGeometry(QRect(70, 180, 93, 91))
        self.saturday.setStyleSheet(u"border-radius: 45px;\n"
"background-color: #D6CA51;")
        self.Wednesday = QPushButton(self.statistic)
        self.Wednesday.setObjectName(u"Wednesday")
        self.Wednesday.setGeometry(QRect(310, 70, 93, 91))
        self.Wednesday.setStyleSheet(u"border-radius: 45px;\n"
"background-color: #EF8C24;\n"
"color: white;")
        self.thursday = QPushButton(self.statistic)
        self.thursday.setObjectName(u"thursday")
        self.thursday.setGeometry(QRect(310, 180, 93, 91))
        self.thursday.setStyleSheet(u"border-radius: 45px;\n"
"background-color: #D6CA51;")
        self.friday = QPushButton(self.statistic)
        self.friday.setObjectName(u"friday")
        self.friday.setGeometry(QRect(190, 230, 93, 91))
        self.friday.setStyleSheet(u"border-radius: 45px;\n"
"background-color: #EF8C24;\n"
"color: white;")
        self.detail = QTextEdit(self.statistic)
        self.detail.setObjectName(u"detail")
        self.detail.setGeometry(QRect(30, 340, 401, 201))
        self.detail.setStyleSheet(u"border-radius: 20px;\n"
"background-color: white;\n"
"padding-top: 20px;\n"
"padding-left: 20px;")
        self.analWidget.addWidget(self.statistic)
        self.history = QWidget()
        self.history.setObjectName(u"history")
        self.analWidget.addWidget(self.history)
        self.label_2 = QLabel(self.Progress)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 0, 231, 71))
        self.label_2.setStyleSheet(u"background-color: #596020;\n"
"border-radius: 20px;")
        self.label_12 = QLabel(self.Progress)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(120, 20, 271, 21))
        self.label_12.setStyleSheet(u"background-color: #596020;\n"
"")
        self.label_13 = QLabel(self.Progress)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(371, 20, 191, 41))
        self.label_13.setStyleSheet(u"background-color: white;\n"
"border-radius: 20px;\n"
"")
        self.label_14 = QLabel(self.Progress)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(79, 20, 61, 41))
        self.label_14.setStyleSheet(u"background-color: white;\n"
"border-radius: 20px;\n"
"")
        self.statistic_btn = QPushButton(self.Progress)
        self.statistic_btn.setObjectName(u"statistic_btn")
        self.statistic_btn.setGeometry(QRect(550, 29, 131, 51))
        self.history_btn = QPushButton(self.Progress)
        self.history_btn.setObjectName(u"history_btn")
        self.history_btn.setGeometry(QRect(680, 30, 131, 51))
        self.history_btn.setStyleSheet(u"")
        self.page_stackedWidget.addWidget(self.Progress)
        self.label_12.raise_()
        self.label_2.raise_()
        self.line.raise_()
        self.Progress_title.raise_()
        self.frame.raise_()
        self.analWidget.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.statistic_btn.raise_()
        self.history_btn.raise_()
        self.Calendar = QWidget()
        self.Calendar.setObjectName(u"Calendar")
        self.calendarWidget = QCalendarWidget(self.Calendar)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(100, 50, 581, 541))
        font2 = QFont()
        font2.setStyleStrategy(QFont.PreferDefault)
        self.calendarWidget.setFont(font2)
        self.calendarWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.calendarWidget.setFocusPolicy(Qt.NoFocus)
        self.calendarWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.calendarWidget.setLayoutDirection(Qt.LeftToRight)
        self.calendarWidget.setAutoFillBackground(False)
        self.calendarWidget.setStyleSheet(u"#qt_calendar_navigationbar{\n"
"background-color: white;\n"
"border: 2px solid rgb(89, 96,32);\n"
"border-radius: 10px;\n"
"}\n"
"QCalendarWidget QWidget{\n"
"alternate-background-color:#EAE4D6;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton{\n"
"color:rgb(89, 96, 32);\n"
"font: 30px \"Imprint MT Shadow\";\n"
"icon-size: 30px;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"font: 18px;\n"
"color: black;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled{\n"
"font: 18px;\n"
"color: #CFC9BB;\n"
"}\n"
"#qt_calendar_prevmonth \n"
"#qt_calendar_nextmonth {\n"
"    qproperty-icon: none;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:hover,\n"
"#qt_calendar_monthbutton:hover{\n"
"	background-color: #EAE4D6;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton QMenu::item:selected:enabled{\n"
"background-color:#d6ca51;\n"
"}\n"
"\n"
"#qt_calendar_calendarview{\n"
"background-color: white;\n"
"border-top: 0px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:hover{\n"
"border-radius: 10px;\n"
"back"
                        "ground-color:#EF8c24;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:selected{\n"
"border-radius: 10px;\n"
"background-color:#d6ca51;\n"
"}\n"
"")
        self.calendarWidget.setInputMethodHints(Qt.ImhNone)
        self.calendarWidget.setFirstDayOfWeek(Qt.Monday)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setSelectionMode(QCalendarWidget.NoSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setDateEditAcceptDelay(1500)
        self.listWidget = QListWidget(self.Calendar)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(710, 140, 251, 441))
        self.listWidget.setStyleSheet(u"background-color:#EF8c24;\n"
"border-radius: 20px;")
        self.listWidget_2 = QListWidget(self.Calendar)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(720, 130, 251, 441))
        self.listWidget_2.setStyleSheet(u"border-radius:20px;\n"
"background-color: white;")
        self.listWidget_3 = QListWidget(self.Calendar)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setGeometry(QRect(700, 150, 251, 441))
        self.listWidget_3.setStyleSheet(u"background-color: #d6ca51;\n"
"border-radius: 20px;")
        self.title_2 = QLabel(self.Calendar)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setGeometry(QRect(790, 60, 131, 51))
        font3 = QFont()
        font3.setFamilies([u"Imprint MT Shadow"])
        font3.setBold(False)
        font3.setItalic(False)
        self.title_2.setFont(font3)
        self.title_2.setStyleSheet(u"font: 50px \"Imprint MT Shadow\";\n"
"text-align: center;\n"
"color: #596020;\n"
"")
        self.page_stackedWidget.addWidget(self.Calendar)
        self.listWidget_3.raise_()
        self.calendarWidget.raise_()
        self.listWidget.raise_()
        self.listWidget_2.raise_()
        self.title_2.raise_()
        self.shownav = QWidget(Form)
        self.shownav.setObjectName(u"shownav")
        self.shownav.setGeometry(QRect(10, 80, 61, 621))
        self.shownav.setStyleSheet(u"backgroun-color: white;\n"
"border-right: 3px solid #596020;\n"
"")
        self.iconpic_2 = QLabel(self.shownav)
        self.iconpic_2.setObjectName(u"iconpic_2")
        self.iconpic_2.setGeometry(QRect(0, 30, 51, 51))
        self.iconpic_2.setPixmap(QPixmap(u"../../../Downloads/logo.png"))
        self.iconpic_2.setScaledContents(True)
        self.layoutWidget = QWidget(self.shownav)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 220, 61, 371))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.layoutWidget)
        self.home_btn.setObjectName(u"home_btn")
        icon8 = QIcon()
        icon8.addFile(u"resource/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn.setIcon(icon8)
        self.home_btn.setFlat(True)

        self.verticalLayout.addWidget(self.home_btn)

        self.user_btn = QPushButton(self.layoutWidget)
        self.user_btn.setObjectName(u"user_btn")
        icon9 = QIcon()
        icon9.addFile(u"resource/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.user_btn.setIcon(icon9)
        self.user_btn.setFlat(True)

        self.verticalLayout.addWidget(self.user_btn)

        self.progress_btn = QPushButton(self.layoutWidget)
        self.progress_btn.setObjectName(u"progress_btn")
        icon10 = QIcon()
        icon10.addFile(u"resource/progress.png", QSize(), QIcon.Normal, QIcon.Off)
        self.progress_btn.setIcon(icon10)
        self.progress_btn.setFlat(True)

        self.verticalLayout.addWidget(self.progress_btn)

        self.calendar_btn = QPushButton(self.layoutWidget)
        self.calendar_btn.setObjectName(u"calendar_btn")
        icon11 = QIcon()
        icon11.addFile(u"resource/calendar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calendar_btn.setIcon(icon11)
        self.calendar_btn.setFlat(True)

        self.verticalLayout.addWidget(self.calendar_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.logout_btn = QPushButton(self.layoutWidget)
        self.logout_btn.setObjectName(u"logout_btn")
        icon12 = QIcon()
        icon12.addFile(u"resource/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_btn.setIcon(icon12)
        self.logout_btn.setFlat(True)

        self.verticalLayout.addWidget(self.logout_btn)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 80, 71, 621))
        self.label.setStyleSheet(u"background-color: white;")
        self.top = QLabel(Form)
        self.top.setObjectName(u"top")
        self.top.setGeometry(QRect(0, 0, 1091, 81))
        self.top.setStyleSheet(u"background-color: #596020;")
        self.nav_btn = QPushButton(Form)
        self.nav_btn.setObjectName(u"nav_btn")
        self.nav_btn.setGeometry(QRect(30, 30, 33, 29))
        icon13 = QIcon()
        icon13.addFile(u"../../../Downloads/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nav_btn.setIcon(icon13)
        self.nav_btn.setCheckable(True)
        self.hidenav = QFrame(Form)
        self.hidenav.setObjectName(u"hidenav")
        self.hidenav.setGeometry(QRect(0, 80, 201, 621))
        self.hidenav.setStyleSheet(u"#hidenav{\n"
"border-right: 3px solid #596020;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: #596020;\n"
"color: white;\n"
"}")
        self.iconpic = QLabel(self.hidenav)
        self.iconpic.setObjectName(u"iconpic")
        self.iconpic.setGeometry(QRect(10, 30, 51, 51))
        self.iconpic.setPixmap(QPixmap(u"../../../Downloads/logo.png"))
        self.iconpic.setScaledContents(True)
        self.sidebartitle = QLabel(self.hidenav)
        self.sidebartitle.setObjectName(u"sidebartitle")
        self.sidebartitle.setGeometry(QRect(70, 50, 101, 31))
        self.sidebartitle.setFont(font3)
        self.sidebartitle.setStyleSheet(u"font: 25px \"Imprint MT Shadow\";\n"
"")
        self.layoutWidget1 = QWidget(self.hidenav)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 220, 171, 371))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fhome_btn = QPushButton(self.layoutWidget1)
        self.fhome_btn.setObjectName(u"fhome_btn")
        self.fhome_btn.setStyleSheet(u"")
        self.fhome_btn.setIcon(icon8)
        self.fhome_btn.setFlat(True)

        self.verticalLayout_2.addWidget(self.fhome_btn)

        self.fuser_btn = QPushButton(self.layoutWidget1)
        self.fuser_btn.setObjectName(u"fuser_btn")
        self.fuser_btn.setIcon(icon9)
        self.fuser_btn.setFlat(True)

        self.verticalLayout_2.addWidget(self.fuser_btn)

        self.fprogress_btn = QPushButton(self.layoutWidget1)
        self.fprogress_btn.setObjectName(u"fprogress_btn")
        self.fprogress_btn.setIcon(icon10)
        self.fprogress_btn.setFlat(True)

        self.verticalLayout_2.addWidget(self.fprogress_btn)

        self.fcalendar_btn = QPushButton(self.layoutWidget1)
        self.fcalendar_btn.setObjectName(u"fcalendar_btn")
        self.fcalendar_btn.setIcon(icon11)
        self.fcalendar_btn.setFlat(True)

        self.verticalLayout_2.addWidget(self.fcalendar_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.flogout_btn = QPushButton(self.layoutWidget1)
        self.flogout_btn.setObjectName(u"flogout_btn")
        self.flogout_btn.setIcon(icon12)
        self.flogout_btn.setFlat(True)

        self.verticalLayout_2.addWidget(self.flogout_btn)

        self.title = QLabel(Form)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(470, 10, 191, 51))
        self.title.setFont(font3)
        self.title.setStyleSheet(u"font: 50px \"Imprint MT Shadow\";\n"
"text-align: center;\n"
"color: white;\n"
"")
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(170, 20, 291, 81))
        self.label_11.setStyleSheet(u"background-color: #596020;\n"
"border-radius: 20px;")
        self.label_11.raise_()
        self.page_stackedWidget.raise_()
        self.top.raise_()
        self.label.raise_()
        self.shownav.raise_()
        self.nav_btn.raise_()
        self.hidenav.raise_()
        self.title.raise_()

        self.retranslateUi(Form)
        self.nav_btn.toggled.connect(self.shownav.setVisible)
        self.nav_btn.toggled.connect(self.hidenav.setHidden)
        self.flogout_btn.clicked.connect(Form.close)
        self.fhome_btn.toggled.connect(self.home_btn.setChecked)
        self.home_btn.toggled.connect(self.fhome_btn.setChecked)
        self.user_btn.toggled.connect(self.fuser_btn.setChecked)
        self.fuser_btn.toggled.connect(self.user_btn.setChecked)
        self.progress_btn.toggled.connect(self.fprogress_btn.setChecked)
        self.fprogress_btn.toggled.connect(self.progress_btn.setChecked)
        self.calendar_btn.toggled.connect(self.fcalendar_btn.setChecked)
        self.fcalendar_btn.toggled.connect(self.calendar_btn.setChecked)
        self.logout_btn.clicked.connect(Form.close)

        self.page_stackedWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        self.analWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.homescreen.setText("")
        self.task_screen.setText("")
        self.dailies_btn.setText(QCoreApplication.translate("Form", u"Dailies", None))
        self.todo_btn.setText(QCoreApplication.translate("Form", u"To Do", None))
        self.adddailies.setText(QCoreApplication.translate("Form", u"+", None))
        self.addtodo.setText(QCoreApplication.translate("Form", u"+", None))
        self.tree.setText("")
        self.label_40.setText("")
        self.label_39.setText("")
        self.profile.setText("")
        self.head1.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.head2.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.title1.setText(QCoreApplication.translate("Form", u"Personal Information", None))
        self.title2.setText(QCoreApplication.translate("Form", u"Connect With                                                                    ", None))
        self.facebook.setText("")
        self.ig.setText("")
        self.title2_2.setText(QCoreApplication.translate("Form", u"Privacy ", None))
        self.title2_3.setText(QCoreApplication.translate("Form", u"Your Rootine                                                                                                           ", None))
        self.title2_4.setText(QCoreApplication.translate("Form", u"About Us                                                                                                                                                                                        ", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Time Spent:  NA", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Latest Update:   31 March 2024", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"App Version :      1.0.0", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Contact Us: ", None))
        self.about.setText("")
        self.help.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"Tel:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"123@gmail.com", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"xxx-xxxx-xxxxx", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.lineEdit_5.setText(QCoreApplication.translate("Form", u"xxxxxxxx", None))
        self.view_btn.setText(QCoreApplication.translate("Form", u" View", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"reset", None))
        self.gmail.setText("")
        self.label_21.setText("")
        self.label_31.setText("")
        self.label_30.setText("")
        self.label_25.setText("")
        self.label_23.setText("")
        self.label_26.setText("")
#if QT_CONFIG(tooltip)
        self.label_33.setToolTip(QCoreApplication.translate("Form", u"gh", None))
#endif // QT_CONFIG(tooltip)
        self.label_33.setText("")
#if QT_CONFIG(tooltip)
        self.label_28.setToolTip(QCoreApplication.translate("Form", u"gh", None))
#endif // QT_CONFIG(tooltip)
        self.label_28.setText("")
        self.label_32.setText("")
        self.label_27.setText("")
        self.label_34.setText("")
        self.Progress_title.setText(QCoreApplication.translate("Form", u"Habit Progress", None))
        self.sunday.setText(QCoreApplication.translate("Form", u"Sunday", None))
        self.tuesday.setText(QCoreApplication.translate("Form", u"Tuesday", None))
        self.monday.setText(QCoreApplication.translate("Form", u"Monday", None))
        self.saturday.setText(QCoreApplication.translate("Form", u"Saturday", None))
        self.Wednesday.setText(QCoreApplication.translate("Form", u"Wednesday", None))
        self.thursday.setText(QCoreApplication.translate("Form", u"Thursday", None))
        self.friday.setText(QCoreApplication.translate("Form", u"Friday", None))
        self.label_2.setText("")
        self.label_12.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
        self.statistic_btn.setText(QCoreApplication.translate("Form", u"Statistic", None))
        self.history_btn.setText(QCoreApplication.translate("Form", u"History", None))
        self.title_2.setText(QCoreApplication.translate("Form", u"Task:", None))
        self.iconpic_2.setText("")
        self.home_btn.setText("")
        self.user_btn.setText("")
        self.progress_btn.setText("")
        self.calendar_btn.setText("")
        self.logout_btn.setText("")
        self.label.setText("")
        self.top.setText("")
        self.nav_btn.setText("")
        self.iconpic.setText("")
        self.sidebartitle.setText(QCoreApplication.translate("Form", u"Side Bar", None))
        self.fhome_btn.setText(QCoreApplication.translate("Form", u"Home", None))
        self.fuser_btn.setText(QCoreApplication.translate("Form", u"User Profile", None))
        self.fprogress_btn.setText(QCoreApplication.translate("Form", u"Habit Progress", None))
        self.fcalendar_btn.setText(QCoreApplication.translate("Form", u"Calendar", None))
        self.flogout_btn.setText(QCoreApplication.translate("Form", u"Logout", None))
        self.title.setText(QCoreApplication.translate("Form", u"Rootine", None))
        self.label_11.setText("")
    # retranslateUi

