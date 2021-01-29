import sqlite3

path_to_db = '/home/peter/PycharmProjects/TimesOfTimeTable/demoapp/database/TimesOfTimeTable.db'
conn = sqlite3.connect(path_to_db)
cur = conn.cursor()


class queries:
    create_table_subjects = """
         CREATE TABLE IF NOT EXISTS "subjects" (
	    "sub_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	    "sub_short_name"	varchar(8) NOT NULL,
	    "sub_name"	varchar(20) NOT NULL,
	    "sub_code"	varchar(10) NOT NULL,
	    "sub_credit"	int NOT NULL,
	    "sub_type"	varchar(10) NOT NULL,
	    "SEM"	INTEGER NOT NULL
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
         sub_id int not null ,
         rem_hours int not null,
         constraint _fac_id foreign key(fac_id) references faculty(fac_id) on delete cascade ,
         constraint _sub_id foreign key(sub_id) references subjects(sub_id) on delete cascade ,
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

    """" view2 is using now """
    view2 = """
        create view if not exists view2 as SELECT r.*, f.fac_short_name, s.sub_short_name 
        from sub_fac r, faculty f, subjects s 
        WHERE r.fac_id = f.fac_id and r.sub_id = s.sub_id ;
    """
    def drop_table(self, table):
        cur.execute("drop table if exists ?", (table,))

    def check_hours(self):
        cur.execute("select sum(rem_hours) from subjects")
        return cur.fetchone()

    memory_a = """ create table if not EXISTS memory_a(
    id INTEGER primary KEY ,
    period1 varchar (15),
    period2 varchar (15),
    period3 varchar (15),
    period4 varchar (15),
    period5 varchar (15),
    period6 varchar (15),
    period7 varchar (15)
	);
    )"""

    memory_b = """ create table if not EXISTS memory_b(
        id INTEGER primary KEY ,
        period1 varchar (15),
        period2 varchar (15),
        period3 varchar (15),
        period4 varchar (15),
        period5 varchar (15),
        period6 varchar (15),
        period7 varchar (15)
    	);
        )"""

    memory_c = """ create table if not EXISTS memory_c(
        id INTEGER primary KEY ,
        period1 varchar (15),
        period2 varchar (15),
        period3 varchar (15),
        period4 varchar (15),
        period5 varchar (15),
        period6 varchar (15),
        period7 varchar (15)
    	);
        )"""

    back_up = """
        CREATE TABLE IF NOT EXISTS "subjects_backup" (
	    "sub_id"	INTEGER PRIMARY KEY,
	    "sub_short_name"	varchar(8) NOT NULL,
	    "sub_name"	varchar(20) NOT NULL,
	    "sub_code"	varchar(10) NOT NULL,
	    "sub_credit"	int NOT NULL,
	    "sub_type"	varchar(10) NOT NULL,
	    "SEM"	INTEGER NOT NULL
         );
    """
