import sqlite3

path_to_db = '/home/peter/PycharmProjects/TimesOfTimeTable/demoapp/database/TimesOfTimeTable.db'
conn = sqlite3.connect(path_to_db)
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

    sub_fac = """
         create table if not exists sub_fac(
         fac_id int not null,
         sec varchar(3) not null,
         sub_id int not null,
         rem_hours int not null,
         constraint _fac_id foreign key(fac_id) references faculty(fac_id),
         constraint _sub_id foreign key(sub_id) references subjects(sub_id),
         constraint pri_sub_fac primary key(fac_id, sub_id)
         );
         """

    get_a_fac = """
        select fac_short_name from Faculty where fac_id in (select fac_id from sub_fac where sec = 'A')    """
    get_b_fac = """
    select fac_short_name from Faculty where fac_id in (select fac_id from sub_fac where sec = 'B')
    """
    get_c_fac = """
    select fac_short_name from Faculty where fac_id in (select fac_id from sub_fac where sec = 'C')
    """

    get_rem_hours = """
    select 
    """

    view1 = """
    create view if not exists view1 as SELECT r.*, f.fac_short_name from sub_fac r, faculty f WHERE r.fac_id = f.fac_id;
    """

    view2 = """
        create view if not exists view2 as SELECT r.*, f.fac_short_name, s.sub_short_name from sub_fac r, faculty f, subjects s WHERE r.fac_id = f.fac_id and r.sub_id = s.sub_id ;
    """
    def drop_table(self, table):
        cur.execute("drop table if exists ?", (table,))

    def check_hours(self):
        cur.execute("select sum(rem_hours) from subjects")
        return cur.fetchone()
