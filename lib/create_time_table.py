""" picks subject from subs list if the sub not present sub_fac table then creates error """

import sqlite3
from random import shuffle
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
    """ refers table 'subjects' """
    cur.execute("""SELECT sub_short_name FROM subjects WHERE SEM = 5;""")
    for row in cur.fetchall():
        subs.append(row[0])


def init_fac():
    """ refers view2, lib/queries.py """
    """ x_fac[sub] = sub faculty for class x """
    """ initializes class_engaged[fac] to 0 """
    cur.execute(queries.view2)
    cur.execute("SELECT sub_short_name, FAC_SHORT_NAME from view2 WHERE sec = 'A'")
    for row in cur.fetchall():
        a_fac[row[0]] = row[1]
        class_engaged[row[1]] = 0

    cur.execute("SELECT sub_short_name, FAC_SHORT_NAME from view2 WHERE sec = 'B'")
    for row in cur.fetchall():
        b_fac[row[0]] = row[1]
        class_engaged[row[1]] = 0

    cur.execute("SELECT sub_short_name, FAC_SHORT_NAME from view2 WHERE sec = 'C'")
    for row in cur.fetchall():
        c_fac[row[0]] = row[1]
        class_engaged[row[1]] = 0


def init_sub_hours():
    """ refers view2, lib/queries.py """
    """ x_hours[sub] = remaining hours of sub """
    cur.execute(queries.view2)
    cur.execute("SELECT SUB_SHORT_NAME, rem_hours from view2 WHERE sec = 'A'")
    for row in cur.fetchall():
        a_hours[row[0]] = row[1]
    cur.execute("SELECT SUB_SHORT_NAME, rem_hours from view2 WHERE sec = 'B'")
    for row in cur.fetchall():
        b_hours[row[0]] = row[1]
    cur.execute("SELECT SUB_SHORT_NAME, rem_hours from view2 WHERE sec = 'C'")
    for row in cur.fetchall():
        c_hours[row[0]] = row[1]


def sub_rearrange(dic):
    def func(e):
        return e[1]  # to sort by 2nd element

    li = dic.items()  # returns list of tuples
    li = list(li)  # make it exactly list
    li.sort(reverse=True, key=func)
    dic = dict(li)
    return dic


get_subs()
init_fac()
init_sub_hours()

a = list()
b = list()
c = list()


# print("a hours", a_hours)


# print("a facs", a_fac)

class time_table:
    """ methods used to create time table """
    """ create a view by joining table 'sub_fac' & 'faculty' and 'subjects'table """
    """ select fac_short_name & rem hours """
    """ store it in a dictionary """
    """ a_fac = {"plk" : 5, "sup": 5, "mr" : 4 }"""
    """ add faculty to "a_sec" dictionary & decrement ; make a_fac["fac"] -=1 """
    """ make class_engaged[fac] = 1 """
    """ check if class_engaged[b_fac[i]] == 1;  if so swap assign to b_sec; make class_engaged[swapped_fac] = 1"""
    """ after each iteration release faculties"""
    """" shuffle list subs after each day """
    """ re-arrange x_hours list based to remaining hours in descending order after each day"""
    """ """

    """ note: steps may have changed """

    for day in range(1):
        """"""
        shuffle(subs)
        i = 0
        for sub in subs:
            i += 1

            if a_hours[subs] > 0:
                a.append(sub)
                a_hours[sub] -= 1
                class_engaged[a_fac[sub]] = 1
                print("appended to A sec")
                print(sub)

            """ for sec b """
            if b_hours[sub] > 0 and not class_engaged[b_fac[sub]]:
                b.append(sub)
                b_hours[sub] -= 1
                class_engaged[a_fac[sub]] = 1
                print("appended to B sec")
            else:
                """ shuffle subjects """
                for j in range(len(subs) - i):
                    if class_engaged[b_fac[subs[i + j]]]:
                        continue
                    else:
                        b.append(subs[i + j])
                        b_hours[subs[i + j]] -= 1
                        print("appended to B sec after swapping")

            """ for sec c """
            if c_hours[sub] > 0 and not class_engaged[c_fac[sub]]:
                c.append(sub)
                c_hours[sub] -= 1
                print("appended to C sec")
            else:
                """ shuffle subjects """
                for j in range(len(subs) - i):
                    if class_engaged[c_fac[subs[i + j]]]:
                        continue
                    else:
                        c.append(subs[i + j])
                        c_hours[subs[i + j]] -= 1
                        print("appended to C sec after swapping")
            #print(class_engaged)
            #class_engaged = dict.fromkeys(class_engaged, 0)
            #print(class_engaged)



time_table
print(a)
print(a_hours)
print()
print(b)
print(b_hours)
print()
print(c)
print(c_hours)