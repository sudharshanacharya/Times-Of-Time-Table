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

""" list of lab engaged """
lab_not_engaged = list()
lab_not_engaged.append('lab1')
lab_not_engaged.append('lab2')
lab_not_engaged.append('lab3')

""" not usual class hours"""
if_lab = list()
if_lab.append('lab1')
if_lab.append('lab2')
if_lab.append('lab3')
if_lab = list()
if_lab.append('spl')

""" list of faculty, who are engaging classes now & who's 'class_engaged' will be decremented """
decrement_it = list()


def get_subs():
    """ creates custon table """
    """ refers table 'subjects' """
    cur.execute('drop table if exists  custom')
    cur.execute(""" create table if not exists custom (sname varchar (20), stype varchar(20), timing int );""")
    cur.execute("""SELECT sub_short_name, sub_type FROM subjects WHERE SEM = 5;""")
    for sname, stype in cur.fetchall():
        if stype in ['lab1', 'lab2', 'lab3']:
            print(sname)
            for duplicate in range(2):
                for i in [0, 1, 4]:
                    cur.execute('insert into custom (sname, stype, timing) values(?, ?, ?)', (sname, stype, i,))
        elif stype in ['spl']:
            for duplicate in range(2):
                for i in [0, 2, 4]:
                    cur.execute('insert into custom (sname, stype, timing) values(?, ?, ?)', (sname, stype, i,))
        else:
            for duplicate in range(2):
                for i in range(7):
                    cur.execute('insert into custom (sname, stype, timing) values(?, ?, -1)', (sname, stype,))
        conn.commit()


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


def sub_rearrange(position, include_others=True, only_others=False):
    """ gets the data from the custom table returns shuffled list subs"""
    # def func(e):
    #   return e[1]  # to sort by 2nd element

    # li = dic.items()  # returns list of tuples
    # li = list(li)  # make it exactly list
    # li.sort(reverse=True, key=func)
    # dic = dict(li)
    # return dic
    if only_others:
        cur.execute('select sname, stype from custom where timing = ?', (-1,))
    elif include_others:
        cur.execute('select sname, stype from custom where timing = ? or timing = ?', (position, -1,))
    else:
        cur.execute('select sname, stype from custom where timing = ?', (position,))

    for sub2, type2 in cur.fetchall():
        d = (sub2, type2)
        subs.append(d)
    return shuffle(subs)


def decrement_hours():
    """ funciton that will faculty engaging hours """
    for s in decrement_it:
        class_engaged[s] -= 1


get_subs()
init_fac()
init_sub_hours()

a = list()
b = list()
c = list()

list_engaging_labs = {'lab1': 0, 'lab2': 0, 'lab3': 0}


class positions_of_class():
    def __init__(self):
        self.pos_b = None
        self.pos_a = None
        self.pos_c = None

    """"""


sem5 = positions_of_class()
is_spl_done_for_week = False


def get_one_sub(position):
    subs = sub_rearrange(position, only_others=True)
    for sub2, type2 in subs:
        if class_engaged[sub2]:
            continue
        decrement_it.append(sub2)
        return sub2


def Spl(sub1, position):
    highest = max(sem5.pos_a, sem5.pos_b, sem5.pos_c)
    if highest in [0, 2, 4]:
        for loop in (highest - sem5.pos_a):
            if sem5.pos_a < highest:
                sub2 = get_one_sub(position)
                a.append(sub2)
                class_engaged[a_fac[sub2]] += 1
                a_hours[sub2] -= 1
                sem5.pos_a += 1

            if sem5.pos_b < highest:
                sub2 = get_one_sub(position)
                b.append(sub2)
                class_engaged[b_fac[sub2]] += 1
                b_hours[sub2] -= 1
                sem5.pos_b += 1

            if sem5.pos_c < highest:
                sub2 = get_one_sub(position)
                c.append(sub2)
                class_engaged[c_fac[sub2]] += 1
                c_hours[sub2] -= 1
                sem5.pos_c += 1

        for i in range(2):
            a.append(sub1)
            b.append(sub1)
            c.append(sub1)
            class_engaged[b_fac[sub1]] += 1
            sem5.pos_a += 1
            sem5.pos_b += 1
            sem5.pos_c += 1
            a_hours[sub1] -= 1
            b_hours[sub1] -= 1
            c_hours[sub1] -= 1
        return 0
    return 1

def xyz(position, sub1, type1, sec):
    if type1 in ['lab1', 'lab2', 'lab3']:
        if list_engaging_labs[type1] < 2:
            for i in range(3):
                sec.append(sub1)
                class_engaged[a_fac[sub1]] += 1
                a_hours[sub1] -= 1
                position += 1


class time_table:
    for day in range(1):
        i = 0
        sem5.pos_a = 0
        sem5.pos_b = 0
        sem5.pos_c = 0
        for i in range(7):
            print("loop", i)

            if isinstance(sem5.pos_a, int) and sem5.pos_a < 7:
                subs = sub_rearrange()
                print("subjects which are in the position ", sem5.pos_a, " are selected from the database ")
                print('a position', sem5.pos_a)
                for sub1, type1 in subs:
                    if class_engaged[a_fac[sub1]]:
                        continue
                    if type1 in ['spl']:
                        return_val = Spl(sem5.pos_a)
                    else:
                        sem5.pos_a = sem5.pos_a + xyz(sem5.pos_a, sub1, type1)

                sem5.pos_a = sem5.pos_a + xyz(sem5.pos_a, sec='a')
            print()

            if isinstance(sem5.pos_b, int) and sem5.pos_b < 7:
                print('b position', sem5.pos_b)
                sem5.pos_b = sem5.pos_b + xyz(sem5.pos_b, sec='b')
            print()

            if isinstance(sem5.pos_c, int) and sem5.pos_c < 7:
                print('c position', sem5.pos_c)
                sem5.pos_c = sem5.pos_c + xyz(sem5.pos_c, sec='c')
            decrement_hours()
            print()
            print()


print(a)
print(b)
print(c)
print(class_engaged)
print(list_engaging_labs)
