import sqlite3
from lib.queries import queries
from lib.hours_per_sub import calculate_hours

conn = sqlite3.connect("database/Times-Of-Time-Table")
cur = conn.cursor()

def count(sub_type):
    cur.execute("select count(sub_type) from subjects where sub_type = '?'", (sub_type,))
    return cur.fetchall()



cal = calculate_hours()


no_major = count("major")
no_minor = count("minor")
theory = count("T")
not_theory = count("NT")
lab = count("lab")

cal.minor_subs = no_minor
cal.major_subs = no_major+theory+not_theory
cal.labs = lab

hour, extra = cal.calculate()
print(hour, extra)