BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "custom" (
	"sname"	varchar(20),
	"stype"	varchar(20),
	"timing"	int
);
CREATE TABLE IF NOT EXISTS "sub_fac" (
	"fac_id"	int NOT NULL,
	"sec"	varchar(3) NOT NULL,
	"sub_id"	int NOT NULL,
	"rem_hours"	int NOT NULL,
	CONSTRAINT "_sub_id" FOREIGN KEY("sub_id") REFERENCES "subjects"("sub_id") on delete cascade,
	CONSTRAINT "_fac_id" FOREIGN KEY("fac_id") REFERENCES "faculty"("fac_id") on delete cascade
);
CREATE TABLE IF NOT EXISTS "subjects_backup" (
	"sub_id"	INTEGER,
	"sub_short_name"	varchar(8) NOT NULL,
	"sub_name"	varchar(20) NOT NULL,
	"sub_code"	varchar(10) NOT NULL,
	"sub_credit"	int NOT NULL,
	"sub_type"	varchar(10) NOT NULL,
	"SEM"	INTEGER NOT NULL,
	PRIMARY KEY("sub_id")
);
CREATE TABLE IF NOT EXISTS "subjects" (
	"sub_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"sub_short_name"	varchar(8) NOT NULL,
	"sub_name"	varchar(20) NOT NULL,
	"sub_code"	varchar(10) NOT NULL,
	"sub_credit"	int NOT NULL,
	"sub_type"	varchar(10) NOT NULL,
	"SEM"	INTEGER
);
CREATE TABLE IF NOT EXISTS "memory_a" (
	"id"	INTEGER,
	"period1"	varchar(15),
	"period2"	varchar(15),
	"period3"	varchar(15),
	"period4"	varchar(15),
	"period5"	varchar(15),
	"period6"	varchar(15),
	"period7"	varchar(15),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "memory_b" (
	"id"	INTEGER,
	"period1"	varchar(15),
	"period2"	varchar(15),
	"period3"	varchar(15),
	"period4"	varchar(15),
	"period5"	varchar(15),
	"period6"	varchar(15),
	"period7"	varchar(15),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "memory_c" (
	"id"	INTEGER,
	"period1"	varchar(15),
	"period2"	varchar(15),
	"period3"	varchar(15),
	"period4"	varchar(15),
	"period5"	varchar(15),
	"period6"	varchar(15),
	"period7"	varchar(15),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "Faculty" (
	"FAC_ID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"FAC_SHORT_NAME"	VARCHAR(8),
	"FAC_NAME"	VARCHAR(25)
);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('dbms','major',-1);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('python','not_theory',-1);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('unix','not_theory',-1);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('env','minor',-1);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('cns_lab','lab2',0);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('cns_lab','lab2',1);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('cns_lab','lab2',4);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('dbms_lab','lab1',0);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('dbms_lab','lab1',1);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('dbms_lab','lab1',4);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('apti','spl',0);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('apti','spl',2);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('apti','spl',4);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('cns','theory',-1);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('me','theory',-1);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('atc','major',-1);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('ic','lab3',0);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('ic','lab3',1);
INSERT INTO "custom" ("sname","stype","timing") VALUES ('ic','lab3',4);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (1,'a',22,4);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (4,'a',20,5);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (2,'a',21,4);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (3,'a',3,5);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (5,'a',5,4);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (12,'a',6,4);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (2,'a',8,2);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (1,'a',10,2);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (19,'a',7,1);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (15,'a',12,2);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (33,'a',11,2);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (7,'b',22,4);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (3,'b',3,5);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (8,'b',20,5);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (11,'b',21,4);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (9,'b',5,4);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (10,'b',6,4);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (11,'b',8,2);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (9,'b',10,2);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (33,'b',11,2);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (15,'b',12,2);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (6,'b',7,1);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (11,'c',22,4);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (16,'c',21,4);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (17,'c',3,5);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (8,'c',20,5);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (18,'c',5,4);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (10,'c',8,2);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (17,'c',10,2);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (6,'c',7,1);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (33,'c',11,2);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (15,'c',12,2);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (19,'c',6,4);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (3,'a',3,5);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (36,'a',3,5);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (4,'a',25,5);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (33,'a',26,2);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (8,'b',25,5);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (36,'b',3,5);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (33,'b',26,2);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (8,'c',25,5);
INSERT INTO "sub_fac" ("fac_id","sec","sub_id","rem_hours") VALUES (33,'c',26,2);
INSERT INTO "subjects_backup" ("sub_id","sub_short_name","sub_name","sub_code","sub_credit","sub_type","SEM") VALUES (11,'ic','ic','18csl57',0,'lab3',5);
INSERT INTO "subjects_backup" ("sub_id","sub_short_name","sub_name","sub_code","sub_credit","sub_type","SEM") VALUES (20,'atc','Automata Theory  of computability','15cs54',4,'major',5);
INSERT INTO "subjects_backup" ("sub_id","sub_short_name","sub_name","sub_code","sub_credit","sub_type","SEM") VALUES (24,'ic','ic','bullshit',0,'lab',5);
INSERT INTO "subjects" ("sub_id","sub_short_name","sub_name","sub_code","sub_credit","sub_type","SEM") VALUES (3,'dbms','Data Base Management System','15cs53',4,'major',5);
INSERT INTO "subjects" ("sub_id","sub_short_name","sub_name","sub_code","sub_credit","sub_type","SEM") VALUES (5,'python','Application Development Using Python','18cs55',4,'not_theory',5);
INSERT INTO "subjects" ("sub_id","sub_short_name","sub_name","sub_code","sub_credit","sub_type","SEM") VALUES (6,'unix','Unix Programming','18cs56',3,'not_theory',5);
INSERT INTO "subjects" ("sub_id","sub_short_name","sub_name","sub_code","sub_credit","sub_type","SEM") VALUES (7,'env','Environment','18cs55',1,'minor',5);
INSERT INTO "subjects" ("sub_id","sub_short_name","sub_name","sub_code","sub_credit","sub_type","SEM") VALUES (8,'cns_lab','cns laboratory','18csl55',2,'lab2',5);
INSERT INTO "subjects" ("sub_id","sub_short_name","sub_name","sub_code","sub_credit","sub_type","SEM") VALUES (10,'dbms_lab','dbms_laboratory','18csl56',2,'lab1',5);
INSERT INTO "subjects" ("sub_id","sub_short_name","sub_name","sub_code","sub_credit","sub_type","SEM") VALUES (12,'apti','aptitude','18cs78',1,'spl',5);
INSERT INTO "subjects" ("sub_id","sub_short_name","sub_name","sub_code","sub_credit","sub_type","SEM") VALUES (21,'cns','computer networks & security','18cs52',3,'theory',5);
INSERT INTO "subjects" ("sub_id","sub_short_name","sub_name","sub_code","sub_credit","sub_type","SEM") VALUES (22,'me','Management & Enterprenuorship','15cs51',3,'theory',5);
INSERT INTO "subjects" ("sub_id","sub_short_name","sub_name","sub_code","sub_credit","sub_type","SEM") VALUES (23,'unix','unix','18cs69',3,'not_theory',5);
INSERT INTO "subjects" ("sub_id","sub_short_name","sub_name","sub_code","sub_credit","sub_type","SEM") VALUES (25,'atc','Automata & Theory Of Computability','18cs54',4,'major',5);
INSERT INTO "subjects" ("sub_id","sub_short_name","sub_name","sub_code","sub_credit","sub_type","SEM") VALUES (26,'ic','ic','jhhgfklk',8,'lab3',5);
INSERT INTO "memory_a" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (1,'cns_lab','cns_lab','cns_lab','dbms','dbms','me','env');
INSERT INTO "memory_a" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (2,'unix','ic','ic','ic','me','unix','python');
INSERT INTO "memory_a" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (3,'cns','me','python','atc','dbms_lab','dbms_lab','dbms_lab');
INSERT INTO "memory_a" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (4,'atc','cns','dbms','atc','cns','python','unix');
INSERT INTO "memory_a" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (5,'apti','apti','dbms','atc','me','cns','python');
INSERT INTO "memory_a" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (6,'unix','dbms','atc','__','__','__','__');
INSERT INTO "memory_b" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (1,'python','atc','python','me','unix','unix','atc');
INSERT INTO "memory_b" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (2,'env','dbms_lab','dbms_lab','dbms_lab','unix','unix','me');
INSERT INTO "memory_b" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (3,'me','python','cns','atc','cns_lab','cns_lab','cns_lab');
INSERT INTO "memory_b" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (4,'dbms','dbms','cns','dbms','cns','__','__');
INSERT INTO "memory_b" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (5,'apti','apti','apti','apti','atc','ic','ic');
INSERT INTO "memory_b" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (6,'me','cns','python','atc','dbms','__','__');
INSERT INTO "memory_c" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (1,'cns_lab','cns_lab','cns_lab','env','dbms_lab','dbms_lab','dbms_lab');
INSERT INTO "memory_c" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (2,'python','atc','me','python','ic','ic','ic');
INSERT INTO "memory_c" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (3,'me','cns','atc','python','python','unix','unix');
INSERT INTO "memory_c" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (4,'dbms','dbms','cns','dbms','atc','me','cns');
INSERT INTO "memory_c" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (5,'apti','apti','dbms','unix','atc','me','cns');
INSERT INTO "memory_c" ("id","period1","period2","period3","period4","period5","period6","period7") VALUES (6,'dbms','unix','atc','__','__','__','__');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (1,'ba','Mrs.Babitha');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (2,'na','Mr.Namitha');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (4,'sup','Ms.Supriya');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (5,'dsp','Mr.Duddela Sai Prashanth');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (6,'s','Mr.Suhas Adiga');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (7,'sss','Mr.Shailesh SHetty S');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (8,'mf','Dr.Musthafa');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (9,'alk','Ms.Alakananda');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (10,'js','Mr.Janardhana Swamy');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (11,'kan','Mrs.Kanmani');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (12,'mr','Ms.Mega Rani');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (15,'nr','Mr. Nagesh Rao');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (16,'vbs','Mr. Vanishree B S');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (17,'pns','Mrs. Pooja N S');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (18,'ha','Mr . Harish Acharya');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (19,'sa','Ms.  Shiji Abraham');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (33,'ic_fac','ic_fac');
INSERT INTO "Faculty" ("FAC_ID","FAC_SHORT_NAME","FAC_NAME") VALUES (36,'plk','Dr . Pushpalatha');
CREATE TRIGGER backup BEFORE DELETE ON subjects
        FOR EACH ROW
        BEGIN
        INSERT INTO subjects_backup
        VALUES (OLD.sub_id, OLD.sub_short_name, OLD.sub_name, OLD.sub_code, OLD.sub_credit, OLD.sub_type, OLD.sem);
        END;
CREATE VIEW view2 as SELECT r.*, f.fac_short_name, s.sub_short_name from sub_fac r, faculty f, subjects s WHERE r.fac_id = f.fac_id and r.sub_id = s.sub_id;
COMMIT;
