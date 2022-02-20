import sqlite3

dbLocation = './DataBase/btb.db'


# 获取用户名
def getMailAddr():
    try:
        db = sqlite3.connect(dbLocation)
    except:
        print('can not open database')
        return
    cursor = db.cursor()
    command = "SELECT * FROM btb WHERE Setting = 'mailAddr';"
    cursor.execute(command)
    result = cursor.fetchone()
    if result[1] is not None:
        db.close()
        return result[1]
    else:
        db.close()
        return - 1  # 权限错误


# 获取密码
def getPassWord():
    try:
        db = sqlite3.connect(dbLocation)
    except:
        print('can not open database')
        return
    cursor = db.cursor()
    command = "SELECT * FROM btb WHERE Setting = 'passWd';"
    cursor.execute(command)
    result = cursor.fetchone()
    if result[1] is not None:
        db.close()
        return result[1]
    else:
        db.close()
        return - 1  # 权限错误


# 获取论坛网址
def getForumsURL():
    try:
        db = sqlite3.connect(dbLocation)
    except:
        print('can not open database')
        return
    cursor = db.cursor()
    command = "SELECT * FROM btb WHERE Setting = 'ForumsURL';"
    cursor.execute(command)
    result = cursor.fetchone()
    db.close()
    return result[1]


# 获取aDashBoard网址
def getAdURL():
    try:
        db = sqlite3.connect(dbLocation)
    except:
        print('can not open database')
        return
    cursor = db.cursor()
    command = "SELECT * FROM btb WHERE Setting = 'AdURL';"
    cursor.execute(command)
    result = cursor.fetchone()
    db.close()
    return result[1]


# 获取jabber用户名
def getJabberName():
    try:
        db = sqlite3.connect(dbLocation)
    except:
        print('can not open database')
        return
    cursor = db.cursor()
    command = "SELECT * FROM btb WHERE Setting = 'jabberName';"
    cursor.execute(command)
    result = cursor.fetchone()
    fromjid = result[1]
    command = "SELECT * FROM btb WHERE Setting = 'jabberServer';"
    cursor.execute(command)
    result = cursor.fetchone()
    db.close()
    fromjid = fromjid + '@' + result[1]
    return fromjid

def getBotJid():
    try:
        db = sqlite3.connect(dbLocation)
    except:
        print('can not open database')
        return
    cursor = db.cursor()
    command = "SELECT * FROM btb WHERE Setting = 'botJid';"
    cursor.execute(command)
    result = cursor.fetchone()
    db.close()
    botJid = result[1]
    return botJid