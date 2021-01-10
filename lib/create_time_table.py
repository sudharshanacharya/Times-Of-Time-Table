import sqlite3
from lib.queries import queries

conn = sqlite3.connect("database/TimesOfTimeTable.db")
cur = conn.cursor()
cur.execute("""SELECT sub_short_name FROM subjects WHERE SEM = 5;""")
subs = list()
for row in cur.fetchall():
    subs.append(row[0])
print("subjects : ", subs)

a_fac = []

cur.execute(queries.get_a_fac)

# print(a_fac)

""" create a view by joining table 'sub_fac' & 'faculty' table """
""" select fac_short_name & rem hours """
""" store it in a dictionary """
""" a_fac = {"plk" : 5, "sup": 5, "mr" : 4 }"""
""" add faculty to "a_sec" dictionary & decrement ; make a_fac["fac"] -=1 """
""" make class_engaged[fac] = 1 """
""" check if class_engaegd[b_fac[i]] == 1;  if so swap assign to b_sec; make class_engaged[swaped_fac] = 1"""
""" after each itteraiton release faculties"""

a_fac = dict()
b_fac = dict()
c_fac = dict()
class_engaged = dict()


def initialize_fac():
    cur.execute(queries.view1)
    cur.execute("SELECT FAC_SHORT_NAME, rem_hours from view1 WHERE sec = 'A'")
    for row in cur.fetchall():
        a_fac[row[0]] = row[1]
        class_engaged[row[0]] = 0
    cur.execute("SELECT FAC_SHORT_NAME, rem_hours from view1 WHERE sec = 'B'")
    for row in cur.fetchall():
        b_fac[row[0]] = row[1]
        class_engaged[row[0]] = 0
    cur.execute("SELECT FAC_SHORT_NAME, rem_hours from view1 WHERE sec = 'C'")
    for row in cur.fetchall():
        c_fac[row[0]] = row[1]
        class_engaged[row[0]] = 0


initialize_fac()

print(a_fac)
print(b_fac)
print(c_fac)
print(class_engaged)