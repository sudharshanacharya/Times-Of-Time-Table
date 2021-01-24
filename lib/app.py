import sqlite3
from lib.hours_per_sub import calculate_hours
from flask import Flask, flash, redirect, render_template, \
    request, url_for, g
from lib.create_time_table import create_time_table
import json

DATABASE = 'database/TimesOfTimeTable.db'

app = Flask(__name__)

a_query = None
b_query = None
c_query = None


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
@app.route('/index')
def index():
    time_table = create_time_table()
    a, b, c = time_table.final_call()
    return render_template('index.html'
                           , monday_a=a[0], tuesday_a=a[1], wednesday_a=a[2], thusday_a=a[3], friday_a=a[4],
                           saturday_a=a[5]
                           , monday_b=b[0], tuesday_b=b[1], wednesday_b=b[2], thusday_b=b[3], friday_b=b[4],
                           saturday_b=b[5]
                           , monday_c=c[0], tuesday_c=c[1], wednesday_c=c[2], thusday_c=c[3], friday_c=c[4],
                           saturday_c=c[5])



@app.route('/fac_detail')
def fac_detail():
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(
            "select fac_name, fac_short_name from faculty ")

        a_query = cur.fetchall()
        return render_template('edit_fac.html', a_query=a_query)


@app.route('/get_fac_info', methods=['POST', 'GET'])
def get_fac_info():
    name = request.form.get('name')
    sname = request.form.get('sname')
    sec = request.form.get('sec')
    print(name)
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        if len(name) * len(sname) is not 0:
            cur.execute("INSERT into Faculty (FAC_NAME, FAC_SHORT_NAME) VALUES(?,?);", (name, sname,))
        con.commit()
        cur.execute(
            "select fac_name, fac_short_name from faculty")
        a_query = cur.fetchall()
        return render_template('edit_fac.html', a_query=a_query)


@app.route('/del_fac_info', methods=['POST', 'GET'])
def del_fac_info():
    fname = request.form.get('delete')
    print(fname)
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute("DELETE from Faculty where FAC_SHORT_NAME=(?)", (fname,))
        con.commit()
        cur.execute("select fac_name, fac_short_name from faculty")
        a_query = cur.fetchall()
        return render_template('edit_fac.html', a_query=a_query)


@app.route('/sub_details')
def sub_details():
    with sqlite3.connect(DATABASE) as con:
        print("connected")
        cur = con.cursor()
        cur.execute(
            "select sub_name, sub_short_name, sub_code, sub_credit, sub_type, sem from subjects order by sub_code")
        a_query = cur.fetchall()
        return render_template('edit_sub.html', query=a_query)


@app.route('/get_sub_info', methods=['POST', 'GET'])
def get_sub_info():
    sname = request.form.get('sname')
    ssname = request.form.get('ssname')
    scode = request.form.get('scode')
    scredit = request.form.get('scredit')
    stype = request.form.get('stype')
    sem = request.form.get('sem')
    print(sname, ssname, scode, scredit, stype, sem)
    with sqlite3.connect(DATABASE) as con:
        print("connected")
        cur = con.cursor()
        if len(sname) * len(ssname) * len(scode) * len(scredit) * len(stype) * len(sem) != 0:
            cur.execute("""
            INSERT into subjects (sub_NAME, sub_SHORT_NAME, sub_code, sub_credit, sub_type, sem) VALUES(?,?, ?,?,?,?)
            """, (sname, ssname, scode, scredit, stype, sem,))
        con.commit()
        cur.execute(
            "select sub_name, sub_short_name, sub_code, sub_credit, sub_type, sem from subjects order by sub_code")

        return render_template('edit_sub.html', query=cur.fetchall())


@app.route('/del_sub_info', methods=['POST', 'GET'])
def del_sub_info():
    sname = request.form.get('delete')
    print(sname)
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute("DELETE from subjects where SUB_SHORT_NAME=?", (sname,))
        con.commit()
        cur.execute(
            "select sub_name, sub_short_name, sub_code, sub_credit, sub_type, sem from subjects order by sub_code")
        a_query = cur.fetchall()
        return render_template('edit_sub.html', query=a_query)


class sec:
    def __init__(self):
        self.sec = 'a'


s = sec()


@app.route('/assign')
def assign():
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute("""
        SELECT fac_short_name, sub_short_name, sec, rem_hours "Hours alloted" FROM faculty f, subjects s,sub_fac r
        WHERE r.fac_id = f.fac_id AND r.sub_id=s.sub_id AND sec=? order by sub_short_name
        """, (s.sec.upper(),))
        tups = cur.fetchall()

        subjects = list()
        faculties = list()
        cur.execute('select sub_short_name from subjects where sub_id not in (select sub_id from sub_fac)')
        for x in cur.fetchall():
            subjects.append(x[0])
        cur.execute('select fac_short_name from faculty')
        for x in cur.fetchall():
            faculties.append(x[0])
        faculties = {'faculties':faculties}
        subjects = {'subects' : subjects}

        return render_template('assign.html', query=tups, subjects=subjects, faculties=faculties)


@app.route('/get_assign_info', methods=['POST', 'GET'])
def get_assign_info():
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cal = calculate_hours(5, cur)  # raise API not done
        per_major, per_nt, per_t = cal.calculate()
        print(per_t, per_nt, per_major)
        fac_name = request.form.get('fname')
        if fac_name is not None:
            print("fac_name is not None")
            try:

                cur.execute("select fac_id from faculty where lower(fac_short_name) = lower (?)", (fac_name,))
                fac_id = cur.fetchone()[0]
                print("fac_id ", fac_id)
            except TypeError:
                print("object is of NoneType 'fac_id = cur.fetchone()[0]' not subscriptable ")
            except:
                print("Other Error")

            """ subject_name & get subject_id to enter into sub_fac table """
            try:
                sub_name = request.form.get('sname')
                cur.execute("select sub_id from subjects where lower(sub_short_name) = lower (?)", (sub_name,))
                sub_id = cur.fetchone()[0]
                print("sub_id", sub_id)
            except TypeError:
                print("object is of NoneType 'sub_id = cur.fetchone()[0]' not subscribable ")
            except:
                print("Other Error")
            try:
                cur.execute("select sub_type from subjects where sub_id = ?", (sub_id,))
            except NameError:
                print("sub_id is not defined")
            except:
                print("Other Error")

            sub_type = cur.fetchone()
            print("subject type", sub_type)
            s.sec = request.form.get('section')
            if sub_type == ('major',):
                try:
                    cur.execute("""
                            insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                            """, (fac_id, s.sec.upper(), sub_id, per_major,))
                except:
                    print("error inserting major subject, subject already present in database")

            elif sub_type == ('not_theory',):
                print("not theory")
                print("extra_hour")
                try:
                    cur.execute("""
                                insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                            """, (fac_id, s.sec.upper(), sub_id, per_nt,))
                except:
                    print("error inserting not_theory subject, subject already present in database")

            elif sub_type == ('theory',):
                print("theory")
                print("extra_hour")
                try:
                    cur.execute("""
                                insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                            """, (fac_id, s.sec.upper(), sub_id, per_t,))
                except:
                    print("error inserting theory subject, subject already present in database")

            elif sub_type in [('lab1',), ('lab2',), ('lab3',)]:
                try:
                    cur.execute("""
                                insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                            """, (fac_id, s.sec.upper(), sub_id, 3,))
                except:
                    print("error inserting lab subject, subject already present in database")

            elif sub_type == ('minor',):
                cur.execute("""
                                insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                            """, (fac_id, s.sec.upper(), sub_id, 1,))


            else:
                try:
                    cur.execute("""
                                insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                            """, (fac_id, s.sec.upper(), sub_id, 2,))
                except:
                    print("error inserting spl subject, subject already present in database")
        con.commit()
        # print("2", sec)
        # if sec is None or sec not in ['A', 'B', 'C']:
        #     print("3",sec)
        a = request.form.get('section')
        if a == None:
            pass
        else:
            s.sec = request.form.get('section')
        # print("4",sec)
        cur.execute("""
                SELECT fac_short_name, sub_short_name, sec, rem_hours "Hours alloted" FROM faculty f, subjects s,sub_fac r
                WHERE r.fac_id = f.fac_id AND r.sub_id=s.sub_id AND sec=? order by sub_short_name 
                """, (s.sec.upper(),))
        tups = cur.fetchall()

        subjects = list()
        faculties = list()
        cur.execute('select sub_short_name from subjects where sub_id not in (select sub_id from sub_fac)')
        for x in cur.fetchall():
            subjects.append(x[0])
        cur.execute('select fac_short_name from faculty')
        for x in cur.fetchall():
            faculties.append(x[0])
        faculties = {'faculties': faculties}
        subjects = {'subects': subjects}
        print(subjects)
        print(faculties)
        return render_template('assign.html', query=tups, subjects=json.dumps(subjects), faculties=json.dumps(faculties))

@app.route('/del_assign_info', methods=['POST', 'GET'])
def del_assign_info():
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        ssname = request.form.get('delete')
        cur.execute("""
        delete from sub_fac where sub_id is (select sub_id from subjects where sub_short_name =?) and sec = ?
        """, (ssname, s.sec,))
        con.commit()
        cur.execute("""
                        SELECT fac_short_name, sub_short_name, sec, rem_hours "Hours alloted" FROM faculty f, subjects s,sub_fac r
                        WHERE r.fac_id = f.fac_id AND r.sub_id=s.sub_id AND sec=? order by sub_short_name
                        """, (s.sec.upper(),))
        tups = cur.fetchall()
        subjects = list()
        faculties = list()
        cur.execute('select sub_short_name from subjects where sub_id not in (select sub_id from sub_fac)')
        for x in cur.fetchall():
            subjects.append(x[0])
        cur.execute('select fac_short_name from faculty')
        for x in cur.fetchall():
            faculties.append(x[0])
        faculties = {'faculties': faculties}
        subjects = {'subects': subjects}
        return render_template('assign.html', query=tups, subjects=json.dumps(subjects), faculties=json.dumps(faculties))


@app.route('/time_table')
def time_table():
    time_table = create_time_table()
    a, b, c = time_table.final_call()
    return render_template('time_table.html'
                           , monday_a=a[0], tuesday_a=a[1], wednesday_a=a[2], thusday_a=a[3], friday_a=a[4],
                           saturday_a=a[5]
                           , monday_b=b[0], tuesday_b=b[1], wednesday_b=b[2], thusday_b=b[3], friday_b=b[4],
                           saturday_b=b[5]
                           , monday_c=c[0], tuesday_c=c[1], wednesday_c=c[2], thusday_c=c[3], friday_c=c[4],
                           saturday_c=c[5])


@app.route('/refresh', methods=['POST', 'GET'])
def refresh():
    time_table = create_time_table()
    a, b, c = time_table.final_call()
    _day = 0
    which_day = None
    with sqlite3.connect('database/TimesOfTimeTable.db') as con:
        cur = con.cursor()
        for x in a:
            for y in x:
                if _day == 0:
                    which_day = 'monday'
                elif _day == 1:
                    which_day = 'tuesday'
                elif _day == 2:
                    which_day = 'wednesday'
                elif _day == 3:
                    which_day = 'thusday'
                elif _day == 4:
                    which_day = 'friday'
                elif _day == 5:
                    which_day = 'saturday'
                _day += 1

                # for sub in y:
                #     cur.execute('insert into time_table_for_a (?) values(?)', (which_day, sub,))

    return render_template('time_table.html'
                           , monday_a=a[0], tuesday_a=a[1], wednesday_a=a[2], thusday_a=a[3], friday_a=a[4],
                           saturday_a=a[5]
                           , monday_b=b[0], tuesday_b=b[1], wednesday_b=b[2], thusday_b=b[3], friday_b=b[4],
                           saturday_b=b[5]
                           , monday_c=c[0], tuesday_c=c[1], wednesday_c=c[2], thusday_c=c[3], friday_c=c[4],
                           saturday_c=c[5])
