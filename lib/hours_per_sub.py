path_to_db = '/home/peter/PycharmProjects/TimesOfTimeTable/demoapp/database/TimesOfTimeTable.db'
def count(sub_type, sem, cur):
    if sub_type == 'lab':
        cur.execute("select count(sub_type) from subjects where sem = ? and  sub_type in ('lab1', 'lab2', 'lab3')", (sem,))
        return cur.fetchall()
    else:
        cur.execute("select count(sub_type) from subjects where sem = ? and  sub_type is ?", (sem, sub_type,))
        return cur.fetchall()


class calculate_hours:
    """total hours per subject"""

    def __init__(self, sem, cur):
        self.sem = sem
        self.theory = count("theory", sem, cur)[0][0]
        self.not_theory = count("not_theory", sem, cur)[0][0]
        self.labs = count("lab", sem, cur)[0][0]
        self.minor_subs = count("minor", sem, cur)[0][0]
        self.major_subs = count("major", sem, cur)[0][0]
        self.spl = count("spl", sem, cur)[0][0]
        self.total_hours_per_week = 39

    def calculate(self):
        no_labs = self.labs
        total_subs = self.major_subs + self.not_theory + self.theory
        hours = (self.total_hours_per_week - (self.labs * 3 + self.minor_subs + self.spl * 2)) / total_subs
        per_sub = int(hours)
        extra = (hours - per_sub) * total_subs
        extra = round(extra)
        per_major = per_sub
        per_not_theory = per_sub
        per_theory = per_sub
        if extra and extra >= self.major_subs:
            per_major = per_sub + 1
            extra = extra - self.major_subs
        if extra and extra >= self.not_theory:
            per_not_theory = per_sub + 1
            extra = extra - self.not_theory
        if (
                per_major * self.major_subs + per_not_theory * self.not_theory + per_theory * self.theory + self.labs * 3 + self.minor_subs + self.spl * 2) <= 39:
            return per_major, per_not_theory, per_theory

def hour_greaterthan(type1, day):
    if type1 == 'minor':
        return 0
    if type1 in ['lab1', 'lab2', 'lab3']:
        return 0
    if type1 == 'spl':
        return 0
    import sqlite3
    with sqlite3.connect(path_to_db) as con:
        cur = con.cursor()
        cal = calculate_hours(5, cur)
        per_major, per_not_theory, per_theory = cal.calculate()
        if type1 == 'theory':
            return per_theory - (day + 1)*2
        if type1 == 'not_theory':
            return per_not_theory - (day + 1)*2
        if type1 == 'major':
            return per_major - (day + 1)*2
