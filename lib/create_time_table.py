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


def get_subs():
    """ refers table 'subjects' """
    cur.execute("""SELECT sub_short_name, sub_type FROM subjects WHERE SEM = 5;""")
    for sname, stype in cur.fetchall():
        d = {sname: stype}
        subs.append(d)


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
init_sub_hours()
print(subs)
a = list()
b = list()
c = list()
flaga = True
flagb = True
flagc = True
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

        for sub_d in subs:  # subs is a list of dictionaries
            i += 1
            for sub, type in sub_d.items():
                """ for sec a """
                if len(a) < 7:
                    if flaga or flagb and type in ['lab'] and a_hours[sub] > 0:
                        if i not in [0, 1, 4]:
                            continue
                        a.append(sub)
                        a.append(sub)
                        a.append(sub)
                        a_hours[sub] -= 3
                        class_engaged[a_fac[sub]] = 3
                        decrement_it.append(a_fac[sub])
                        flaga = False
                    elif type in ['spl'] and a_hours[sub] > 0:
                        if i in [0, 2, 4, 6] and len(a) == len(b) and len(b) == len(c):
                            continue
                        a.append(sub)
                        a.append(sub)
                        b.append(sub)
                        b.append(sub)
                        c.append(sub)
                        c.append(sub)
                        a_hours[sub] -= 2
                        b_hours[sub] -= 2
                        c_hours[sub] -= 2
                    else:
                        a.append(sub)
                        a_hours[sub] -= 1
                        class_engaged[a_fac[sub]] = 1
                        decrement_it.append(a_fac[sub])

                print()
                print("sec A say Monday: ", a)
                if len(b) < 7:
                    """ for sec b """
                    if type in ['lab'] and b_hours[sub] > 0 and not class_engaged[b_fac[sub]]:
                        if i not in [0, 1, 4]:
                            continue
                        b.append(sub)
                        b.append(sub)
                        b.append(sub)
                        print("lab appended 3 times",b)
                        b_hours[sub] -= 3
                        class_engaged[a_fac[sub]] = 3
                        decrement_it.append(b_fac[sub])
                    elif b_hours[sub] > 0 and not class_engaged[b_fac[sub]]:  # if faculty is not engaging any other
                        # class
                        print("b else if ")
                        b.append(sub)
                        b_hours[sub] -= 1
                        class_engaged[a_fac[sub]] = 1
                        decrement_it.append(b_fac[sub])
                    else:  # if faculty is engaging any other class
                        """ check for next subject & check if the sub faculty is free ?  """
                        print("b else")
                        k = i
                        for j in range(len(subs) - i):
                            for sub_d1 in subs:
                                if not k < 0:
                                    k -= 1
                                    continue
                                else:
                                    for sub1, type1 in sub_d1.items():
                                        if not class_engaged[b_fac[sub1]]:
                                            print(sub1)
                                            b.append(sub1)
                                            print("sec B say Monday: ", b)
                                            b_hours[sub1] -= 1
                                            class_engaged[b_fac[sub1]] = 1
                                            decrement_it.append(b_fac[sub1])
                                            break
                                    break
                            break

                print("sec B say Monday: ", b)
                if len(c) < 7:
                    """ for sec c """
                    if flaga and type in ['lab'] and c_hours[sub] > 0 and not class_engaged[c_fac[sub]]:  #
                        # for lab
                        if i not in [0, 1, 4]:
                            continue
                        c.append(sub)
                        c.append(sub)
                        c.append(sub)
                        c_hours[sub] -= 3
                        class_engaged[c_fac[sub]] = 3
                        decrement_it.append(c_fac[sub])
                    elif c_hours[sub] > 0 and not class_engaged[c_fac[sub]]:  # if faculty is not engaging any other
                        # class
                        c.append(sub)
                        c_hours[sub] -= 1
                        class_engaged[c_fac[sub]] = 1
                        decrement_it.append(c_fac[sub])
                    else:  # if faculty is engaging any other class
                        """ check sub fac is free? """
                        k = i
                        for j in range(len(subs) - i):
                            for sub_d1 in subs:
                                if not k < 0:
                                    k -= 1
                                    continue
                                else:
                                    for sub1, type1 in sub_d1.items():
                                        if not class_engaged[c_fac[sub1]]:
                                            c.append(sub1)
                                            c_hours[sub1] -= 1
                                            class_engaged[c_fac[sub1]] = 1
                                            decrement_it.append(c_fac[sub1])
                                            break
                                    break
                            break
                print()
                print("sec C say Monday: ", c)
            decrement_hours()
            """ subjects taken per day is not more than 7 """
            if i == 7:
                print("exiting")
                break
        flaga = True
        flagb = True
