# import sqlite3
# from flask import Flask, request, render_template, redirect, url_for
# from lib import sub_input
# from lib.queries import queries
# from subprocess
#
# app = Flask(__name__)
# #@app.route("/")
# @app.route("/sub_input")
# def sub_input(no_sub = 1,sub_short_name = 'ss', sub_name = 'ssss',sub_code = '1111', sub_credit = 1,sub_type = 'not_theory', sem = 5, drop_table = False, create_table = False):
#     conn = sqlite3.connect("database/TimesOfTimeTable.db")
#     cur = conn.cursor()
#     if drop_table:
#         queries.drop_table('subjects')
#         # cur.execute("drop table if EXISTS subjects ")
#         print("Table Dropped")
#     if create_table:
#         cur.execute(queries.create_table_subjects)
#
#     for i in range(no_sub):
#         print("subject (?)", i)
#         #sub_name = input("Enter sub_nam: ")
#         #sub_short_name = input("Enter sub_short_name: ")
#         #sub_code = input("Enter sub_code: ")
#         #sub_credit = input("Enter sub_credit: ")
#         #sub_type = input("Enter sub_type: ")
#
#         cur.execute("""
#         insert into subjects (sub_short_name,sub_name, sub_code, sub_credit, sub_type, sem)
#         values(?,?,?,?,?)
#         """, (sub_short_name, sub_name, sub_code, sub_credit, sub_type,sem,))
#
#     conn.commit()
#     conn.close()
#     return render_template('faculty.html')
#
# @app.route("/")
# @app.route("/main")
# def main():
#     return render_template("main.html")
#
#
# @app.route("/ftable.html")
# def ftable():
#     return render_template("ftable.html")
#
#
# @app.route("/dropdown.html")
# def dropdown():
#     return render_template("dropdown.html")
#
#
# @app.route("/subjects.html")
# def subjects():
#     return render_template("subjects.html")
#
# @app.route("/get_sub_info", methods=['POST'])
# def get_sub_info():
#     print("receiving data")
#     sid = request.form.get('sid')
#     short_name = request.form.get('ssname')
#     name = request.form.get('sfname')
#     scode = request.form.get('scode')
#     credit = request.form.get('scredit')
#     stype = request.form.get('stype')
#     sem = request.form.get('sem')
#     return redirect(url_for('sub_input',no_sub=1, sub_short_name=short_name, sub_name=name, sub_code=scode, sub_credit=credit , sub_type=stype, sem=sem))
#
# @app.route("/faculty.html")
# def faculty():
#     return render_template("faculty.html")
#
#
# @app.route("/get_fac_info", methods=['POST'])
# def get_fac_info():
#     name = request.form.get('name')
#     short_name = request.form.get('short_name')
#     return "successfully entered"
