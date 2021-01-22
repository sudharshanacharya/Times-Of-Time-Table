""" picks subject from subs list if the sub not present sub_fac table then creates error """
""" now you can remove decrement it fuction """

import sqlite3
from random import shuffle
from lib.queries import queries

list_engaging_labs = {'lab1': 0, 'lab2': 0, 'lab3': 0}

path_to_db = '/home/peter/PycharmProjects/TimesOfTimeTable/demoapp/database/TimesOfTimeTable.db'
conn = sqlite3.connect(path_to_db)
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
        class_engaged[row[1]] = 0

    cur.execute("SELECT sub_short_name, FAC_SHORT_NAME from view2 WHERE sec = 'B'")
    for row in cur.fetchall():
        b_fac[row[0]] = row[1]
        fac[row[0]] = row[1]
        class_engaged[row[1]] = 0

    cur.execute("SELECT sub_short_name, FAC_SHORT_NAME from view2 WHERE sec = 'C'")
    for row in cur.fetchall():
        c_fac[row[0]] = row[1]
        fac[row[0]] = row[1]
        class_engaged[row[1]] = 0

    cur.execute('select distinct  fac_short_name from faculty')
    facs = cur.fetchall()
    for fname in facs:
        fac_list.append(fname[0])


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
    print(class_engaged, 'before')
    for f in fac_list:
        if class_engaged[f] < 1:
            pass
        else:
            class_engaged[f] -= 1
    print(class_engaged, 'after')




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




class positions_of_class():
    def __init__(self):
        self.pos_b = None
        self.pos_a = None
        self.pos_c = None

    """"""


class spl:
    def __init__(self):
        self.is_spl_done_for_week = False


spl_sub = spl()
sem5 = positions_of_class()

""" dictionary of list  """



def get_one_sub(position, include_others=True, only_others=False, return_type=False):
    update_subs(position, include_others=include_others, only_others=only_others)
    for sub2, type2 in subs:
        if class_engaged[fac[sub2]]:
            continue
        if return_type:
            return sub2, type2
        return sub2


def get_all_subs(position, include_others=True, only_others=False):
    """ no need to return, because update is make 'subs' list. its accessible """
    update_subs(position, include_others=include_others, only_others=only_others)
    return


def Spl(sub1, position, day):
    """ return value zero represents any sub is not appended to any class"""
    """ return vale 1, spl subject is appended to all the class """
    if spl_sub.is_spl_done_for_week:
        return 0
    highest = max(sem5.pos_a, sem5.pos_b, sem5.pos_c)
    if highest in [0, 2, 4]:
        for loop in range(highest - sem5.pos_a):
            if sem5.pos_a < highest:
                sub2, type2 = get_one_sub(position, only_others=True, return_type=True)
                if not a_hours[sub1] > hours.hour_greaterthan(type2, day):
                    continue
                a.append(sub2)
                print("class appended is", sub1)
                class_engaged[a_fac[sub2]] += 1
                a_hours[sub2] -= 1
                sem5.pos_a += 1
        for loop in range(highest - sem5.pos_b):
            if sem5.pos_b < highest:
                sub2, type2 = get_one_sub(position, only_others=True, return_type=True)
                if not b_hours[sub1] > hours.hour_greaterthan(type2, day):
                    continue
                b.append(sub2)
                print("class appended is", sub1)
                class_engaged[b_fac[sub2]] += 1
                b_hours[sub2] -= 1
                sem5.pos_b += 1
        for loop in range(highest - sem5.pos_c):
            if sem5.pos_c < highest:
                sub2, type2 = get_one_sub(position, only_others=True, return_type=True)
                if not c_hours[sub1] > hours.hour_greaterthan(type2, day):
                    continue
                c.append(sub2)
                print("class appended is", sub1)
                class_engaged[c_fac[sub2]] += 1
                c_hours[sub2] -= 1
                sem5.pos_c += 1

        for i in range(2):
            a.append(sub1)
            b.append(sub1)
            c.append(sub1)
            class_engaged[b_fac[sub1]] += 1
            class_engaged[a_fac[sub1]] += 1
            class_engaged[c_fac[sub1]] += 1
            sem5.pos_a += 1
            sem5.pos_b += 1
            sem5.pos_c += 1
            a_hours[sub1] -= 1
            b_hours[sub1] -= 1
            c_hours[sub1] -= 1
            spl_sub.is_spl_done_for_week = True
        return 0
    return -1

labs_done = dict()
labs_done = {'a': [], 'b': [], 'c': []}
def xyz(position, sub1, type1, sec, _class_var, day):
    diff = 0
    for lb in labs_done.get(_class_var):
        if sub1 in lb:
            return position, diff
        else:
            pass
    print('successfuly passed labs_done?')
    if type1 in ['lab1', 'lab2', 'lab3']:
        print('yess it is a lab !!')
        print('checking for more than 2 same lab engaging...')
        print(list_engaging_labs[type1])
        print(list_engaging_labs)
        if list_engaging_labs[type1] < 2:
            print('no 2 same lab is engaging')
            print('checking for end position...')
            if position + 3 <= 7:
                print('end position is oky')
                for diff in range(3):
                    sec.append(sub1)
                    if _class_var == 'a':
                        a_hours[sub1] -= 1
                        class_engaged[a_fac[sub1]] += 1
                    elif _class_var == 'b':
                        b_hours[sub1] -= 1
                        class_engaged[b_fac[sub1]] += 1
                    elif _class_var == 'c':
                        c_hours[sub1] -= 1
                        class_engaged[c_fac[sub1]] += 1

                    print("class appended is", sub1)
                    position += 1
                if _class_var == 'a':
                    labs_done['a'].append(sub1)
                if _class_var == 'b':
                    labs_done['b'].append(sub1)
                if _class_var == 'c':
                    labs_done['c'].append(sub1)
                list_engaging_labs[type1] += 1
                """ adding faculty who are engaging class to decrement list"""
                add_fac_to_decrement_it(_class_var, sub1, loop=3)
                return position, diff + 1
        else:
            print('entering to else loop in labs')
            get_all_subs(position, include_others=False)
            for sub1, type1 in subs:
                if type1 not in ['spl'] and list_engaging_labs[type1] < 2:
                    for lb in labs_done.get(_class_var):
                        if sub1 in lb:
                            continue
                        else:
                            print('checking for end position...')
                            if position + 3 <= 7:
                                print('end position is oky')
                                list_engaging_labs[type1] += 1
                                add_fac_to_decrement_it(_class_var, sub1, loop=3)
                                for diff in range(3):
                                    sec.append(sub1)
                                    if _class_var == 'a':
                                        a_hours[sub1] -= 1
                                        class_engaged[a_fac[sub1]] += 1
                                    elif _class_var == 'b':
                                        b_hours[sub1] -= 1
                                        class_engaged[b_fac[sub1]] += 1
                                    elif _class_var == 'c':
                                        c_hours[sub1] -= 1
                                        class_engaged[c_fac[sub1]] += 1
                                    print("class appended is", sub1)
                                    position += 1
                                if _class_var == 'a':
                                    labs_done['a'].append(sub1)
                                if _class_var == 'b':
                                    labs_done['b'].append(sub1)
                                if _class_var == 'c':
                                    labs_done['c'].append(sub1)
                                print(labs_done, 'changed lab')
                    return position, diff + 1
            print('lab rejected')
            return position, diff + 1


def normal_classes(position, sub1, type1, sec, _class_var, day):
    print("its a noraml class !!")
    if _class_var == 'a':
        if a_hours[sub1] > hours.hour_greaterthan(type1, day):
            sec.append(sub1)
            a_hours[sub1] -= 1
            class_engaged[a_fac[sub1]] += 1
            print("class appended is", sub1)
            position += 1
            add_fac_to_decrement_it(_class_var, sub1)
            return position, 1
        print(sub1, 'not inserted')
        get_all_subs(position, only_others=True)
        for sub1, type1 in subs:
            if not a_hours[sub1] > hours.hour_greaterthan(type1, day):
                continue
            sec.append(sub1)
            a_hours[sub1] -= 1
            class_engaged[a_fac[sub1]] += 1
            print("class appended is", sub1)
            position += 1
            add_fac_to_decrement_it(_class_var, sub1)
            return position, 1
        print('subject rejected:', sub1)
        return position, 1
    if _class_var == 'b':
        if b_hours[sub1] > hours.hour_greaterthan(type1, day):
            sec.append(sub1)
            b_hours[sub1] -= 1
            class_engaged[b_fac[sub1]] += 1
            print("class appended is", sub1)
            position += 1
            add_fac_to_decrement_it(_class_var, sub1)
            return position, 1
        print(sub1, 'not inserted')
        get_all_subs(position, only_others=True)
        for sub1, type1 in subs:
            if not b_hours[sub1] > hours.hour_greaterthan(type1, day):
                continue
            sec.append(sub1)
            b_hours[sub1] -= 1
            class_engaged[b_fac[sub1]] += 1
            print("class appended is", sub1)
            position += 1
            add_fac_to_decrement_it(_class_var, sub1)
            return position, 1
        print('subject rejected:', sub1)
        return position, 1
    if _class_var == 'c':
        if c_hours[sub1] > hours.hour_greaterthan(type1, day):
            sec.append(sub1)
            c_hours[sub1] -= 1
            class_engaged[c_fac[sub1]] += 1
            print("class appended is", sub1)
            position += 1
            add_fac_to_decrement_it(_class_var, sub1)
            return position, 1
        print(sub1, 'not inserted')
        get_all_subs(position, only_others=True)
        for sub1, type1 in subs:
            if not c_hours[sub1] > hours.hour_greaterthan(type1, day):
                continue
            sec.append(sub1)
            c_hours[sub1] -= 1
            class_engaged[c_fac[sub1]] += 1
            print("class appended is", sub1)
            position += 1
            add_fac_to_decrement_it(_class_var, sub1)
            return position, 1
        print('subject rejected:', sub1)
        return position, 1

from lib import hours_per_sub as hours

print(list_engaging_labs)


class time_table:
    type1 = None
    sub1 = None
    for day in range(6):
        class_engaged = dict.fromkeys(class_engaged, 0)
        print(list_engaging_labs)
        list_engaging_labs = dict.fromkeys(list_engaging_labs, 0)
        print(list_engaging_labs)
        i = 0
        sem5.pos_a = 0
        sem5.pos_b = 0
        sem5.pos_c = 0
        a.clear()
        b.clear()
        c.clear()

        for hour in range(12):
            decrement_hours()
            print('next hour')
            if isinstance(sem5.pos_a, int) and sem5.pos_a < 7:
                if day >= 3:
                    sub_dict = {key: val for key, val in sorted(a_hours.items(), key=lambda ele: ele[1], reverse=True)}
                    print(sub_dict,'for a')
                    for sub, hour_rem in sub_dict.items():
                        sub1 = sub
                        hour_left = hour_rem
                        cur.execute('select sub_type from subjects where sub_short_name = ?', (sub,))
                        type1 = cur.fetchone()[0]
                        print('subjects selected for a from sorted dictionary is ', sub1)
                        print()
                        """ not more than two subjects per day """
                        if not a_hours[sub1] > hours.hour_greaterthan(type1, day):
                            print('continued 2 hours is done for the day')
                            continue
                        print("pass")
                        if class_engaged[a_fac[sub1]]:
                            print('continued, faculty is engaging')
                            continue
                        print("pass")
                        if type1 in ['spl']:
                            if spl_sub.is_spl_done_for_week:
                                continue
                            return_val = Spl(sub1, sem5.pos_a, day)
                            is_spl_done_for_week = True
                            break
                        if type1 in ['lab1', 'lab2', 'lab3']:
                            if a_hours[sub1]:
                                print("yess entered to xyz")
                                sem5.pos_a, diff = xyz(sem5.pos_a, sub1, type1, a, 'a', day)
                            break
                        else:
                            if a_hours[sub1]:
                                print("yess entered to nomal class")
                                sem5.pos_a, diff = normal_classes(sem5.pos_a, sub1, type1, a, 'a', day)
                            break
                else:
                    update_subs(sem5.pos_a)
                    shuffle(subs)
                    for sub in subs:
                        sub1 = sub[0]
                        type1 = sub[1]
                        print('subjects selected for a is ', sub1)
                        if not a_hours[sub1] > hours.hour_greaterthan(type1, day):
                            print('continued 2 hours is done for the day')
                            continue
                        if class_engaged[a_fac[sub1]]:
                            print('continued, faculty is engaging')
                            print(class_engaged)
                            continue
                        if type1 in ['spl']:
                            print('spl')
                            if spl_sub.is_spl_done_for_week:
                                continue
                            return_val = Spl(sub1, sem5.pos_a, day)
                            is_spl_done_for_week = True
                            break
                        if type1 in ['lab1', 'lab2', 'lab3']:
                            if a_hours[sub1]:
                                print("yess entered to xyz")
                                sem5.pos_a, diff = xyz(sem5.pos_a, sub1, type1, a, 'a', day)
                            break
                        else:
                            if a_hours[sub1]:
                                print("yess entered to nomal class")
                                sem5.pos_a, diff = normal_classes(sem5.pos_a, sub1, type1, a, 'a', day)
                            break

            if isinstance(sem5.pos_b, int) and sem5.pos_b < 7:
                if day >= 3:
                    sub_dict = {key: val for key, val in sorted(b_hours.items(), key=lambda ele: ele[1], reverse=True)}
                    print(sub_dict, 'for b')
                    for sub, hour_left in sub_dict.items():
                        sub1 = sub
                        hour_left = hour_rem
                        cur.execute('select sub_type from subjects where sub_short_name = ?', (sub,))
                        type1 = cur.fetchone()[0]
                        if sub1 == 'dbms':
                            print(type1, 'dbms type')
                        print('subjects selected for b from sorted dictionary is', sub1)
                        print()
                        if not b_hours[sub1] > hours.hour_greaterthan(type1, day):
                            print('continued 2 hours is done for the day')
                            continue
                        print("pass")
                        if class_engaged[b_fac[sub1]]:
                            print('continued, faculty is engaging')
                            print(class_engaged)
                            continue
                        print("pass")
                        if type1 in ['spl']:
                            if spl_sub.is_spl_done_for_week:
                                continue
                            return_val = Spl(sub1, sem5.pos_b, day)
                            break
                        if type1 in ['lab1', 'lab2', 'lab3']:
                            if b_hours[sub1]:
                                print("yess entered to xyz")
                                sem5.pos_b, diff = xyz(sem5.pos_b, sub1, type1, b, 'b', day)
                            break
                        else:
                            if b_hours[sub1]:
                                print("yess entered to xyz")
                                sem5.pos_b, diff = normal_classes(sem5.pos_b, sub1, type1, b, 'b', day)
                            break
                else:
                    update_subs(sem5.pos_b)
                    shuffle(subs)
                    for sub in subs:
                        sub1 = sub[0]
                        type1 = sub[1]
                        print('subjects selected for b is ', sub1)
                        if not b_hours[sub1] > hours.hour_greaterthan(type1, day):
                            print("continued 2 hours is done for the day")
                            continue
                        if class_engaged[b_fac[sub1]]:
                            print('continued, faculty is engaging')
                            print(class_engaged)
                            continue
                        if type1 in ['spl']:
                            if spl_sub.is_spl_done_for_week:
                                continue
                            return_val = Spl(sub1, sem5.pos_b, day)
                            break
                        if type1 in ['lab1', 'lab2', 'lab3']:
                            if b_hours[sub1]:
                                print("yess entered to xyz")
                                sem5.pos_b, diff = xyz(sem5.pos_b, sub1, type1, b, 'b', day)
                            break
                        else:
                            if b_hours[sub1]:
                                print("yess entered to nomal_class")
                                sem5.pos_b, diff = normal_classes(sem5.pos_b, sub1, type1, b, 'b', day)
                            break

            if isinstance(sem5.pos_c, int) and sem5.pos_c < 7:
                if day >= 3:
                    sub_dict = {key: val for key, val in sorted(c_hours.items(), key=lambda ele: ele[1], reverse=True)}
                    print(sub_dict, 'for c')
                    for sub, hour_left in sub_dict.items():
                        sub1 = sub
                        hour_left = sub
                        cur.execute('select sub_type from subjects where sub_short_name = ?', (sub,))
                        type1 = cur.fetchone()[0]
                        print('subjects selected for c from sorted dictionary is ', sub1)
                        print()
                        if not c_hours[sub1] > hours.hour_greaterthan(type1, day):
                            print('continued 2 hours is done for the day')
                            continue
                        print("pass")
                        if class_engaged[c_fac[sub1]]:
                            print('continued, faculty is engaging')
                            continue
                        print("pass")
                        if type1 in ['spl']:
                            if spl_sub.is_spl_done_for_week:
                                continue
                            return_val = Spl(sub1, sem5.pos_c, day)
                            is_spl_done_for_week = True
                            break
                        if type1 in ['lab1', 'lab2', 'lab3']:
                            if c_hours[sub1]:
                                sem5.pos_c, diff = xyz(sem5.pos_c, sub1, type1, c, 'c', day)
                            break
                        else:
                            if c_hours[sub1]:
                                sem5.pos_c, diff = normal_classes(sem5.pos_c, sub1, type1, c, 'c', day)
                            break
                else:
                    update_subs(sem5.pos_c)
                    shuffle(subs)
                    for sub in subs:
                        sub1 = sub[0]
                        type1 = sub[1]
                        print('subjects selected for c is ', sub1)
                        if not c_hours[sub1] > hours.hour_greaterthan(type1, day):
                            print('continued, 2 is done for the day')
                            continue
                        if class_engaged[c_fac[sub1]]:
                            print('continue, faculty enageging class')
                            print(class_engaged)
                            continue
                        if type1 in ['spl']:
                            if spl_sub.is_spl_done_for_week:
                                continue
                            return_val = Spl(sub1, sem5.pos_c, day)
                            is_spl_done_for_week = True
                            break
                        if type1 in ['lab1', 'lab2', 'lab3']:
                            if c_hours[sub1]:
                                sem5.pos_c, diff = xyz(sem5.pos_c, sub1, type1, c, 'c', day)
                            break
                        else:
                            if c_hours[sub1]:
                                sem5.pos_c, diff = normal_classes(sem5.pos_c, sub1, type1, c, 'c', day)
                            break
#             decrement_it.clear()
#             print()
#             print(class_engaged)
#             print(a)
#             print(sem5.pos_a)
#             print(a_hours)
#             print()
#             print(b)
#             print(sem5.pos_b)
#             print(b_hours)
#             print()
#             print(c)
#             print(sem5.pos_c)
#             print(c_hours)
#             print()
#
# print(a_hours)
# print(b_hours)
# print(c_hours)
# print(subs)
