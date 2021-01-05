from lib.queries import queries
import sqlite3



def fac_input(no_sub, drop_table = False, create_table = False):
    """takes faculty detail enters into faculty database"""
    conn = sqlite3.connect("database/TimesOfTimeTable.db")
    cur = conn.cursor()
    if drop_table:
        queries.drop_table('faculty')
        # cur.execute("drop table if EXISTS subjects ")
        print("Table Dropped")
    if create_table:
        cur.execute(queries.create_table_faculties)

        cur.execute("""
        insert into subjects (sub_short_name,sub_name, sub_code, sub_credit, sub_type)
        values(?,?,?,?,?)
        """, (sub_short_name, sub_name, sub_code, sub_credit, sub_type,))

    conn.commit()
    conn.close()
