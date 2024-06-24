from PySide6.QtGui import QCloseEvent
from PySide6.QtCharts import *
import ZODB
import ZODB.config
import z_obj
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtMultimedia import QSoundEffect
import transaction
from PySide6 import QtCore
from PySide6.QtMultimedia import QSoundEffect
from login_ui import Ui_Login
from signup_ui import Ui_Signup
from Landingpage_ui import Ui_LandingPage
from Mainwidget_ui import Ui_Form
from About_Help_ui import Ui_about
from Add_task_ui import Ui_addtask
from Add_habbit_ui import Ui_addhabbit
from Edit_habit_ui import Ui_edit_habit
from Edit_task_ui import Ui_edittask
from PySide6.QtCore import QDate
from threading import Thread
import bcrypt
import random


counter = 0
user = z_obj.User("none", "none", "none", "none")
global conn

path = './config.xml'
db = ZODB.config.databaseFromURL(path)
conn = db.open()
root = conn.root


class NotificationWindow(QWidget):
    def __init__(self, message):
        super().__init__()

        self.setWindowTitle("Notification")
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile(
            "resource/system-notification.wav"))
        self.sound.play()
        layout = QVBoxLayout()
        self.message_label = QLabel(message)
        self.message_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.message_label)
        self.setLayout(layout)

        self.setStyleSheet(
            "background-color: none; color: black; padding: 10px; ")
        self.setFixedSize(350, 175)

    def mousePressEvent(self, event):
        self.close()


class Habitsystem(object):
    def __init__(self):
        self.habits = user.habitList
        self.history = user.History
        self.observer = []
        self.win = None

    def addobserver(self, observer):
        self.observer.append(observer)

    def notifyobserver(self, habitdata, historydata):
        for observer in self.observer:
            observer.update_habit(habitdata)
            observer.update_history(historydata)

    def notifyleaveobserver(self, leaves):
        for observer in self.observer:
            observer.ui.lineEdit_6.setText(str(leaves))

    def addhabit(self, habitname, description, time, days):
        if not any(h.name == habitname for h in self.habits):
            habit = z_obj.Habit(habitname, description, time, days)
            self.habits.append(habit)
            print("habit added to system")
            self.history.append(
                z_obj.Event(
                    habit.name,
                    QDate.currentDate(),
                    QTime.currentTime(),
                    "added"))
            self.notifyobserver(self.habits, self.history)
            Thread(target=self.update_database).start()
        else:
            print("habit already exist")
            self.win = NotificationWindow("Habit already exists")
            self.win.show()

    def deletehabit(self, name):
        self.habits = [habit for habit in self.habits if habit.name != name]
        print("habit deleted")
        self.history.append(
            z_obj.Event(
                name,
                QDate.currentDate(),
                QTime.currentTime(),
                "deleted"))
        self.notifyobserver(self.habits, self.history)
        Thread(target=self.update_database).start()

    def edit_habit(self, habitname, name, description, days):
        for h in self.habits:
            if h.name == habitname:
                h.name = name
                h.description = description
                h.days = days
                print("habit edited")
                self.notifyobserver(self.habits, self.history)
                Thread(target=self.update_database).start()
                return

    def duplicatecheck(self, name):
        for habit in self.habits:
            if habit.name == name:
                return True
        return False

    def setdone(self, hname):
        for h in self.habits:
            if h.name == hname:
                h.done = True
                h.counter += 1
                self.history.append(
                    z_obj.Event(
                        h.name,
                        QDate.currentDate(),
                        QTime.currentTime(),
                        "done"))
                self.notifyobserver(self.habits, self.history)

                print("habit done")
                Thread(target=self.update_database).start()
                return
        print("habit not found")

    def setundone(self, hname):
        for h in self.habits:
            if h.name == hname:
                h.done = False
                h.counter -= 1
                self.history.append(
                    z_obj.Event(
                        h.name,
                        QDate.currentDate(),
                        QTime.currentTime(),
                        "undone"))
                self.notifyobserver(self.habits, self.history)

                print("habit undone")
                Thread(target=self.update_database).start()
                return
        print("habit not found")

    def updatehabitlist(self):
        self.habits = user.habitList
        self.history = user.History
        self.notifyobserver(self.habits, self.history)

    def deleteleaves(self, value):
        user.tree.deleteLeave(value)
        transaction.commit()
        self.notifyleaveobserver(user.tree.leaves)

    def addleaves(self, value):
        user.tree.addLeave(value)
        transaction.commit()
        self.notifyleaveobserver(user.tree.leaves)

    def update_database(self):
        root.users[user.username].habitList = self.habits
        root.users[user.username].History = self.history

        transaction.commit()


class Todosystem(object):
    def __init__(self):
        self.todos = user.todoTask
        self.observer = []
        self.win = None

    def addobserver(self, observer):
        self.observer.append(observer)

    def notifyobserver(self, data):
        for observer in self.observer:
            observer.update_todo(data)

    def addtodo(self, title, description, date, urgency, tag, time):
        if not any(t.name == title for t in self.todos):
            todo = z_obj.TodoTask(title, description, date, urgency, tag, time)
            self.todos.append(todo)
            print(self.todos)
            self.notifyobserver(self.todos)
            root.users[user.username].todoTask = self.todos
            user.todoTask = self.todos
            transaction.commit()
        else:
            print("todo already exist")
            self.win = NotificationWindow("Todo already exists")
            self.win.show()

    def edittodo(self, todoname, name, description, urgency, tag, date, time):
        for t in self.todos:
            if t.name == todoname:
                t.name = name
                t.description = description
                t.urgency = urgency
                t.tag = tag
                t.date = date
                t.time = time
                print("todo edited")
                self.notifyobserver(self.todos)
                root.users[user.username].todoTask = self.todos
                user.todoTask = self.todos
                transaction.commit()
                return

    def deletetodo(self, name):
        self.todos = [todo for todo in self.todos if todo.name != name]
        print("todo deleted")
        self.notifyobserver(self.todos)
        root.users[user.username].todoTask = self.todos
        user.todoTask = self.todos
        transaction.commit()

    def updatetodolist(self):
        self.todos = user.todoTask
        self.notifyobserver(self.todos)

    def duplicatescheck(self, name):
        for todo in self.todos:
            if todo.name == name:
                return True
        return False


habitsystem = Habitsystem()
todosystem = Todosystem()


class CenteredDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        option_aligned = QStyleOptionViewItem(option)
        option_aligned.displayAlignment = Qt.AlignCenter
        super().paint(painter, option_aligned, index)

        painter.save()
        border_color = QColor("#222222")  # Set the color of the border
        # Set the alpha (transparency) of the border
        border_color.setAlphaF(0.5)
        painter.setPen(border_color)
        rect = option_aligned.rect
        # Draw a line along the bottom edge
        painter.drawLine(rect.bottomLeft(), rect.bottomRight())
        painter.restore()

    def sizeHint(self, option, index):
        size_hint = super().sizeHint(option, index)
        list_widget = option.widget
        if list_widget:
            top_margin = 10
            # size_hint.setHeight(list_widget.viewport().size().height() / 12)
        return size_hint


class MainWindow(QMainWindow):
    def __init__(self, habitsystem):
        QMainWindow.__init__(self)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.lineEdit_6.setText(str(user.tree.leaves))
        # initially set pic according to leaves
        self.ui.hidenav.hide()
        self.ui.page_stackedWidget.setCurrentIndex(0)
        self.ui.fhome_btn.setChecked(True)
        self.ui.home_btn.clicked.connect(self.on_home_btn_clicked)
        self.ui.fhome_btn.clicked.connect(self.on_home_btn_clicked)
        self.ui.user_btn.clicked.connect(self.on_user_btn_clicked)
        self.ui.fuser_btn.clicked.connect(self.on_user_btn_clicked)
        self.ui.progress_btn.clicked.connect(self.on_analyze_btn_clicked)
        self.ui.fprogress_btn.clicked.connect(self.on_analyze_btn_clicked)
        self.ui.calendar_btn.clicked.connect(self.on_calendar_btn_clicked)
        self.ui.fcalendar_btn.clicked.connect(self.on_calendar_btn_clicked)
        self.ui.calendarWidget.clicked.connect(self.on_calendar_btn_clicked)
        self.ui.calendarWidget.setSelectionMode(
            QCalendarWidget.SingleSelection)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.about.clicked.connect(self.about)
        self.ui.help.clicked.connect(self.about)
        self.ui.adddailies.clicked.connect(self.add_habit)
        self.ui.addtodo.clicked.connect(self.add_todo)
        self.ui.dailies_btn.clicked.connect(self.daily)
        self.ui.todo_btn.clicked.connect(self.todo)

        self.ui.view_btn.clicked.connect(self.showpsw)
        self.showp = False
        self.habitcontainer = QWidget()
        self.habitlayout = QVBoxLayout(self.habitcontainer)

        self.habitScrollArea = QScrollArea()
        self.habitScrollArea.setWidgetResizable(True)
        self.habitScrollArea.setWidget(self.habitcontainer)
        self.habitScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.habitScrollArea.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        self.habitScrollArea.setFrameShape(QFrame.NoFrame)
        self.ui.habit_list.setLayout(QVBoxLayout())
        self.ui.habit_list.layout().addWidget(self.habitScrollArea)

        self.historycontainer = QWidget()
        self.historylayout = QVBoxLayout(self.historycontainer)

        self.historyscrollArea = QScrollArea()
        self.historyscrollArea.setWidgetResizable(True)
        self.historyscrollArea.setWidget(self.historycontainer)
        self.historyscrollArea.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        self.historyscrollArea.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff)
        self.historyscrollArea.setFrameShape(QFrame.NoFrame)
        self.ui.history.setLayout(QVBoxLayout())
        self.ui.history.layout().addWidget(self.historyscrollArea)

        self.todolistcontainer = QWidget()
        self.todolayout = QVBoxLayout(self.todolistcontainer)

        self.todoScrollArea = QScrollArea()
        self.todoScrollArea.setWidgetResizable(True)
        self.todoScrollArea.setWidget(self.todolistcontainer)
        self.todoScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.todoScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.todoScrollArea.setWidgetResizable(True)
        self.todoScrollArea.setFrameShape(QFrame.NoFrame)
        self.ui.todo_list.setLayout(QVBoxLayout())
        self.ui.todo_list.layout().addWidget(self.todoScrollArea)

        self.todo_system = todosystem
        self.todo_system.addobserver(self)
        self.todo_system.updatetodolist()

        self.ui.statistic_btn.clicked.connect(self.showstatistic)
        self.ui.history_btn.clicked.connect(self.showhistory)

        self.chart = QChart()
        self.chartView = QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)

        self.chartLayout = QVBoxLayout()

        self.graphlayout = QHBoxLayout()
        self.graphlayout.addLayout(self.chartLayout)
        self.graphlayout.addWidget(self.chartView)
        self.ui.frame.setLayout(self.graphlayout)

        self.habit_system = habitsystem
        self.habit_system.addobserver(self)
        self.habit_system.updatehabitlist()

        self.habits = self.habit_system.habits

        self.ui.monday.clicked.connect(lambda: self.displayanalysis("mon"))
        self.ui.tuesday.clicked.connect(lambda: self.displayanalysis("tue"))
        self.ui.Wednesday.clicked.connect(lambda: self.displayanalysis("wed"))
        self.ui.thursday.clicked.connect(lambda: self.displayanalysis("thu"))
        self.ui.friday.clicked.connect(lambda: self.displayanalysis("fri"))
        self.ui.saturday.clicked.connect(lambda: self.displayanalysis("sat"))
        self.ui.sunday.clicked.connect(lambda: self.displayanalysis("sun"))

        for habit in self.habits:
            print(habit.name, habit.days, habit.time)

        self.updatetreesprite()

    def updatetreesprite(self):
        if user.tree.leaves == 0:
            self.ui.tree.setPixmap(QPixmap("resource/tree0.png"))
        elif user.tree.leaves >= 1 and user.tree.leaves <= 5:
            self.ui.tree.setPixmap(QPixmap("resource/tree1.png"))
        elif user.tree.leaves >= 6 and user.tree.leaves <= 10:
            self.ui.tree.setPixmap(QPixmap("resource/tree2.png"))
        elif user.tree.leaves >= 11 and user.tree.leaves <= 15:
            self.ui.tree.setPixmap(QPixmap("resource/tree3.png"))
        elif user.tree.leaves >= 16:  # and user.tree.leaves <= 20:
            self.ui.tree.setPixmap(QPixmap("resource/tree4.png"))

    def displayanalysis(self, day):
        string = ""
        string2 = ""
        for habit in self.habits:
            if day in habit.days:
                string += f"{habit.name} | {habit.counter} times\n"
                if habit.counter > 10:
                    string2 += f"{habit.name} | {habit.counter} times\n"

        if string == "":
            string = "No habits for this day"

        self.ui.detail.setText(string + string2)

    def showinfo(self):
        self.ui.lineEdit.setText(user.username)
        self.ui.lineEdit_2.setText(user.email)

    def showpsw(self):
        if not self.showp:
            self.ui.lineEdit_5.setText(user.password)
            self.showp = True
        elif self.showp:
            self.ui.lineEdit_5.setText("********")
            self.showp = False

    def showstatistic(self):
        self.ui.analWidget.setCurrentIndex(0)

    def showhistory(self):
        self.ui.analWidget.setCurrentIndex(1)

    def daily(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.dailies_btn.setStyleSheet(
            'background-color: #EF8C24; border-radius: 20px;')
        self.ui.todo_btn.setStyleSheet(
            'background-color: white; border-radius: 20px;')

    def todo(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.dailies_btn.setStyleSheet(
            'background-color: white; border-radius: 20px;')
        self.ui.todo_btn.setStyleSheet(
            'background-color: #EF8C24; border-radius: 20px;')

    def on_home_btn_clicked(self):
        self.ui.page_stackedWidget.setCurrentIndex(0)
        self.ui.calendarWidget.setSelectedDate(QDate.currentDate())

    def on_user_btn_clicked(self):
        self.ui.page_stackedWidget.setCurrentIndex(1)
        self.showinfo()
        self.ui.calendarWidget.setSelectedDate(QDate.currentDate())

    def on_analyze_btn_clicked(self):
        self.ui.page_stackedWidget.setCurrentIndex(2)
        self.ui.calendarWidget.setSelectedDate(QDate.currentDate())

    def on_calendar_btn_clicked(self):
        self.ui.page_stackedWidget.setCurrentIndex(3)

        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.setItemDelegate(CenteredDelegate())
        date = QDate.currentDate()
        

        currentMonth = self.ui.calendarWidget.selectedDate().month()
        currentYear = self.ui.calendarWidget.selectedDate().year()

        for todo in user.todoTask:

            if todo.date.toString(
                    "yyyy-MM-dd") == self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd"):
                print("todo found")
                print(todo.name)
                print(todo.date.toString("yyyy-MM-dd"))
                tagg = ""
                for tag in todo.tag:
                    tagg += f"{tag} "
                print(todo.date.toString())
                calendarbutton = QPushButton(
                    f"name : {todo.name} \n description : {todo.description} \n urgency : {todo.urgency} \n tag : {tagg} \n time : {todo.time.toString('hh:mm')}")
                calendarbutton.clicked.connect(self.edittodoclickhandler(todo))
                calendaritem = QListWidgetItem(self.ui.listWidget_2)
                calendaritem.setSizeHint(calendarbutton.sizeHint())
                self.ui.listWidget_2.setItemWidget(
                    calendaritem, calendarbutton)

        # Get the number of days in the current month
        num_days = QDate(currentYear, currentMonth, 1).daysInMonth()

        # Iterate over each day of the month
        for day in range(1, num_days + 1):
            date = QDate(currentYear, currentMonth, day)

            # Check if there's a todo task for this day
            for todo in user.todoTask:
                if todo.date == date:
                    # If there is, set the underline and color for this day
                    underline_format = QTextCharFormat()
                    underline_format.setFontUnderline(True)
                    underline_format.setBackground(QColor("#EF8c24"))
                    self.ui.calendarWidget.setDateTextFormat(
                        date, underline_format)
                    break  # No need to check the rest of the tasks for this day
                else:
                    # If there isn't, set the underline for this day
                    underline_format = QTextCharFormat()
                    underline_format.setFontUnderline(False)
                    underline_format.setBackground(QColor("#FFFFFF"))
                    self.ui.calendarWidget.setDateTextFormat(
                        date, underline_format)

    def about(self):
        self.main = About_Help()
        self.main.show()

    def add_habit(self):

        self.main = Add_habit(self.habit_system)
        self.main.show()

    def add_todo(self):
        self.main = Add_task(self.todo_system)
        self.main.show()

    def editclickhandler(self, habit):
        def handler():
            self.edithabit(habit)
        return handler

    def edittodoclickhandler(self, todo):
        def handler():
            self.edittodo(todo)
        return handler

    def setdoneclickhandler(self, habit):
        sound = QSoundEffect()
        sound.setSource(QUrl.fromLocalFile("resource/soundeffect1.wav"))

        def handler():
            self.habit_system.setdone(habit.name)
            self.habit_system.addleaves(3)
            sound.play()
            print(user.tree.leaves)
            self.updatetreesprite()

            # print(habit.counter)
        return handler

    def setundoneclickhandler(self, habit):
        def handler():
            self.habit_system.setundone(habit.name)
            self.habit_system.deleteleaves(3)

            print(user.tree.leaves)
            self.updatetreesprite()

        return handler

    def update_history(self, history):
        # Delete all existing buttons in habit_list
        for layout in self.ui.history.findChildren(QHBoxLayout):
            while layout.count():
                child = layout.takeAt(0)
                widget = child.widget()
                if widget is not None:
                    widget.deleteLater()
            self.historylayout.removeItem(layout)
            layout.deleteLater()

        # Loop through the habits todo: databse update
        history = history[::-1]
        for event in history:
            # Create a QPushButton for each habit
            eventButton = QPushButton(
                f"{event.habit} | {event.date.toString('yyyy-MM-dd')} | {event.time.toString('hh:mm')} | {event.type}")
            eventButton.setStyleSheet(
                "width: 200px; height: 35px; background-color: white; border-radius: 10px;"
            )

            # Create a QHBoxLayout for the habit button and the done button
            buttonLayout = QHBoxLayout()
            buttonLayout.addWidget(eventButton)

            # Add the QHBoxLayout to the main layout
            self.historylayout.addLayout(buttonLayout)

        print("update success")

    def update_habit(self, habits):
        # Delete all existing buttons in habit_list
        for layout in self.ui.habit_list.findChildren(QHBoxLayout):
            while layout.count():
                child = layout.takeAt(0)
                widget = child.widget()
                if widget is not None:
                    widget.deleteLater()
            self.habitlayout.removeItem(layout)
            layout.deleteLater()

        print(QDate.currentDate().toString("ddd").lower())

        leavestodelete = 0
        # Loop through the habits todo: databse update
        for habit in habits:
            if habit.time < QDate.currentDate() and habit.done:
                habit.done = False
                habit.time = QDate.currentDate()
                print("habit reset")

            if habit.time < QDate.currentDate() and not habit.done and QDate.currentDate(
            ).addDays(-1).toString("ddd").lower() in habit.days:

                habit.time = QDate.currentDate()
                leavestodelete += 3
                print(
                    "---------------------------habit reset, fail habit--------------------------")

            # Create a QPushButton for each habit
            habitButton = QPushButton(habit.name)
            if habit.done:
                habitButton.setStyleSheet(
                    "width: 200px; height: 35px; background-color: #596020; color: white; border-radius: 10px;"
                )
            else:
                habitButton.setStyleSheet(
                    "width: 200px; height: 35px; background-color: white; border-radius: 10px;"
                )

            habitButton.clicked.connect(self.editclickhandler(habit))

            # Create a QHBoxLayout for the habit button and the done button
            buttonLayout = QHBoxLayout()
            buttonLayout.addWidget(habitButton)

            for day in habit.days:
                if QDate.currentDate().toString("ddd").lower() == day:

                    # Create a QPushButton for setting the habit as done
                    if not habit.done:
                        doneButton = QPushButton("Done")
                        # doneButton.setChecked(False)
                        doneButton.setStyleSheet(
                            " height: 35px; padding-left: 5px; background-color: #D6CA51; color: white; border-radius: 10px;"
                        )
                        doneButton.clicked.connect(
                            self.setdoneclickhandler(habit))
                    else:
                        doneButton = QPushButton("Undo")
                        # doneButton.setChecked(True)
                        doneButton.setStyleSheet(
                            " height: 35px; padding-left: 5px; background-color: #EF8C24; border-radius: 10px;"
                        )
                        doneButton.clicked.connect(
                            self.setundoneclickhandler(habit))

                    buttonLayout.addWidget(doneButton)
                    break

            # Add the QHBoxLayout to the main layout
            self.habitlayout.addLayout(buttonLayout)

        self.habit_system.deleteleaves(leavestodelete)
        self.habit_system.update_database()

        for axis in self.chart.axes():
            self.chart.removeAxis(axis)
        self.chart.removeAllSeries()

        max_counter = max(
            (habit.counter for habit in habits if habit.counter > 0),
            default=0)
        axisx = QValueAxis()
        axisx.setMax(1.1)
        axisx.setVisible(False)
        self.chart.addAxis(axisx, Qt.AlignBottom)

        axisy = QBarCategoryAxis()
        axisy.append(
            [f"{habit.name} | {habit.counter} times" for habit in habits if habit.counter > 0])
        self.chart.addAxis(axisy, Qt.AlignLeft)
        self.chart.legend().setVisible(False)

        barSets = [(habit.name, habit.counter / (max_counter), habit.counter)
                   for habit in habits if habit.counter > 0]
        for index, (habit_name, relative_counter,
                    counter) in enumerate(barSets):
            barSet = QBarSet(habit_name)
            barSet.append(relative_counter)

            barSet.setBrush(QColor("#596020"))
            series = QHorizontalBarSeries()
            series.setBarWidth(0.5)
            series.append(barSet)
            self.chart.addSeries(series)
            series.attachAxis(axisx)

        print("update success")

    def update_todo(self, todos):
        # Delete all existing buttons in todo_list
        for layout in self.ui.todo_list.findChildren(QHBoxLayout):
            while layout.count():
                child = layout.takeAt(0)
                widget = child.widget()
                if widget is not None:
                    widget.deleteLater()
            self.habitlayout.removeItem(layout)
            layout.deleteLater()

        # Loop through the todos
        for todo in todos:
            # Create a QPushButton for each todo
            todoButton = QPushButton(todo.name)
            if todo.urgency == "Urgent":
                todoButton.setStyleSheet(
                    "width: 200px; height: 35px; background-color: #EF8C24; color: white; border-radius: 10px;"
                )
            else:
                todoButton.setStyleSheet(
                    "width: 200px; height: 35px; background-color: white; border-radius: 10px;"
                )

            todoButton.clicked.connect(self.edittodoclickhandler(todo))

            # make notifcation button

            # Create a QHBoxLayout for the todo button
            buttonLayout = QHBoxLayout()
            buttonLayout.addWidget(todoButton)

            # Add the QHBoxLayout to the main layout
            self.todolayout.addLayout(buttonLayout)

        print("update success")

    def edithabit(self, habit):
        self.main = Edit_habit(
            self.habit_system,
            habit.days,
            habit.name,
            habit.description)
        self.main.show()

    def edittodo(self, todo):
        self.main = Edit_task(
            self.todo_system,
            todo.name,
            todo.description,
            todo.urgency,
            todo.tag,
            todo.date,
            todo.time)
        self.main.show()

    def closeEvent(self, event):
        global conn
        conn.close()
        super().closeEvent(event)


class Edit_habit(QMainWindow):
    def __init__(self, habitsystem, days=[], name="", description="", time=""):
        QMainWindow.__init__(self)
        self.habitsystem = habitsystem
        self.win = None
        self.ui = Ui_edit_habit()
        self.ui.setupUi(self)
        self.days = days
        self.oldname = name
        self.ui.titletext.setText(name)
        self.ui.notetext.setText(description)
        for day in self.days:
            if day == "mon":
                self.ui.mon.setStyleSheet(
                    'background-color: #EF8C24; border-radius: 20px;')
            if day == "tue":
                self.ui.tues.setStyleSheet(
                    'background-color: #EF8C24; border-radius: 20px;')
            if day == "wed":
                self.ui.wed.setStyleSheet(
                    'background-color: #EF8C24; border-radius: 20px;')
            if day == "thu":
                self.ui.thurs.setStyleSheet(
                    'background-color: #EF8C24; border-radius: 20px;')
            if day == "fri":
                self.ui.fri.setStyleSheet(
                    'background-color: #EF8C24; border-radius: 20px;')
            if day == "sat":
                self.ui.sat.setStyleSheet(
                    'background-color: #EF8C24; border-radius: 20px;')
            if day == "sun":
                self.ui.sun.setStyleSheet(
                    'background-color: #EF8C24; border-radius: 20px;')

        self.ui.mon.clicked.connect(self.monday)
        self.ui.tues.clicked.connect(self.tuesday)
        self.ui.wed.clicked.connect(self.wednesday)
        self.ui.thurs.clicked.connect(self.thursday)
        self.ui.fri.clicked.connect(self.friday)
        self.ui.sat.clicked.connect(self.saturday)
        self.ui.sun.clicked.connect(self.sunday)
        self.ui.every.clicked.connect(self.everyday)
        self.ui.save.clicked.connect(self.edit_habit)
        self.ui.undo.clicked.connect(self.close)
        self.ui.delete_2.clicked.connect(self.delete_habit)

    def monday(self):
        if "mon" not in self.days:
            self.days.append("mon")
            self.ui.mon.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.days.remove("mon")
            self.ui.mon.setStyleSheet(
                'background-color: #596020; border-radius: 20px;')

    def tuesday(self):
        if "tue" not in self.days:
            self.days.append("tue")
            self.ui.tues.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.days.remove("tue")
            self.ui.tues.setStyleSheet(
                'background-color: #596020; border-radius: 20px;')

    def wednesday(self):
        if "wed" not in self.days:
            self.days.append("wed")
            self.ui.wed.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.days.remove("wed")
            self.ui.wed.setStyleSheet(
                'background-color: #596020; border-radius: 20px;')

    def thursday(self):
        if "thu" not in self.days:
            self.days.append("thu")
            self.ui.thurs.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.days.remove("thu")
            self.ui.thurs.setStyleSheet(
                'background-color: #596020; border-radius: 20px;')

    def friday(self):
        if "fri" not in self.days:
            self.days.append("fri")
            self.ui.fri.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.days.remove("fri")
            self.ui.fri.setStyleSheet(
                'background-color: #596020; border-radius: 20px;')

    def saturday(self):
        if "sat" not in self.days:
            self.days.append("sat")
            self.ui.sat.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.days.remove("sat")
            self.ui.sat.setStyleSheet(
                'background-color: #596020; border-radius: 20px;')

    def sunday(self):
        if "sun" not in self.days:
            self.days.append("sun")
            self.ui.sun.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.days.remove("sun")
            self.ui.sun.setStyleSheet(
                'background-color: #596020; border-radius: 20px;')

    def everyday(self):
        self.days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        self.ui.mon.setStyleSheet(
            'background-color: #EF8C24; border-radius: 20px;')
        self.ui.tues.setStyleSheet(
            'background-color: #EF8C24; border-radius: 20px;')
        self.ui.wed.setStyleSheet(
            'background-color: #EF8C24; border-radius: 20px;')
        self.ui.thurs.setStyleSheet(
            'background-color: #EF8C24; border-radius: 20px;')
        self.ui.fri.setStyleSheet(
            'background-color: #EF8C24; border-radius: 20px;')
        self.ui.sat.setStyleSheet(
            'background-color: #EF8C24; border-radius: 20px;')
        self.ui.sun.setStyleSheet(
            'background-color: #EF8C24; border-radius: 20px;')

    def delete_habit(self):
        self.habitsystem.deletehabit(self.oldname)
        self.close()

    def edit_habit(self):

        newname = self.ui.titletext.text()
        description = self.ui.notetext.toPlainText()

        if self.oldname == newname:
            if self.days == []:
                self.win = NotificationWindow("no days selected")
                self.win.show()
                print("no days selected")
            else:
                self.habitsystem.edit_habit(
                    self.oldname, newname, description, self.days)
                self.close()

        elif self.habitsystem.duplicatecheck(newname):
            self.win = NotificationWindow(
                "habit with the same name already exist")
            self.win.show()
            print("habit with the same name already exist")

        else:
            if self.days == []:
                self.win = NotificationWindow("no days selected")
                self.win.show()
                print("no days selected")
            elif newname == "":
                self.win = NotificationWindow("name cannot be empty")
                self.win.show()
                print("name cannot be empty")
            else:
                self.habitsystem.edit_habit(
                    self.oldname, newname, description, self.days)
                self.close()


class Add_habit(QMainWindow):
    def __init__(self, habitsystem):
        QMainWindow.__init__(self)
        self.habitsystem = habitsystem
        self.ui = Ui_addhabbit()
        self.ui.setupUi(self)
        self.days = []

        for day in self.days:
            if day == "mon":
                self.ui.mon.setStyleSheet(
                    'background-color: #EF8C24; border-radius: 20px;')
            if day == "tue":
                self.ui.tues.setStyleSheet(
                    'background-color: #EF8C24; border-radius: 20px;')
            if day == "wed":
                self.ui.wed.setStyleSheet(
                    'background-color: #EF8C24; border-radius: 20px;')
            if day == "thu":
                self.ui.thurs.setStyleSheet(
                    'background-color: #EF8C24; border-radius: 20px;')
            if day == "fri":
                self.ui.fri.setStyleSheet(
                    'background-color: #EF8C24; border-radius: 20px;')
            if day == "sat":
                self.ui.sat.setStyleSheet(
                    'background-color: #EF8C24; border-radius: 20px;')
            if day == "sun":
                self.ui.sun.setStyleSheet(
                    'background-color: #EF8C24; border-radius: 20px;')

        self.ui.mon.clicked.connect(self.monday)
        self.ui.tues.clicked.connect(self.tuesday)
        self.ui.wed.clicked.connect(self.wednesday)
        self.ui.thurs.clicked.connect(self.thursday)
        self.ui.fri.clicked.connect(self.friday)
        self.ui.sat.clicked.connect(self.saturday)
        self.ui.sun.clicked.connect(self.sunday)
        self.ui.every.clicked.connect(self.everyday)
        self.ui.save.clicked.connect(self.add_habit)
        self.ui.undo.clicked.connect(self.close)

    def monday(self):
        if "mon" not in self.days:
            self.days.append("mon")
            self.ui.mon.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.days.remove("mon")
            self.ui.mon.setStyleSheet(
                'background-color: #596020; border-radius: 20px;')

    def tuesday(self):
        if "tue" not in self.days:
            self.days.append("tue")
            self.ui.tues.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.days.remove("tue")
            self.ui.tues.setStyleSheet(
                'background-color: #596020; border-radius: 20px;')

    def wednesday(self):
        if "wed" not in self.days:
            self.days.append("wed")
            self.ui.wed.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.days.remove("wed")
            self.ui.wed.setStyleSheet(
                'background-color: #596020; border-radius: 20px;')

    def thursday(self):
        if "thu" not in self.days:
            self.days.append("thu")
            self.ui.thurs.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.days.remove("thu")
            self.ui.thurs.setStyleSheet(
                'background-color: #596020; border-radius: 20px;')

    def friday(self):
        if "fri" not in self.days:
            self.days.append("fri")
            self.ui.fri.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.days.remove("fri")
            self.ui.fri.setStyleSheet(
                'background-color: #596020; border-radius: 20px;')

    def saturday(self):
        if "sat" not in self.days:
            self.days.append("sat")
            self.ui.sat.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.days.remove("sat")
            self.ui.sat.setStyleSheet(
                'background-color: #596020; border-radius: 20px;')

    def sunday(self):
        if "sun" not in self.days:
            self.days.append("sun")
            self.ui.sun.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.days.remove("sun")
            self.ui.sun.setStyleSheet(
                'background-color: #596020; border-radius: 20px;')

    def everyday(self):
        self.days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        self.ui.mon.setStyleSheet(
            'background-color: #EF8C24; border-radius: 20px;')
        self.ui.tues.setStyleSheet(
            'background-color: #EF8C24; border-radius: 20px;')
        self.ui.wed.setStyleSheet(
            'background-color: #EF8C24; border-radius: 20px;')
        self.ui.thurs.setStyleSheet(
            'background-color: #EF8C24; border-radius: 20px;')
        self.ui.fri.setStyleSheet(
            'background-color: #EF8C24; border-radius: 20px;')
        self.ui.sat.setStyleSheet(
            'background-color: #EF8C24; border-radius: 20px;')
        self.ui.sun.setStyleSheet(
            'background-color: #EF8C24; border-radius: 20px;')

    def add_habit(self):
        title = self.ui.titletext.text()
        description = self.ui.notetext.toPlainText()
        # time = QDate.currentDate().addDays(-1)
        time = QDate.currentDate()
        if self.days == []:
            self.win = NotificationWindow("Please select a day")
            self.win.show()
            print("Please select a day")
        elif title == "":
            self.win = NotificationWindow("Please enter a title")
            self.win.show()
            print("Please enter a title")
        else:
            self.habitsystem.addhabit(title, description, time, self.days)
            self.close()


class Edit_task(QMainWindow):
    def __init__(
            self,
            todosystem,
            name="",
            description="",
            urgency="",
            tags=[],
            date="",
            time=""):
        QMainWindow.__init__(self)
        self.todosystem = todosystem
        self.win = None
        self.ui = Ui_edittask()
        self.ui.setupUi(self)
        self.ui.titletext.setText(name)
        self.ui.notetext.setText(description)
        self.oldname = name
        self.urgent = urgency
        self.tags = tags
        self.ui.time.setDate(date)
        self.ui.time.setTime(time)

        if "Home" in self.tags:
            self.ui.home.setStyleSheet(
                "background-color: #EF8C24; border-radius: 10px;"
            )
        if "Work" in self.tags:
            self.ui.work.setStyleSheet(
                "background-color: #EF8C24; border-radius: 10px;"
            )
        if "Errands" in self.tags:
            self.ui.errand.setStyleSheet(
                "background-color: #EF8C24; border-radius: 10px;"
            )
        if "Others" in self.tags:
            self.ui.others.setStyleSheet(
                "background-color: #EF8C24; border-radius: 10px;"
            )

        if self.urgent == "Urgent":
            self.ui.urgent_lev.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        elif self.urgent == "High":
            self.ui.high_lev.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        elif self.urgent == "Medium":
            self.ui.med_lev.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        elif self.urgent == "Low":
            self.ui.low_lev.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')

        self.ui.save.clicked.connect(self.edit_todo)
        self.ui.undo.clicked.connect(self.close)
        self.ui.dele.clicked.connect(self.delete_todo)
        self.ui.urgent_lev.clicked.connect(self.urgen)
        self.ui.high_lev.clicked.connect(self.high)
        self.ui.med_lev.clicked.connect(self.medium)
        self.ui.low_lev.clicked.connect(self.low)

        self.ui.home.clicked.connect(self.home)
        self.ui.work.clicked.connect(self.work)
        self.ui.errand.clicked.connect(self.errand)
        self.ui.others.clicked.connect(self.others)

    def urgen(self):
        print(self.urgent)
        if self.urgent == "none" or self.urgent == "Low" or self.urgent == "Medium" or self.urgent == "High":
            if self.urgent == "Low":
                self.ui.low_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')
            elif self.urgent == "Medium":
                self.ui.med_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')
            elif self.urgent == "High":
                self.ui.high_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')

            self.urgent = "Urgent"
            self.ui.urgent_lev.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.urgent = "none"
            self.ui.urgent_lev.setStyleSheet(
                'background-color: #EAE4D6; border-radius: 20px;')

    def high(self):
        print(self.urgent)
        if self.urgent == "none" or self.urgent == "Low" or self.urgent == "Medium" or self.urgent == "Urgent":
            if self.urgent == "Low":
                self.ui.low_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')
            elif self.urgent == "Medium":
                self.ui.med_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')
            elif self.urgent == "Urgent":
                self.ui.urgent_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')

            self.urgent = "High"
            self.ui.high_lev.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.urgent = "none"
            self.ui.high_lev.setStyleSheet(
                'background-color: #EAE4D6; border-radius: 20px;')

    def medium(self):
        print(self.urgent)
        if self.urgent == "none" or self.urgent == "Low" or self.urgent == "High" or self.urgent == "Urgent":
            if self.urgent == "Low":
                self.ui.low_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')
            elif self.urgent == "High":
                self.ui.high_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')
            elif self.urgent == "Urgent":
                self.ui.urgent_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')

            self.urgent = "Medium"
            self.ui.med_lev.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.urgent = "none"
            self.ui.med_lev.setStyleSheet(
                'background-color: #EAE4D6; border-radius: 20px;')

    def low(self):
        print(self.urgent)
        if self.urgent == "none" or self.urgent == "Urgent" or self.urgent == "Medium" or self.urgent == "High":
            if self.urgent == "Urgent":
                self.ui.urgent_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')
            elif self.urgent == "High":
                self.ui.high_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')
            elif self.urgent == "Medium":
                self.ui.med_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')

            self.urgent = "Low"
            self.ui.low_lev.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.urgent = "none"
            self.ui.low_lev.setStyleSheet(
                'background-color: #EAE4D6; border-radius: 20px;')

    def home(self):
        if "Home" not in self.tags:
            self.tags.append("Home")
            self.ui.home.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.tags.remove("Home")
            self.ui.home.setStyleSheet(
                'background-color: #EAE4D6; border-radius: 20px;')

    def work(self):
        if "Work" not in self.tags:
            self.tags.append("Work")
            self.ui.work.setStyleSheet(
                "background-color: #EF8C24; border-radius: 10px;"
            )
        else:
            self.tags.remove("Work")
            self.ui.work.setStyleSheet(
                "background-color: #EAE4D6; border-radius: 10px;"
            )

    def errand(self):
        if "Errands" not in self.tags:
            self.tags.append("Errands")
            self.ui.errand.setStyleSheet(
                "background-color: #EF8C24; border-radius: 10px;"
            )
        else:
            self.tags.remove("Errands")
            self.ui.errand.setStyleSheet(
                "background-color: #EAE4D6; border-radius: 10px;"
            )

    def others(self):
        if "Others" not in self.tags:
            self.tags.append("Others")
            self.ui.others.setStyleSheet(
                "background-color: #EF8C24; border-radius: 10px;"
            )
        else:
            self.tags.remove("Others")
            self.ui.others.setStyleSheet(
                "background-color: #EAE4D6; border-radius: 10px;"
            )

    def delete_todo(self):
        self.todosystem.deletetodo(self.ui.titletext.text())
        self.close()

    def edit_todo(self):
        newname = self.ui.titletext.text()
        description = self.ui.notetext.toPlainText()
        date = self.ui.time.date()
        time = self.ui.time.time()

        if self.oldname == newname:
            self.todosystem.edittodo(
                self.oldname,
                newname,
                description,
                self.urgent,
                self.tags,
                date,
                time)
            self.close()

        elif self.todosystem.duplicatescheck(newname):
            print("todo with the same name already exist")
            self.win = NotificationWindow(
                "todo with the same name already exist")
            self.win.show()

        else:
            if newname == "":
                self.win = NotificationWindow("name cannot be empty")
                self.win.show()
                print("name cannot be empty")
            else:
                self.todosystem.edittodo(
                    self.oldname,
                    newname,
                    description,
                    self.urgent,
                    self.tags,
                    date,
                    time)
                self.close()

            # if self.todosystem.checkduplicates(newname):
            #     print("habit with the same name already exist")

            # else:
            # self.todosystem.edittodo(self.oldname, newname, description, self.urgent, self.tags)
            # self.close()


class Add_task(QMainWindow):
    def __init__(self, todosystem):
        QMainWindow.__init__(self)
        self.todosystem = todosystem
        self.win = None
        self.ui = Ui_addtask()
        self.ui.setupUi(self)
        self.urgent = "none"
        self.tags = []

        self.ui.urgent_lev.clicked.connect(self.urgen)
        self.ui.high_lev.clicked.connect(self.high)
        self.ui.med_lev.clicked.connect(self.medium)
        self.ui.low_lev.clicked.connect(self.low)

        self.ui.urgent_lev.setStyleSheet(
            'background-color: #EAE4D6; border-radius: 20px;')
        self.ui.high_lev.setStyleSheet(
            'background-color: #EAE4D6; border-radius: 20px;')
        self.ui.med_lev.setStyleSheet(
            'background-color: #EAE4D6; border-radius: 20px;')
        self.ui.low_lev.setStyleSheet(
            'background-color: #EAE4D6; border-radius: 20px;')

        self.ui.home.clicked.connect(self.home)
        self.ui.work.clicked.connect(self.work)
        self.ui.errand.clicked.connect(self.errand)
        self.ui.others.clicked.connect(self.others)

        self.ui.save.clicked.connect(self.add_todo)
        self.ui.undo.clicked.connect(self.close)

    def urgen(self):
        print(self.urgent)
        if self.urgent == "none" or self.urgent == "Low" or self.urgent == "Medium" or self.urgent == "High":
            if self.urgent == "Low":
                self.ui.low_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')
            elif self.urgent == "Medium":
                self.ui.med_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')
            elif self.urgent == "High":
                self.ui.high_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')

            self.urgent = "Urgent"
            self.ui.urgent_lev.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.urgent = "none"
            self.ui.urgent_lev.setStyleSheet(
                'background-color: #EAE4D6; border-radius: 20px;')

    def high(self):
        print(self.urgent)
        if self.urgent == "none" or self.urgent == "Low" or self.urgent == "Medium" or self.urgent == "Urgent":
            if self.urgent == "Low":
                self.ui.low_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')
            elif self.urgent == "Medium":
                self.ui.med_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')
            elif self.urgent == "Urgent":
                self.ui.urgent_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')

            self.urgent = "High"
            self.ui.high_lev.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.urgent = "none"
            self.ui.high_lev.setStyleSheet(
                'background-color: #EAE4D6; border-radius: 20px;')

    def medium(self):
        print(self.urgent)
        if self.urgent == "none" or self.urgent == "Low" or self.urgent == "High" or self.urgent == "Urgent":
            if self.urgent == "Low":
                self.ui.low_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')
            elif self.urgent == "High":
                self.ui.high_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')
            elif self.urgent == "Urgent":
                self.ui.urgent_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')

            self.urgent = "Medium"
            self.ui.med_lev.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.urgent = "none"
            self.ui.med_lev.setStyleSheet(
                'background-color: #EAE4D6; border-radius: 20px;')

    def low(self):
        print(self.urgent)
        if self.urgent == "none" or self.urgent == "Urgent" or self.urgent == "Medium" or self.urgent == "High":
            if self.urgent == "Urgent":
                self.ui.urgent_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')
            elif self.urgent == "High":
                self.ui.high_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')
            elif self.urgent == "Medium":
                self.ui.med_lev.setStyleSheet(
                    'background-color: #EAE4D6; border-radius: 20px;')

            self.urgent = "Low"
            self.ui.low_lev.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.urgent = "none"
            self.ui.low_lev.setStyleSheet(
                'background-color: #EAE4D6; border-radius: 20px;')

    def home(self):
        if "Home" not in self.tags:
            self.tags.append("Home")
            self.ui.home.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.tags.remove("Home")
            self.ui.home.setStyleSheet(
                'background-color: #EAE4D6; border-radius: 20px;')

    def work(self):
        if "Work" not in self.tags:
            self.tags.append("Work")
            self.ui.work.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.tags.remove("Work")
            self.ui.work.setStyleSheet(
                'background-color: #EAE4D6; border-radius: 20px;')

    def errand(self):
        if "Errands" not in self.tags:
            self.tags.append("Errands")
            self.ui.errand.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.tags.remove("Errands")
            self.ui.errand.setStyleSheet(
                'background-color: #EAE4D6; border-radius: 20px;')

    def others(self):
        if "Others" not in self.tags:
            self.tags.append("Others")
            self.ui.others.setStyleSheet(
                'background-color: #EF8C24; border-radius: 20px;')
        else:
            self.tags.remove("Others")
            self.ui.others.setStyleSheet(
                'background-color: #EAE4D6; border-radius: 20px;')

    def add_todo(self):
        title = self.ui.titletext.text()
        if title == "":
            self.win = NotificationWindow("title is empty")
            self.win.show()
            print("title is empty")
            return
        description = self.ui.notetext.toPlainText()
        date = self.ui.time.date()
        time = self.ui.time.time()
        urgency = self.urgent
        tag = []

        for t in self.tags:
            tag.append(t)

        self.todosystem.addtodo(title, description, date, urgency, tag, time)
        self.close()


class About_Help(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_about()
        self.ui.setupUi(self)


class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.win = None
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.signup.clicked.connect(self.signup_page)
    #     self.ui.loginbutton = QPushButton("loginbutton")
        self.ui.loginbutton.clicked.connect(self.login)

        self.ui.passwordinp.setEchoMode(QLineEdit.Password)
        self.ui.showpsw.clicked.connect(self.showpsw)

    def showpsw(self):
        if self.ui.passwordinp.echoMode() == QLineEdit.Password:
            self.ui.passwordinp.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.passwordinp.setEchoMode(QLineEdit.Password)

    def login(self):
        global user
        if self.ui.usernameinp.text() == "" or self.ui.passwordinp.text() == "":
            print("username or password is empty")
            self.win = NotificationWindow("username or password is empty")
            self.win.show()
            return
        for c in root.users:
            if root.users[c].username == self.ui.usernameinp.text() and root.users[c].password == bcrypt.hashpw(
                    self.ui.passwordinp.text().encode('utf-8'), root.users[c].salt):
                user = root.users[c]
                print("login success")
                self.close()
                self.main = MainWindow(habitsystem)
                self.main.show()
                return

        print("login failed")
        self.win = NotificationWindow("login failed")
        self.win.show()

    def keyPressEvent(self, event):
        if event.key() in [Qt.Key_Enter, Qt.Key_Return]:
            self.login()

    def signup_page(self):
        self.close()
        self.main = SignupWindow()
        self.main.show()
        print("signup")
        # self.close()


class SignupWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.win = None
        self.ui = Ui_Signup()
        self.ui.setupUi(self)
        self.ui.login_btn.clicked.connect(self.login_page)
        self.ui.signupbutton.clicked.connect(self.signup)

        self.ui.passwordinp.setEchoMode(QLineEdit.Password)
        self.ui.passwordinp_2.setEchoMode(QLineEdit.Password)

    def signup(self):
        print("signup")
        if self.ui.usernameinp.text() == "" or self.ui.passwordinp.text(
        ) == "" or self.ui.passwordinp_2.text() == "":
            print("username or password is empty")
            self.win = NotificationWindow("username or password is empty")
            self.win.show()
            return

        for c in root.users:
            if root.users[c].username == self.ui.usernameinp.text():
                print("username already exist")
                self.win = NotificationWindow("username already exist")
                self.win.show()
                return

        if self.ui.passwordinp.text() != self.ui.passwordinp_2.text():
            print("password not match")
            self.win = NotificationWindow("password not match")
            self.win.show()
            return

        if self.ui.emailinp.text() == "":
            print("email is empty")
            self.win = NotificationWindow("email is empty")
            self.win.show()
            return

        if self.ui.emailinp.text().count(
                "@") != 1 or self.ui.emailinp.text().count(".") < 1:
            print("invalid email")
            self.win = NotificationWindow("invalid email")
            self.win.show()
            return

        username = self.ui.usernameinp.text()
        salt = bcrypt.gensalt()
        password = self.ui.passwordinp.text()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        mail = self.ui.emailinp.text()
        user = z_obj.User(username, salt, hashed_password, mail)
        root.users[username] = user
        print("signup success")
        transaction.commit()
        self.close()
        self.main = LoginWindow()
        self.main.show()

    def login_page(self):
        self.close()
        self.main = LoginWindow()
        self.main.show()
        print("login")
        # self.close()


class LandingPage(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LandingPage()
        self.ui.setupUi(self)

        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        self.show()

    def stop_timer_for_duration(self, duration):
        # Stop the original timer
        self.timer.stop()

        # Start a temporary timer to wait for the specified duration
        self.temp_timer = QTimer()
        self.temp_timer.singleShot(duration, self.restart_original_timer)

    def restart_original_timer(self):
        # Restart the original timer after the specified duration
        self.timer.start(35)  # Or with the desired interval

    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.main = LoginWindow()
            self.main.show()
            self.close()
        if not random.randint(1, 32) == 1:
            counter += 1
        else:
            self.stop_timer_for_duration(100)


if __name__ == '__main__':

    for c in root.users:
        obj = root.users[c]
        print(" ")

    app = QApplication(sys.argv)
    window = LandingPage()

    sys.exit(app.exec())
