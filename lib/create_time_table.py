import sqlite3
import random
from lib.queries import queries

conn = sqlite3.connect("database/TimesOfTimeTable.db")
cur = conn.cursor()

""" x_fac[sub] = sub faculty for class x """
a_fac = dict()
b_fac = dict()
c_fac = dict()
class_engaged = dict()

""" x_hours[sub] = remaining hours of sub """
a_hours = dict()
b_hours = dict()
c_hours = dict()

""" list of subjects """
subs = list()

""" """

def get_subs():
    cur.execute("""SELECT sub_short_name FROM subjects WHERE SEM = 5;""")
    for row in cur.fetchall():
        subs.append(row[0])


def init_fac():
    cur.execute(queries.view1)
    cur.execute("SELECT sub_short_name, FAC_SHORT_NAME from view2 WHERE sec = 'A'")
    for row in cur.fetchall():
        a_hours[row[0]] = row[1]
        class_engaged[row[1]] = 0
    cur.execute("SELECT sub_short_name, FAC_SHORT_NAME from view2 WHERE sec = 'B'")
    for row in cur.fetchall():
        b_hours[row[0]] = row[1]
        class_engaged[row[1]] = 0
    cur.execute("SELECT sub_short_name, FAC_SHORT_NAME from view2 WHERE sec = 'C'")
    for row in cur.fetchall():
        c_hours[row[0]] = row[1]
        class_engaged[row[1]] = 0


def init_sub():
    """ hello """
    cur.execute(queries.view1)
    cur.execute("SELECT SUB_SHORT_NAME, rem_hours from view2 WHERE sec = 'A'")
    for row in cur.fetchall():
        a_fac[row[0]] = row[1]
    cur.execute("SELECT SUB_SHORT_NAME, rem_hours from view2 WHERE sec = 'B'")
    for row in cur.fetchall():
        b_fac[row[0]] = row[1]
    cur.execute("SELECT SUB_SHORT_NAME, rem_hours from view2 WHERE sec = 'C'")
    for row in cur.fetchall():
        c_fac[row[0]] = row[1]


class time_table:
    """ methods used to create time table """
    """ create a view by joining table 'sub_fac' & 'faculty' table """
    """ select fac_short_name & rem hours """
    """ store it in a dictionary """
    """ a_fac = {"plk" : 5, "sup": 5, "mr" : 4 }"""
    """ add faculty to "a_sec" dictionary & decrement ; make a_fac["fac"] -=1 """
    """ make class_engaged[fac] = 1 """
    """ check if class_engaged[b_fac[i]] == 1;  if so swap assign to b_sec; make class_engaged[swapped_fac] = 1"""
    """ after each iteration release faculties"""

    """" shuffle a_fac, b_fab, c_fac after each day """

    """ note: steps may have changed """


init_fac()
init_sub()

a_mon = list()
b_mon = list()
c_mon = list()

for sub in subs:
    a_mon.append(sub)

print(a_mon)
print(a_hours['atc'])
print(class_engaged[a_fac['atc']])
