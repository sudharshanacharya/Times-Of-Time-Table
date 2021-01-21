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
        print("no of major", self.major_subs)
        print("no of theory", self.theory)
        print("no of nt theory", self.not_theory)
        print("labs", self.labs)
        print("spl", self.spl)
        print("minor", self.minor_subs)
        no_labs = self.labs
        print("no of labs", no_labs)
        total_subs = self.major_subs + self.not_theory + self.theory
        print("total_subs", total_subs)
        hours = (self.total_hours_per_week - (self.labs * 3 + self.minor_subs + self.spl * 2)) / total_subs
        print("hours in general", hours)
        per_sub = int(hours)
        print("hours per sub", per_sub)
        extra = (hours - per_sub) * total_subs
        print("remaining extra hours", extra)
        extra = round(extra)
        print(extra)
        per_major = per_sub
        per_not_theory = per_sub
        per_theory = per_sub
        if extra and extra >= self.major_subs:
            per_major = per_sub + 1
            extra = extra - self.major_subs
            print("extra", extra)
        if extra and extra >= self.not_theory:
            print("hello")
            per_not_theory = per_sub + 1
            extra = extra - self.not_theory
        print(
            per_major * self.major_subs + per_not_theory * self.not_theory + per_theory * self.theory + self.labs * 3 + self.minor_subs + self.spl * 2)
        if (
                per_major * self.major_subs + per_not_theory * self.not_theory + per_theory * self.theory + self.labs * 3 + self.minor_subs + self.spl * 2) <= 39:
            return per_major, per_not_theory, per_theory
# import sqlite3
# with sqlite3.connect('database/TimesOfTimeTable.db') as con:
#     cur = con.cursor()
#     print(count('lab', 5, cur))
#     cal = calculate_hours(5, cur)  # raise API not done
#     per_major, per_nt, per_t = cal.calculate()
#     print(per_t, per_nt, per_major)
#     print(count('lab', 5, cur))