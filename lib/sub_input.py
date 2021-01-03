import sqlite3
from lib.queries import queries


class sub:
    """take subject detail, Enters into subject database"""


def sub_input(no_sub, drop_table = False, create_table = False):
    conn = sqlite3.connect("database/TimesOfTimeTable.db")
    cur = conn.cursor()
    if drop_table == True:
        cur.execute("drop table if EXISTS subjects ")
        print("Table Droped")
    if create_table == True:
        cur.execute(queries.create_table_subjects)

    for i in range(no_sub):
        print("subject (?)", i)
        sub_name = input("Enter sub_nam: ")
        sub_short_name = input("Enter sub_short_name: ")
        sub_code = input("Enter sub_code: ")
        sub_credit = input("Enter sub_credit: ")
        sub_type = input("Enter sub_type: ")

        cur.execute("""
        insert into subjects (sub_short_name,sub_name, sub_code, sub_credit, sub_type)
        values(?,?,?,?,?)
        """, (sub_short_name, sub_name, sub_code, sub_credit, sub_type,))

    conn.commit()
    conn.close()
