import pymysql

def get_connection():
    connection = pymysql.connect(hots='localhotst',
                                user='root',
                                passwd='',
                                db='web_personal',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.Dictcursor)

    return connection
    