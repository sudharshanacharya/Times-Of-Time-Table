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

""" list of faculty, who are engaging classes now & who's 'class_engaged' will be decremented """
decrement_it = list()

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
if_lab.append('spl')


def get_subs():
    """ refers table 'subjects' """
    cur.execute('drop table if exists  custom')
    cur.execute(""" create table if not exists custom (sname varchar (20), stype varchar(20), timing int );""")
    cur.execute("""SELECT sub_short_name, sub_type FROM subjects WHERE SEM = 5;""")
    for sname, stype in cur.fetchall():
        if stype in ['lab1', 'lab2', 'lab3']:
            print(sname)
            for i in [0, 1, 4]:
                cur.execute('insert into custom (sname, stype, timing) values(?, ?, ?)', (sname, stype, i,))
        elif stype in ['spl']:
            for i in [0, 2, 4]:
                cur.execute('insert into custom (sname, stype, timing) values(?, ?, ?)', (sname, stype, i,))
        else:
            for i in range(7):
                cur.execute('insert into custom (sname, stype, timing) values(?, ?, ?)', (sname, stype,i,))
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


def sub_rearrange(dic):
    def func(e):
        return e[1]  # to sort by 2nd element

    li = dic.items()  # returns list of tuples
    li = list(li)  # make it exactly list
    li.sort(reverse=True, key=func)
    dic = dict(li)
    return dic


def decrement_hours():
    """ funciton that will faculty engaging hours """
    for s in decrement_it:
        class_engaged[s] -= 1


get_subs()
init_fac()
print(class_engaged)
init_sub_hours()
print(subs)
a = list()
b = list()
c = list()

list_engaging_labs = {'lab1' : 2, 'lab2': 2, 'lab3' : 2}
class spl():
    is_spl_done_for_week = False
spl = spl()

def xyz(posiiton, sec):
    cur.execute('select distinct sname, stype from custom where timing = ?', (posiiton,))
    for sub2, type2 in cur.fetchall():
        d = (sub2, type2)
        subs.append(d)
    shuffle(subs)
    """ sub_d -> single subject dictionary """
    for sub1, type1 in subs:
        if class_engaged[a_fac[sub1]]:
            continue
        print(sub1, type1)
        if type1 in ['lab1', 'lab2', 'lab3']:
            if list_engaging_labs[type1] < 2:
                if sec == 'a' and a_hours[sub1]:
                    for i in range(3):
                        a.append(sub1)
                        class_engaged[a_fac[sub1]] += 1
                        print("class engaged", class_engaged[a_fac[sub1]])
                        a_hours[sub1] -= 1
                        posiiton += 1
                    return posiiton
                if sec == 'b' and b_hours[sub1]:
                    for i in range(3):
                        b.append(sub1)
                        class_engaged[b_fac[sub1]] += 1
                        b_hours[sub1] -= 1
                        posiiton += 1
                    return posiiton
                if sec == 'c' and c_hours[sub1]:
                    for i in range(3):
                        c.append(sub1)
                        class_engaged[c_fac[sub1]] += 1
                        c_hours[sub1] -= 1
                        posiiton += 1
                    return posiiton
                list_engaging_labs[type1] += 1
            else:
                continue
        if type1 in ['spl']:
            if not spl.is_spl_done_for_week:
                continue
                for i in range(2):
                    a.append(sub1)
                    b.append(sub1)
                    c.append(sub1)
                    posiiton += 1
                    spl.is_spl_done_for_week = True
                return posiiton
        else:
            if sec == 'a' and a_hours[sub1]:
                a.append(sub1)
                a_hours[sub1] -= 1
                posiiton += 1
                class_engaged[a_fac[sub1]] += 1
                return posiiton
            if sec == 'b' and b_hours[sub1]:
                b.append(sub1)
                b_hours[sub1] -= 1
                posiiton += 1
                class_engaged[b_fac[sub1]] += 1
                return posiiton
            if sec == 'c' and c_hours[sub1]:
                c.append(sub1)
                c_hours[sub1] -= 1
                posiiton += 1
                class_engaged[c_fac[sub1]] += 1
                return posiiton
    posiiton += 1
    return



class time_table:
    for day in range(1):
        i = 0
        pos_a = i
        pos_b = i
        pos_c = i
        for i in range(7):
            if pos_c < 7 and pos_b< 7 and pos_a< 7:
                print(i)
                pos_a = xyz(pos_a, sec='a')
                print("updated", i)
                pos_b = xyz(pos_b, sec='b')
                pos_c = xyz(pos_c, sec='c')
            else:
                break


print(a)
print(b)
print(c)
print(class_engaged)
