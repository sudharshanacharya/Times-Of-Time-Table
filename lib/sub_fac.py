import sqlite3
from lib.queries import queries
from lib.hours_per_sub import calculate_hours

def edit_sub_fac(drop_table=False, create_table=False,):
    cal = calculate_hours(5)  # raise API not done
    per_major, per_nt, per_t = cal.calculate()

    conn = sqlite3.connect("database/TimesOfTimeTable.db")
    cur = conn.cursor()

    if drop_table:
        cur.execute("drop table if exists sub_fac")
        print("Table Dropped")
    if create_table:
        cur.execute(queries.sub_fac)
    cur.execute(queries.sub_fac)

    sec = input("Enter section(A , B  or C): ").upper()

    cur.execute("SELECT count(sub_name) from subjects where sem = '5'")

    for a in range(cur.fetchone()[0]):
        """ faculty_name and get faculty_id to enter into sub_fac table """
        try:
            fac_name = input("Enter fac_name: ")
            cur.execute("select fac_id from faculty where lower(fac_short_name) = lower (?)", (fac_name,))
            fac_id = cur.fetchone()[0]
            print(fac_id)
        except TypeError:
            print("object is of NoneType 'fac_id = cur.fetchone()[0]' not subscriptable ")
            continue
        except:
            print("Other Error")
            continue

        """ subject_name & get subject_id to enter into sub_fac table """
        try:
            sub_name = input("Enter sub_name: ")
            cur.execute("select sub_id from subjects where lower(sub_short_name) = lower (?)", (sub_name,))
            sub_id = cur.fetchone()[0]
            print(sub_id)
        except TypeError:
            print("object is of NoneType 'sub_id = cur.fetchone()[0]' not subscribable ")
            continue
        except:
            print("Other Error")
            continue


        try:
            cur.execute("select sub_type from subjects where sub_id = ?", (sub_id,))
        except NameError:
            print("sub_id is not defined")
            continue
        except:
            print("Other Error")
            continue

        sub_type = cur.fetchone()
        if sub_type == ('major',):
            print("major")
            print("extra_hour")
            cur.execute("""
                        insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                        """, (fac_id, sec, sub_id, per_major,))
        elif sub_type == ('not_theory',):
            print("not theory")
            print("extra_hour")
            cur.execute("""
                            insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                        """, (fac_id, sec, sub_id, per_nt,))

        elif sub_type == ('theory',):
            print("theory")
            print("extra_hour")
            cur.execute("""
                            insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                        """, (fac_id, sec, sub_id, per_t,))

        elif sub_type == ('lab',):
            cur.execute("""
                            insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                        """, (fac_id, sec, sub_id, 3,))

        elif sub_type == ('minor',):
            cur.execute("""
                            insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                        """, (fac_id, sec, sub_id, 1,))

        else :
            cur.execute("""
                            insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                        """, (fac_id, sec, sub_id, 2,))

        conn.commit()
        print("comited")

    conn.commit()
    conn.close()