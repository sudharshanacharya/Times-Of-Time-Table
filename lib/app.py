import sqlite3
from lib import queries
from flask import Flask, flash, redirect, render_template, \
    request, url_for, g

DATABASE = 'database/TimesOfTimeTable.db'

app = Flask(__name__)


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


def query_insert():
    """"""


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


@app.route('/get_sub_info', methods=['POST', 'GET'])
def get_sub_info():
    name = request.form.get('name')
    sname = request.form.get('sname')
    scode = request.form.get('scode')
    credit = request.form.get('credit')
    stype = request.form.get('stype')
    sem = request.form.get('sem')
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute("""
                insert into subjects (sub_name,sub_short_name, sub_code, sub_credit, sub_type, sem)
                values(?,?,?,?,?,?)
                """, (name, sname, scode, credit, stype, sem,))
        con.commit()
    return render_template('result.html')



@app.route('/display_fac' ,methods=['POST', 'GET'])
def display_fac():
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute("select fac_name, fac_short_name from faculty")
        return render_template('fac_input.html', a_query=cur.fetchall())



#app.run(debug=True)
