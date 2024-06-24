import ZODB, ZODB.config
import z_obj
import transaction


path = './config.xml'
db = ZODB.config.databaseFromURL(path)
conn = db.open()
root = conn.root

if __name__ == '__main__':
    root.users['tin'] = z_obj.User('tin', '123')
    print("Successfully added user!")


transaction.commit()