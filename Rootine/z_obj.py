import ZODB
import ZODB.config
import persistent
from abc import ABC, abstractmethod
from PySide6.QtCore import QDate


class User(persistent.Persistent):
    def __init__(self, username, salt, password, email):
        self.username = username
        self.salt = salt
        self.password = password
        self.habitList = []
        self.todoTask = []
        self.tree = Tree()
        self.email = email
        self.History = []  # list of events


class Tree(persistent.Persistent):
    def __init__(self):
        self.leaves = 0

    def addLeave(self, value):
        self.leaves += value

    def deleteLeave(self, value):
        if value > self.leaves:
            self.leaves = 0
        else:
            self.leaves = self.leaves - value


class Habit(persistent.Persistent):
    def __init__(self, name, description, time, days):
        self.name = name
        self.description = description
        self.counter = 0
        self.done = False
        self.time = time
        self.days = days


class TodoTask(persistent.Persistent):
    def __init__(self, name, description, date, urgency, tag, time):
        self.name = name
        self.description = description
        self.date = date
        self.time = time
        self.urgency = urgency
        self.tag = tag


class Event(persistent.Persistent):
    def __init__(self, habit, date, time, type):
        self.habit = habit
        self.date = date
        self.time = time
        self.type = type
