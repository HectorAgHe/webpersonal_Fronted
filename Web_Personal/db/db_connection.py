import pymysql

def get_connection():
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='123456',
                                db='web_personal',
                                cursorclass=pymysql.cursors.DictCursor)

    return connection
    