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
fac = dict()
fac_list = list()
class_engaged = dict()

""" x_hours[sub] = remaining hours of sub """
a_hours = dict()
b_hours = dict()
c_hours = dict()

""" this sub-list keeps on changing based on update_subs(), get_all_subs(), get_one_sub() """
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


def create_custom():
    """ creates custon table """
    """ refers table 'subjects' """
    cur.execute('drop table if exists  custom')
    cur.execute(""" create table if not exists custom (sname varchar (20), stype varchar(20), timing int );""")
    cur.execute("""SELECT distinct sub_short_name, sub_type FROM subjects WHERE SEM = 5;""")
    for sname, stype in cur.fetchall():
        if stype in ['lab1', 'lab2', 'lab3']:
            for duplicate in range(1):
                for i in [0, 1, 4]:
                    cur.execute('insert into custom (sname, stype, timing) values(?, ?, ?)', (sname, stype, i,))
        elif stype in ['spl']:
            for duplicate in range(1):
                for i in [0, 2, 4]:
                    cur.execute('insert into custom (sname, stype, timing) values(?, ?, ?)', (sname, stype, i,))
        else:
            for duplicate in range(1):
                for i in range(1):
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
        fac[row[0]] = row[1]
        fac_list.append(row[1])
        class_engaged[row[1]] = 0

    cur.execute("SELECT sub_short_name, FAC_SHORT_NAME from view2 WHERE sec = 'B'")
    for row in cur.fetchall():
        b_fac[row[0]] = row[1]
        fac[row[0]] = row[1]
        fac_list.append(row[1])
        class_engaged[row[1]] = 0

    cur.execute("SELECT sub_short_name, FAC_SHORT_NAME from view2 WHERE sec = 'C'")
    for row in cur.fetchall():
        c_fac[row[0]] = row[1]
        fac[row[0]] = row[1]
        fac_list.append(row[1])
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


def update_subs(position, include_others=True, only_others=False):
    """ gets the data from the custom table returns shuffled list subs"""
    """ by default returns subs applicable for position """
    """ if 'include_others=False' :returns subs only applicable for perticular position """
    """ if 'only_others=True' :returns subs expect the only applicable one  """
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
    subs.clear()
    for sub2, type2 in cur.fetchall():
        d = (sub2, type2)
        subs.append(d)
    return


def decrement_hours():
    """ function that will decrement faculty engaging hours """
    # for di in class_engaged:
    #     if di[]
    for f in fac_list:
        print(f)
        if class_engaged[f] <= 0:
            pass
        else:
            class_engaged[f] -= 1
    # for f in decrement_it:
    #     print('faculty selected is ',f)
        # print('subject selected is',f)
        # print(class_engaged[fac[f]])
        # class_engaged[f] -= 1
        # print('decremented value by 1')
        # if class_engaged[fac[s]] > 0:
        #     print("decrement_hours")
        #     class_engaged[fac[s]] -= 1
        # else:
        #     print("passed")
        #     pass
def add_fac_to_decrement_it(_class_var, sub1, loop=1):
    """ adding faculty who are engaging class to decrement list"""
    for i in range(loop):
        if _class_var == 'a':
            decrement_it.append(a_fac[sub1])
        if _class_var == 'b':
            decrement_it.append(b_fac[sub1])
        if _class_var == 'c':
            decrement_it.append(c_fac[sub1])


create_custom()
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
""" dictionary of list  """
labs_done = dict()
labs_done = {'a':[], 'b':[], 'c':[]}


def get_one_sub(position, include_others=True, only_others=False, return_type=False):
    update_subs(position, include_others=include_others, only_others=only_others)
    for sub2, type2 in subs:
        if class_engaged[fac[sub2]]:
            continue
        if return_type:
            return sub2, type2
        return sub2


def get_all_subs(position, include_others=True, only_others=False):
    update_subs(position, include_others=include_others, only_others=only_others)
    return


def Spl(sub1, position):
    print("apti")
    """ return value zero represents any sub is not appended to any class"""
    """ return vale 1, spl subject is appended to all the class """
    if is_spl_done_for_week:
        return 0
    highest = max(sem5.pos_a, sem5.pos_b, sem5.pos_c)
    if highest in [0, 2, 4]:
        for loop in range(highest - sem5.pos_a):
            if sem5.pos_a < highest:
                sub2 = get_one_sub(position, only_others=True)
                a.append(sub2)
                print(sub2)
                class_engaged[a_fac[sub2]] += 1
                a_hours[sub2] -= 1
                sem5.pos_a += 1
        for loop in range(highest - sem5.pos_b):
            if sem5.pos_b < highest:
                sub2 = get_one_sub(position, only_others=True)
                b.append(sub2)
                print(sub2)
                class_engaged[b_fac[sub2]] += 1
                b_hours[sub2] -= 1
                sem5.pos_b += 1
        for loop in range(highest - sem5.pos_c):
            if sem5.pos_c < highest:
                sub2 = get_one_sub(position, only_others=True)
                c.append(sub2)
                print(sub2)
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
    return -1



def xyz(position, sub1, type1, sec, _class_var):
    diff = 0
    for lb in labs_done.get(_class_var):
        if sub1 in lb:
            return position, diff
        else:
            pass
    if type1 in ['lab1', 'lab2', 'lab3']:
        if list_engaging_labs[type1] < 2:
            if position + 3 <= 7:
                #print("position + 3 ", position + 3)
                for diff in range(3):
                    sec.append(sub1)
                    position += 1
            # print(sub1)
            # print(sec)
                if _class_var == 'a':
                    labs_done['a'].append(sub1)
                if _class_var == 'b':
                    labs_done['b'].append(sub1)
                if _class_var == 'c':
                    labs_done['c'].append(sub1)
                list_engaging_labs[type1] += 1
                """ adding faculty who are engaging class to decrement list"""
                add_fac_to_decrement_it(_class_var, sub1, loop=3)
                return position, diff+1
        else:
            get_all_subs(position, include_others=False)
            for sub1, type1 in subs:
                if type1 not in ['spl'] and list_engaging_labs[type1] < 2:
                    for lb in labs_done.get(_class_var):
                        if sub1 in lb:
                            continue
                        else:

                            if position + 3 <= 7:
                                list_engaging_labs[type1] += 1
                                add_fac_to_decrement_it(_class_var, sub1, loop=3)
                                for diff in range(3):
                                    sec.append(sub1)
                                    position += 1
                                if _class_var == 'a':
                                    labs_done['a'].append(sub1)
                                if _class_var == 'b':
                                    labs_done['b'].append(sub1)
                                if _class_var == 'c':
                                    labs_done['c'].append(sub1)
                    return position, diff+1
            return position, diff+1
    else:
        sec.append(sub1)
        position += 1
        add_fac_to_decrement_it(_class_var, sub1)
        return position, 1


class time_table:
    for day in range(3):
        i = 0
        sem5.pos_a = 0
        sem5.pos_b = 0
        sem5.pos_c = 0
        a.clear()
        b.clear()
        c.clear()
        for hour in range(7):
            print()
            print("loop", hour + 1)
            if isinstance(sem5.pos_a, int) and sem5.pos_a < 7:
                update_subs(sem5.pos_a)
                shuffle(subs)
                for sub in subs:
                    sub1 = sub[0]
                    type1 = sub[1]
                    print("subject selected for a ", sub1)
                    if class_engaged[a_fac[sub1]]:
                        continue
                    if type1 in ['spl']:
                        if is_spl_done_for_week:
                            continue
                        return_val = Spl(sub1, sem5.pos_a)
                        is_spl_done_for_week = True
                        break
                    else:
                        if a_hours[sub1]:
                            sem5.pos_a, diff = xyz(sem5.pos_a, sub1, type1, a, 'a')
                            class_engaged[a_fac[sub1]] += diff
                            a_hours[sub1] -= diff
                        break

            if isinstance(sem5.pos_b, int) and sem5.pos_b < 7:
                update_subs(sem5.pos_b)
                shuffle(subs)
                for sub in subs:
                    sub1 = sub[0]
                    type1 = sub[1]
                    print("subject selected for b ", sub1)
                    if class_engaged[b_fac[sub1]]:
                        continue
                    if type1 in ['spl']:
                        if is_spl_done_for_week:
                            continue
                        return_val = Spl(sub1, sem5.pos_b)
                        is_spl_done_for_week = True
                        break
                    else:
                        if b_hours[sub1]:
                            sem5.pos_b, diff = xyz(sem5.pos_b, sub1, type1, b, 'b')
                            class_engaged[b_fac[sub1]] += diff
                            b_hours[sub1] -= diff
                        break

            if isinstance(sem5.pos_c, int) and sem5.pos_c < 7:
                update_subs(sem5.pos_c)
                shuffle(subs)
                for sub in subs:
                    sub1 = sub[0]
                    type1 = sub[1]
                    print("subject selected for c ", sub1)
                    if class_engaged[c_fac[sub1]]:
                        continue
                    if type1 in ['spl']:
                        if is_spl_done_for_week:
                            continue
                        return_val = Spl(sub1, sem5.pos_c)
                        is_spl_done_for_week = True
                        break
                    else:
                        if c_hours[sub1]:
                            sem5.pos_c, diff = xyz(sem5.pos_c, sub1, type1, c, 'c')
                            class_engaged[c_fac[sub1]] += diff
                            c_hours[sub1] -= diff
                        break
            print(a)
            print(sem5.pos_a)
            print(b)
            print(sem5.pos_b)
            print(c)
            print(sem5.pos_c)
            print(decrement_it)
            print(class_engaged)
            decrement_hours()
            decrement_it.clear()
            print(class_engaged)