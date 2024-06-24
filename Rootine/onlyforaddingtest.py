import ZODB, ZODB.config
import BTrees.OOBTree
import persistent
import transaction
import z_obj
from PySide6.QtCore import QDate



path = './config.xml'
db = ZODB.config.databaseFromURL(path)
conn = db.open()
root = conn.root
# temp = root.users["tin"].habitList
# temp.append(z_obj.Habit("tin", "tin", QDate.currentDate().addDays(-1), ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]))
# root.users["tin"].habitList = temp

root.users["tin"].habitList.append(z_obj.Habit("FAILTEST", "FAILTEST", QDate.currentDate().addDays(-1), ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]))
root.users["tin"]._p_changed = True


transaction.commit()
print("added habit to tin")