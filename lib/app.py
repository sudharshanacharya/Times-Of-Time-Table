import sqlite3
from lib.hours_per_sub import calculate_hours
from flask import Flask, flash, redirect, render_template, \
    request, url_for, g


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
def index():
    return render_template('index.html')


# def sub_input(sub_name, sub_short_name, sub_code, sub_credit, sub_type, sem, drop_table=False,
#               create_table=False):
#     with sqlite3.connect(DATABASE) as con:
#         cur = con.cursor()
#         cur.execute("""
#             insert into subjects (sub_short_name,sub_name, sub_code, sub_credit, sub_type, sem)
#             values(?,?,?,?,?)
#             """, (sub_short_name, sub_name, sub_code, sub_credit, sub_type, sem,))
#         con.commit()
#     msg = 'record successfully added'
#     return msg

# cur = get_db().cursor()
# if drop_table:
#     cur.execute("drop table if exists subjects")
# if create_table:
#     cur.execute(queries.create_table_subjects)
# cur.execute("""
# insert into subjects (sub_short_name,sub_name, sub_code, sub_credit, sub_type, sem)
# values(?,?,?,?,?)
# """, (sub_short_name, sub_name, sub_code, sub_credit, sub_type, sem,))


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or \
#                 request.form['password'] != 'secret':
#             error = 'Invalid credentials'
#             flash('You were successfully logged in')
#         else:
#             flash('You were successfully logged in')
#             return redirect(url_for('index'))
#     return render_template('login.html', error=error)


@app.route('/sub_input')
def sub_input():
    return render_template('sub_input.html')


# @app.route('/get_sub_info', methods=['POST', 'GET'])
# def get_sub_info():
#     name = request.form.get('name')
#     sname = request.form.get('sname')
#     scode = request.form.get('scode')
#     credit = request.form.get('credit')
#     stype = request.form.get('stype')
#     sem = request.form.get('sem')
#     with sqlite3.connect(DATABASE) as con:
#         cur = con.cursor()
#         cur.execute("""
#                 insert into subjects (sub_name,sub_short_name, sub_code, sub_credit, sub_type, sem)
#                 values(?,?,?,?,?,?)
#                 """, (name, sname, scode, credit, stype, sem,))
#         con.commit()

#     return render_template('result.html')


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
    sname = request.form.get('delete')
    print(sname)
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute("DELETE from Faculty where FAC_SHORT_NAME=(?)", (sname,))
        con.commit()
        cur.execute("select fac_name, fac_short_name from faculty")
        a_query = cur.fetchall()
        return render_template('edit_fac.html', a_query=a_query)


@app.route('/sub_details')
def sub_details():
    with sqlite3.connect(DATABASE) as con:
        print("connected")
        cur = con.cursor()
        cur.execute("select sub_name, sub_short_name, sub_code, sub_credit, sub_type, sem from subjects")
        a_query = cur.fetchall()
        return render_template('edit_sub.html', query=a_query)


@app.route('/get_sub_info', methods=['POST', 'GET'])
def get_sub_info():
    sname = request.form.get('sname')
    ssname = request.form.get('sname')
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
        cur.execute("select sub_name, sub_short_name, sub_code, sub_credit, sub_type, sem from subjects")

        return render_template('edit_sub.html', query=cur.fetchall())


@app.route('/del_sub_info', methods=['POST', 'GET'])
def del_sub_info():
    sname = request.form.get('delete')
    print(sname)
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute("DELETE from subjects where SUB_SHORT_NAME=(?)", (sname,))
        con.commit()
        cur.execute("select sub_name, sub_short_name, sub_code, sub_credit, sub_type, sem from subjects")
        a_query = cur.fetchall()
        return render_template('edit_sub.html', query=a_query)


@app.route('/assign')
def assign():
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute("""
        SELECT fac_short_name, sub_short_name, sec FROM faculty f, subjects s,sub_fac r
            WHERE r.fac_id = f.fac_id AND r.sub_id=s.sub_id AND sec='A';
        """)
        tups = cur.fetchall()
        print(tups)
        return render_template('assign.html', query=tups)

@app.route('/get_assign_info')
def get_assign_info():
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cal = calculate_hours(5, cur)  # raise API not done
        per_major, per_nt, per_t = cal.calculate()
        try:
            fac_name = request.form.get('fname')
            cur.execute("select fac_id from faculty where lower(fac_short_name) = lower (?)", (fac_name,))
            fac_id = cur.fetchone()[0]
            print(fac_id)
        except TypeError:
            print("object is of NoneType 'fac_id = cur.fetchone()[0]' not subscriptable ")
        finally:
            print("Other Error")

        """ subject_name & get subject_id to enter into sub_fac table """
        try:
            sub_name = request.form.get('sname')
            cur.execute("select sub_id from subjects where lower(sub_short_name) = lower (?)", (sub_name,))
            sub_id = cur.fetchone()[0]
            print(sub_id)
        except TypeError:
            print("object is of NoneType 'sub_id = cur.fetchone()[0]' not subscribable ")
        finally:
            print("Other Error")
        try:
            cur.execute("select sub_type from subjects where sub_id = ?", (sub_id,))
        except NameError:
            print("sub_id is not defined")
        finally:
            print("Other Error")

        sub_type = cur.fetchone()
        sec = request.form.get('sec')
        if sub_type == ('major',):
            try:
                cur.execute("""
                        insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                        """, (fac_id, sec, sub_id, per_major,))
            except:
                print("subject already exists")

        elif sub_type == ('not_theory',):
            print("not theory")
            print("extra_hour")
            try:
                cur.execute("""
                            insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                        """, (fac_id, sec, sub_id, per_nt,))
            except:
                print("subject already exists")

        elif sub_type == ('theory',):
            print("theory")
            print("extra_hour")
            try:
                cur.execute("""
                            insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                        """, (fac_id, sec, sub_id, per_t,))
            except:
                print("subject already exists")

        elif sub_type == ('lab',):
            try:
                cur.execute("""
                            insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                        """, (fac_id, sec, sub_id, 3,))
            except:
                print("subject already exists")

        elif sub_type == ('minor',):
            cur.execute("""
                            insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                        """, (fac_id, sec, sub_id, 1,))


        else:
            try:
                cur.execute("""
                            insert into sub_fac (fac_id,sec,sub_id, rem_hours) values (?, ?, ? ,?)
                        """, (fac_id, sec, sub_id, 2,))
            except:
                print("subject already exists")

    return render_template('assign.html')

@app.route('/del_assign_info')
def del_assign_info():
    return render_template('assign.html')