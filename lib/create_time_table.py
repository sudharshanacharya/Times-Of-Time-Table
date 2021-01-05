import sqlite3

conn = sqlite3.connect("database/TimesOfTimeTable.db")
cur = conn.cursor()
cur.execute("""SELECT sub_short_name FROM subjects WHERE SEM = 5;""")
subs = list()
for row in cur.fetchall():
    subs.append(row[0])
print(subs)