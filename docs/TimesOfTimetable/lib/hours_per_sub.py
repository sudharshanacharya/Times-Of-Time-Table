def count(sub_type, sem, cur):
    cur.execute("select count(sub_type) from subjects where sub_type = ? and sem = ?", (sub_type, sem,))
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
