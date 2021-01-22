from lib.queries import queries
import sqlite3



def fac_input(no_sub = None, drop_table = False, create_table = False):
    """takes faculty detail enters into faculty database"""
    conn = sqlite3.connect("database/TimesOfTimeTable.db")
    cur = conn.cursor()
    if drop_table:
        queries.drop_table('faculty')
        # cur.execute("drop table if EXISTS subjects ")
        print("Table Dropped")
    if create_table:
        cur.execute(queries.create_table_faculties)

    no_fac = input("Enter the number of faculty")
    for i in range(int(no_fac)):
        fac_name = input("Enter the faculty full name")
        fac_short_name = input("Enter facutly short name")
        cur.execute('insert into faculty (fac_short_name, fac_name) values(?,?)', (fac_short_name, fac_name,))

    conn.commit()
    conn.close()


fac_input()