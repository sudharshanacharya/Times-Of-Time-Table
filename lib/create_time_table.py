import sqlite3
from random import shuffle
from lib.queries import queries
from lib import hours_per_sub as hours
path_to_db = '/home/peter/PycharmProjects/TimesOfTimeTable/demoapp/database/TimesOfTimeTable.db'

class variables:
    def __init__(self):
        self.is_spl_done_for_week = False
        self.list_engaging_labs = {'lab1': 0, 'lab2': 0, 'lab3': 0}
        """ x_fac[sub] = sub faculty for class x """
        self.a_fac = dict()
        self.b_fac = dict()
        self.c_fac = dict()
        self.fac = dict()
        self.fac_list = list()
        self.class_engaged = dict()
        """ x_hours[sub] = remaining hours of sub """
        self.a_hours = dict()
        self.b_hours = dict()
        self.c_hours = dict()
        """ this sub-list keeps on changing based on update_subs(), get_all_subs(), get_one_sub() """
        self.subs = list()

        """ list of lab engaged """
        self.lab_not_engaged = list()
        self.lab_not_engaged.append('lab1')
        self.lab_not_engaged.append('lab2')
        self.lab_not_engaged.append('lab3')
        """ not usual class hours"""
        self.if_lab = list()
        self.if_lab.append('lab1')
        self.if_lab.append('lab2')
        self.if_lab.append('lab3')
        self.if_lab = list()
        self.if_lab.append('spl')
        """ list of faculty, who are engaging classes now & who's 'class_engaged' will be decremented """
        self.decrement_it = list()

        self.pos_b = None
        self.pos_a = None
        self.pos_c = None

        self.a = list()
        self.b = list()
        self.c = list()

        self.labs_done = dict()
        self.labs_done = {'a': [], 'b': [], 'c': []}

        self.x = list()
        self.y = list()
        self.z = list()


class create_time_table:
    """ picks subject from subs list if the sub not present sub_fac table then creates error """
    """ now you can remove decrement it fuction """
    def __init__(self):
        self.var = variables()
        
    def create_custom(self):
        with sqlite3.connect(path_to_db) as conn:
            cur = conn.cursor()
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


    def init_fac(self):
        """ refers view2, lib/queries.py """
        """ x_fac[sub] = sub faculty for class x """
        """ initializes class_engaged[fac] to 0 """
        with sqlite3.connect(path_to_db) as conn:
            cur = conn.cursor()
            cur.execute(queries.view2)
            cur.execute("SELECT sub_short_name, FAC_SHORT_NAME from view2 WHERE sec = 'A'")
            for row in cur.fetchall():
                self.var.a_fac[row[0]] = row[1]
                self.var.fac[row[0]] = row[1]
                self.var.class_engaged[row[1]] = 0

            cur.execute("SELECT sub_short_name, FAC_SHORT_NAME from view2 WHERE sec = 'B'")
            for row in cur.fetchall():
                self.var.b_fac[row[0]] = row[1]
                self.var.fac[row[0]] = row[1]
                self.var.class_engaged[row[1]] = 0

            cur.execute("SELECT sub_short_name, FAC_SHORT_NAME from view2 WHERE sec = 'C'")
            for row in cur.fetchall():
                self.var.c_fac[row[0]] = row[1]
                self.var.fac[row[0]] = row[1]
                self.var.class_engaged[row[1]] = 0

            cur.execute('select distinct  fac_short_name from faculty')
            facs = cur.fetchall()
            for fname in facs:
                self.var.fac_list.append(fname[0])


    def init_sub_hours(self):
        """ refers view2, lib/queries.py """
        """ x_hours[sub] = remaining hours of sub """
        with sqlite3.connect(path_to_db) as conn:
            cur = conn.cursor()
            cur.execute(queries.view2)
            cur.execute("SELECT SUB_SHORT_NAME, rem_hours from view2 WHERE sec = 'A'")
            for row in cur.fetchall():
                self.var.a_hours[row[0]] = row[1]
            cur.execute("SELECT SUB_SHORT_NAME, rem_hours from view2 WHERE sec = 'B'")
            for row in cur.fetchall():
                self.var.b_hours[row[0]] = row[1]
            cur.execute("SELECT SUB_SHORT_NAME, rem_hours from view2 WHERE sec = 'C'")
            for row in cur.fetchall():
                self.var.c_hours[row[0]] = row[1]


    def update_subs(self, position, include_others=True, only_others=False):
        """ gets the data from the custom table returns shuffled list subs"""
        """ by default returns subs applicable for position """
        """ if 'include_others=False' :returns subs only applicable for perticular position """
        """ if 'only_others=True' :returns subs expect the only applicable one  """
        with sqlite3.connect(path_to_db) as conn:
            cur = conn.cursor()
            if only_others:
                cur.execute('select sname, stype from custom where timing = ?', (-1,))
            elif include_others:
                cur.execute('select sname, stype from custom where timing = ? or timing = ?', (position, -1,))
            else:
                cur.execute('select sname, stype from custom where timing = ?', (position,))
            self.var.subs.clear()
            for sub2, type2 in cur.fetchall():
                d = (sub2, type2)
                self.var.subs.append(d)
            return


    def decrement_hours(self,):
        """ function that will decrement faculty engaging hours """
        for f in self.var.fac_list:
            if self.var.class_engaged[f] < 1:
                pass
            else:
                self.var.class_engaged[f] -= 1


    def get_one_sub(self,position, include_others=True, only_others=False, return_type=False):
        self.update_subs(position, include_others=include_others, only_others=only_others)
        for sub2, type2 in self.var.subs:
            if self.var.class_engaged[self.var.fac[sub2]]:
                continue
            if return_type:
                return sub2, type2
            return sub2


    def get_all_subs(self, position, include_others=True, only_others=False):
        """ no need to return, because update is make 'subs' list. its accessible """
        self.update_subs(position, include_others=include_others, only_others=only_others)
        return


    def Spl(self, sub1, position, day):
        """ return value zero represents any sub is not appended to any class"""
        """ return vale 1, spl subject is appended to all the class """
        if self.var.is_spl_done_for_week:
            return 0
        highest = max(self.var.pos_a, self.var.pos_b, self.var.pos_c)
        if highest in [0, 2, 4]:
            for loop in range(highest - self.var.pos_a):
                if self.var.pos_a < highest:
                    sub2, type2 = self.get_one_sub(position, only_others=True, return_type=True)
                    if not self.var.a_hours[sub1] > hours.hour_greaterthan(type2, day):
                        continue
                    self.var.a.append(sub2)
                    self.var.class_engaged[self.var.a_fac[sub2]] += 1
                    self.var.a_hours[sub2] -= 1
                    self.var.pos_a += 1
            for loop in range(highest - self.var.pos_b):
                if self.var.pos_b < highest:
                    sub2, type2 = self.get_one_sub(position, only_others=True, return_type=True)
                    if not self.var.b_hours[sub1] > hours.hour_greaterthan(type2, day):
                        continue
                    self.var.b.append(sub2)
                    self.var.class_engaged[self.var.b_fac[sub2]] += 1
                    self.var.b_hours[sub2] -= 1
                    self.var.pos_b += 1
            for loop in range(highest - self.var.pos_c):
                if self.var.pos_c < highest:
                    sub2, type2 = self.get_one_sub(position, only_others=True, return_type=True)
                    if not self.var.c_hours[sub1] > hours.hour_greaterthan(type2, day):
                        continue
                    self.var.c.append(sub2)
                    self.var.class_engaged[self.var.c_fac[sub2]] += 1
                    self.var.c_hours[sub2] -= 1
                    self.var.pos_c += 1

            for i in range(2):
                self.var.a.append(sub1)
                self.var.b.append(sub1)
                self.var.b.append(sub1)
                self.var.c.append(sub1)
                self.var.class_engaged[self.var.b_fac[sub1]] += 1
                self.var.class_engaged[self.var.a_fac[sub1]] += 1
                self.var.class_engaged[self.var.c_fac[sub1]] += 1
                self.var.pos_a += 1
                self.var.pos_b += 1
                self.var.pos_c += 1
                self.var.a_hours[sub1] -= 1
                self.var.b_hours[sub1] -= 1
                self.var.c_hours[sub1] -= 1
                self.var.is_spl_done_for_week = True
            return 0
        return -1


    def xyz(self, position, sub1, type1, sec, _class_var, day):
        for lb in self.var.labs_done.get(_class_var):
            if sub1 in lb:
                return position
            else:
                pass
        if type1 in ['lab1', 'lab2', 'lab3']:
            if self.var.list_engaging_labs[type1] < 2:
                if position + 3 <= 7:
                    for diff in range(3):
                        sec.append(sub1)
                        if _class_var == 'a':
                            self.var.a_hours[sub1] -= 1
                            self.var.class_engaged[self.var.a_fac[sub1]] += 1
                        elif _class_var == 'b':
                            self.var.b_hours[sub1] -= 1
                            self.var.class_engaged[self.var.b_fac[sub1]] += 1
                        elif _class_var == 'c':
                            self.var.c_hours[sub1] -= 1
                            self.var.class_engaged[self.var.c_fac[sub1]] += 1
                        position += 1
                    if _class_var == 'a':
                        self.var.labs_done['a'].append(sub1)
                    if _class_var == 'b':
                        self.var.labs_done['b'].append(sub1)
                    if _class_var == 'c':
                        self.var.labs_done['c'].append(sub1)
                    self.var.list_engaging_labs[type1] += 1
                    """ adding faculty who are engaging class to decrement list"""
                    # add_fac_to_decrement_it(_class_var, sub1, loop=3)
                    return position
            else:
                self.get_all_subs(position, include_others=False)
                for sub1, type1 in self.var.subs:
                    if type1 not in ['spl'] and self.var.list_engaging_labs[type1] < 2:
                        for lb in self.var.labs_done.get(_class_var):
                            if sub1 in lb:
                                continue
                            else:
                                if position + 3 <= 7:
                                    self.var.list_engaging_labs[type1] += 1
                                    # add_fac_to_decrement_it(_class_var, sub1, loop=3)
                                    for diff in range(3):
                                        sec.append(sub1)
                                        if _class_var == 'a':
                                            self.var.a_hours[sub1] -= 1
                                            self.var.class_engaged[self.var.a_fac[sub1]] += 1
                                        elif _class_var == 'b':
                                            self.var.b_hours[sub1] -= 1
                                            self.var.class_engaged[self.var.b_fac[sub1]] += 1
                                        elif _class_var == 'c':
                                            self.var.c_hours[sub1] -= 1
                                            self.var.class_engaged[self.var.c_fac[sub1]] += 1
                                        position += 1
                                    if _class_var == 'a':
                                        self.var.labs_done['a'].append(sub1)
                                    if _class_var == 'b':
                                        self.var.labs_done['b'].append(sub1)
                                    if _class_var == 'c':
                                        self.var.labs_done['c'].append(sub1)
                        return position
                return position


    def normal_classes(self,position, sub1, type1, sec, _class_var, day):
        if _class_var == 'a':
            if self.var.a_hours[sub1] > hours.hour_greaterthan(type1, day):
                sec.append(sub1)
                self.var.a_hours[sub1] -= 1
                self.var.class_engaged[self.var.a_fac[sub1]] += 1
                position += 1
                # add_fac_to_decrement_it(_class_var, sub1)
                return position
            self.get_all_subs(position, only_others=True)
            for sub1, type1 in subs:
                if not self.var.a_hours[sub1] > hours.hour_greaterthan(type1, day):
                    continue
                sec.append(sub1)
                self.var.a_hours[sub1] -= 1
                self.var.class_engaged[self.var.a_fac[sub1]] += 1
                position += 1
                # add_fac_to_decrement_it(_class_var, sub1)
                return position
            return position
        if _class_var == 'b':
            if self.var.b_hours[sub1] > hours.hour_greaterthan(type1, day):
                sec.append(sub1)
                self.var.b_hours[sub1] -= 1
                self.var.class_engaged[self.var.b_fac[sub1]] += 1
                position += 1
                # add_fac_to_decrement_it(_class_var, sub1)
                return position
            self.get_all_subs(position, only_others=True)
            for sub1, type1 in subs:
                if not self.var.b_hours[sub1] > hours.hour_greaterthan(type1, day):
                    continue
                sec.append(sub1)
                self.var.b_hours[sub1] -= 1
                self.var.class_engaged[self.var.b_fac[sub1]] += 1
                position += 1
                # add_fac_to_decrement_it(_class_var, sub1)
                return position
            return position
        if _class_var == 'c':
            if self.var.c_hours[sub1] > hours.hour_greaterthan(type1, day):
                sec.append(sub1)
                self.var.c_hours[sub1] -= 1
                self.var.class_engaged[self.var.c_fac[sub1]] += 1
                position += 1
                # add_fac_to_decrement_it(_class_var, sub1)
                return position
            self.get_all_subs(position, only_others=True)
            for sub1, type1 in subs:
                if not c_hours[sub1] > hours.hour_greaterthan(type1, day):
                    continue
                sec.append(sub1)
                self.var.c_hours[sub1] -= 1
                self.var.class_engaged[self.var.c_fac[sub1]] += 1
                position += 1
                # add_fac_to_decrement_it(_class_var, sub1)
                return position
            return position



    def final_call(self):
        self.create_custom()
        self.init_fac()
        self.init_sub_hours()

        type1 = None
        sub1 = None
        for day in range(6):
            self.var.class_engaged = dict.fromkeys(self.var.class_engaged, 0)
            self.var.list_engaging_labs = dict.fromkeys(self.var.list_engaging_labs, 0)
            i = 0
            self.var.pos_a = 0
            self.var.pos_b = 0
            self.var.pos_c = 0
            self.var.a.clear()
            self.var.b.clear()
            self.var.c.clear()

            for hour in range(12):
                self.decrement_hours()
                if isinstance(self.var.pos_a, int) and self.var.pos_a < 7:
                    if day >= 3:
                        sub_dict = {key: val for key, val in sorted(self.var.a_hours.items(), key=lambda ele: ele[1], reverse=True)}
                        for sub, hour_rem in sub_dict.items():
                            sub1 = sub
                            hour_left = hour_rem
                            with sqlite3.connect(path_to_db) as conn:
                                cur = conn.cursor()
                                cur.execute('select sub_type from subjects where sub_short_name = ?', (sub,))
                                type1 = cur.fetchone()[0]
                            """ not more than two subjects per day """
                            if not self.var.a_hours[sub1] > hours.hour_greaterthan(type1, day):
                                continue
                            if self.var.class_engaged[self.var.a_fac[sub1]]:
                                continue
                            if type1 in ['spl']:
                                if self.var.is_spl_done_for_week:
                                    continue
                                return_val = self.Spl(sub1, self.var.pos_a, day)
                                self.var.is_spl_done_for_week = True
                                break
                            if type1 in ['lab1', 'lab2', 'lab3']:
                                if self.var.a_hours[sub1]:
                                    self.var.pos_a = self.xyz(self.var.pos_a, sub1, type1, self.var.a, 'a', day)
                                break
                            else:
                                if self.var.a_hours[sub1]:
                                    self.var.pos_a = self.normal_classes(self.var.pos_a, sub1, type1, self.var.a, 'a', day)
                                break
                    else:
                        self.update_subs(self.var.pos_a)
                        shuffle(self.var.subs)
                        for sub in self.var.subs:
                            sub1 = sub[0]
                            type1 = sub[1]
                            if not self.var.a_hours[sub1] > hours.hour_greaterthan(type1, day):
                                continue
                            if self.var.class_engaged[self.var.a_fac[sub1]]:
                                continue
                            if type1 in ['spl']:
                                if self.var.is_spl_done_for_week:
                                    continue
                                return_val = self.Spl(sub1, self.var.pos_a, day)
                                self.var.is_spl_done_for_week = True
                                break
                            if type1 in ['lab1', 'lab2', 'lab3']:
                                if self.var.a_hours[sub1]:
                                    self.var.pos_a = self.xyz(self.var.pos_a, sub1, type1, self.var.a, 'a', day)
                                break
                            else:
                                if self.var.a_hours[sub1]:
                                    self.var.pos_a = self.normal_classes(self.var.pos_a, sub1, type1, self.var.a, 'a', day)
                                break

                if isinstance(self.var.pos_b, int) and self.var.pos_b < 7:
                    if day >= 3:
                        sub_dict = {key: val for key, val in sorted(self.var.b_hours.items(), key=lambda ele: ele[1], reverse=True)}
                        for sub, hour_left in sub_dict.items():
                            sub1 = sub
                            hour_left = hour_rem
                            with sqlite3.connect(path_to_db):
                                cur = conn.cursor()
                                cur.execute('select sub_type from subjects where sub_short_name = ?', (sub,))
                                type1 = cur.fetchone()[0]
                            if not self.var.b_hours[sub1] > hours.hour_greaterthan(type1, day):
                                continue
                            if self.var.class_engaged[self.var.b_fac[sub1]]:
                                continue
                            if type1 in ['spl']:
                                if self.var.is_spl_done_for_week:
                                    continue
                                return_val = self.Spl(sub1, self.var.pos_b, day)
                                break
                            if type1 in ['lab1', 'lab2', 'lab3']:
                                if self.var.b_hours[sub1]:
                                    self.var.pos_b = self.xyz(self.var.pos_b, sub1, type1, self.var.b, 'b', day)
                                break
                            else:
                                if self.var.b_hours[sub1]:
                                    self.var.pos_b = self.normal_classes(self.var.pos_b, sub1, type1, self.var.b, 'b', day)
                                break
                    else:
                        self.update_subs(self.var.pos_b)
                        shuffle(self.var.subs)
                        for sub in self.var.subs:
                            sub1 = sub[0]
                            type1 = sub[1]
                            if not self.var.b_hours[sub1] > hours.hour_greaterthan(type1, day):
                                continue
                            if self.var.class_engaged[self.var.b_fac[sub1]]:
                                continue
                            if type1 in ['spl']:
                                if self.var.is_spl_done_for_week:
                                    continue
                                return_val = self.Spl(sub1, self.var.pos_b, day)
                                break
                            if type1 in ['lab1', 'lab2', 'lab3']:
                                if self.var.b_hours[sub1]:
                                    self.var.pos_b = self.xyz(self.var.pos_b, sub1, type1, self.var.b, 'b', day)
                                break
                            else:
                                if self.var.b_hours[sub1]:
                                    self.var.pos_b = self.normal_classes(self.var.pos_b, sub1, type1, self.var.b, 'b', day)
                                break

                if isinstance(self.var.pos_c, int) and self.var.pos_c < 7:
                    if day >= 3:
                        sub_dict = {key: val for key, val in sorted(self.var.c_hours.items(), key=lambda ele: ele[1], reverse=True)}
                        for sub, hour_left in sub_dict.items():
                            sub1 = sub
                            hour_left = sub
                            with sqlite3.connect(path_to_db):
                                cur = conn.cursor()
                                cur.execute('select sub_type from subjects where sub_short_name = ?', (sub,))
                                type1 = cur.fetchone()[0]
                            if not hours.hour_greaterthan(type1, day) < self.var.c_hours[sub1]:
                                continue
                            if self.var.class_engaged[self.var.c_fac[sub1]]:
                                continue
                            if type1 in ['spl']:
                                if self.var.is_spl_done_for_week:
                                    continue
                                return_val = self.Spl(sub1, self.var.pos_c, day)
                                self.var.is_spl_done_for_week = True
                                break
                            if type1 in ['lab1', 'lab2', 'lab3']:
                                if self.var.c_hours[sub1]:
                                    self.var.pos_c = self.xyz(self.var.pos_c, sub1, type1, self.var.c, 'c', day)
                                break
                            else:
                                if self.var.c_hours[sub1]:
                                    self.var.pos_c = self.normal_classes(self.var.pos_c, sub1, type1, self.var.c, 'c', day)
                                break
                    else:
                        self.update_subs(self.var.pos_c)
                        shuffle(self.var.subs)
                        for sub in self.var.subs:
                            sub1 = sub[0]
                            type1 = sub[1]
                            if not self.var.c_hours[sub1] > hours.hour_greaterthan(type1, day):
                                continue
                            if self.var.class_engaged[self.var.c_fac[sub1]]:
                                continue
                            if type1 in ['spl']:
                                if self.var.is_spl_done_for_week:
                                    continue
                                return_val = self.Spl(sub1, self.var.pos_c, day)
                                self.var.is_spl_done_for_week = True
                                break
                            if type1 in ['lab1', 'lab2', 'lab3']:
                                if self.var.c_hours[sub1]:
                                    self.var.pos_c = self.xyz(self.var.pos_c, sub1, type1, self.var.c, 'c', day)
                                break
                            else:
                                if self.var.c_hours[sub1]:
                                    self.var.pos_c = self.normal_classes(self.var.pos_c, sub1, type1, self.var.c, 'c', day)
                                break
                self.var.decrement_it.clear()
            self.var.x.append(self.var.a.copy())
            self.var.y.append(self.var.b.copy())
            self.var.z.append(self.var.b.copy())
        return self.var.x, self.var.y, self.var.z


# time_table = create_time_table()
# x, y, z = time_table.final_call()
#
# print()
# for i in range(6):
#     try:
#         print(x[i])
#     except:
#         pass
# print()
# for i in range(6):
#     try:
#         print(y[i])
#     except:
#         pass
# print()
# for i in range(6):
#     try:
#         print(z[i])
#     except:
#         pass
