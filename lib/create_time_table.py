import sqlite3
from lib.queries import queries

conn = sqlite3.connect("database/TimesOfTimeTable.db")
cur = conn.cursor()
cur.execute("""SELECT sub_short_name FROM subjects WHERE SEM = 5;""")
subs = list()
for row in cur.fetchall():
    subs.append(row[0])
print(subs)

a_fac = []

cur.execute(queries.get_a_fac)
for row in cur.fetchall():
    print(row)
    #a_fac.append(row[0])

#print(a_fac)

""" create a view by joining table 'sub_fac' & 'faculty' table """
""" select fac_short_name & rem hours """
""" store it in a dictionary """
""" a_fac = {"plk" : 5, "sup": 5, "mr" : 4 }"""
""" add faculty to "a_sec" dictionary & decrement ; make a_fac["fac"] -=1 """
""" make class_engaged[fac] = 1 """
""" check if class_engaegd[b_fac[i]] == 1;  if so swap assign to b_sec; make class_engaged[swaped_fac] = 1"""
""" after each itteraiton release faculties"""