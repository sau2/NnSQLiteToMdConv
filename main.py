"""
Convert Nimbus Notes DB to MD
"""


from markdownify import markdownify as md
import json, os, shutil, re, sqlite3


def nimbusNoteDbToMdConv():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("База данных создана и успешно подключена к SQLite")

        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        print("Версия базы данных SQLite: ", record)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    return


def from_nnf():
    import base64

    f = open('D://sau//PJ//NimbusNotes//NN//Notes//1DYHVjXl4uzaw7Si.nnf', 'r', encoding="ansi")
    print(base64.b64decode(f.read()))


from_nnf()