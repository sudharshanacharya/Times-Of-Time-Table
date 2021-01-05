import sqlite3

conn = sqlite3.connect('database/TimesOfTimeTable.db')
cur = conn.cursor()


class queries:
    create_table_subjects = """
         create table subjects(
         sub_id INTEGER PRIMARY KEY AUTOINCREMENT,
         sub_short_name varchar(8) not null ,
         sub_name varchar(20) not null,
         sub_code varchar(10) not null,
         sub_credit int not null,
         sub_type varchar(10) not null 
         );
         """

    create_table_faculties = """
         create table faculty(
         fac_id INTEGER PRIMARY KEY AUTOINCREMENT,
         fac_short_name varchar(5) not null ,
         fac_name varchar(20) not null
         );
         """

    sub_fac_5th_sem = """
         create table sub_fac_5th_sem(
         fac_id int unique not null,
         sec varchar(3) not null,
         sub_id int unique not null,
         rem_hours int not null,
         constraint _fac_id foreign key(fac_id) references faculty(fac_id),
         constraint _sub_id foreign key(sub_id) references subjects(sub_id),
         constraint pri_sub_fac primary key(fac_id, sub_id)
         );
         """

    def drop_table(self, table):
        cur.execute("drop table if exists ?", (table,))

    def check_hours(self):
        cur.execute("select sum(rem_hours) from subjects")
        return cur.fetchone()
