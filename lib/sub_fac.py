import sqlite3
from lib.queries import queries
from lib.hours_per_sub import hours_per_sub

hours = hours_per_sub()
hours.labs = 3
hours.minor_subs = 1
hours.total_major_subs = 6

per_sub, extra = hours_per_sub.calculate(hours)
print(per_sub, extra)

conn = sqlite3.connect("database/TimesOfTimeTable.db")
cur = conn.cursor()

#cur.execute("drop table sub_fac_5th_sem")
cur.execute(queries.sub_fac_5th_sem)

sec = input("Enter section: ").upper()
for a in range(hours.total_major_subs):


    try:
        fac_name = input("Enter fac_name: ")
        cur.execute("select fac_id from faculty where lower(fac_short_name) = lower (?)", (fac_name,))
        fac_id = cur.fetchone()[0]
    except TypeError:
        print("object is of NoneType 'fac_id = cur.fetchone()[0]' not subscriptable ")
        continue
    except :
        print("Other Error")
        continue


    try:
        sub_name = input("Enter sub_name: ")
        cur.execute("select sub_id from subjects where lower(sub_short_name) = lower (?)", (sub_name,))
        sub_id = cur.fetchone()[0]
    except TypeError:
        print("object is of NoneType 'sub_id = cur.fetchone()[0]' not subscriptable ")
        continue
    except:
        print("Other Error")
        continue



    if extra:
        try:
            cur.execute("select sub_type from subjects where sub_id = ?", (sub_id,))
        except NameError:
            print("sub_id is not defined")
            continue
        except:
            print("Other Error")
            continue


        if cur.fetchone() == ('M',):
            print("extra_hour")
            cur.execute("""
                insert into sub_fac_5th_sem (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                """, (fac_id, sec, sub_id, per_sub + 1,))
            extra -= 1
        else:
            print("no extra hour")
            cur.execute("""                                                                   
                    insert into sub_fac_5th_sem (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                    """, (fac_id, sec, sub_id, per_sub,))



    conn.commit()
    print("commited")
    print(cur.fetchall())
