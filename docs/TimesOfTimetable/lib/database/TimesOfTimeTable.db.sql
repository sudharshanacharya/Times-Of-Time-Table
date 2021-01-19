BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "sub_fac" (
	"fac_id"	int NOT NULL,
	"sec"	varchar(3) NOT NULL,
	"sub_id"	int NOT NULL,
	"rem_hours"	int NOT NULL,
	CONSTRAINT "_sub_id" FOREIGN KEY("sub_id") REFERENCES "subjects"("sub_id"),
	CONSTRAINT "_fac_id" FOREIGN KEY("fac_id") REFERENCES "faculty"("fac_id")
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
CREATE TABLE IF NOT EXISTS "Faculty" (
	"FAC_ID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"FAC_SHORT_NAME"	VARCHAR(8),
	"FAC_NAME"	VARCHAR(25)
);
INSERT INTO "sub_fac" VALUES (4,'A',4,5);
INSERT INTO "sub_fac" VALUES (3,'A',3,5);
INSERT INTO "sub_fac" VALUES (12,'A',6,4);
INSERT INTO "sub_fac" VALUES (1,'A',1,4);
INSERT INTO "sub_fac" VALUES (7,'A',12,2);
INSERT INTO "sub_fac" VALUES (2,'A',2,4);
INSERT INTO "sub_fac" VALUES (9,'B',5,4);
INSERT INTO "sub_fac" VALUES (11,'C',6,4);
INSERT INTO "sub_fac" VALUES (6,'A',7,1);
INSERT INTO "sub_fac" VALUES (7,'B',1,4);
INSERT INTO "sub_fac" VALUES (11,'B',2,4);
INSERT INTO "sub_fac" VALUES (8,'B',4,5);
INSERT INTO "sub_fac" VALUES (10,'B',6,4);
INSERT INTO "sub_fac" VALUES (11,'B',8,3);
INSERT INTO "sub_fac" VALUES (9,'B',10,3);
INSERT INTO "sub_fac" VALUES (5,'A',5,4);
INSERT INTO "sub_fac" VALUES (1,'A',10,3);
INSERT INTO "sub_fac" VALUES (2,'A',8,3);
INSERT INTO "sub_fac" VALUES (14,'A',11,3);
INSERT INTO "sub_fac" VALUES (6,'B',7,1);
INSERT INTO "sub_fac" VALUES (14,'B',11,3);
INSERT INTO "sub_fac" VALUES (15,'B',12,2);
INSERT INTO "sub_fac" VALUES (3,'B',3,5);
INSERT INTO "sub_fac" VALUES (16,'C',2,4);
INSERT INTO "sub_fac" VALUES (17,'C',3,5);
INSERT INTO "sub_fac" VALUES (8,'C',4,5);
INSERT INTO "sub_fac" VALUES (6,'C',6,4);
INSERT INTO "sub_fac" VALUES (17,'C',10,3);
INSERT INTO "sub_fac" VALUES (10,'C',8,3);
INSERT INTO "sub_fac" VALUES (6,'C',7,1);
INSERT INTO "sub_fac" VALUES (18,'C',5,4);
INSERT INTO "sub_fac" VALUES (14,'C',11,3);
INSERT INTO "sub_fac" VALUES (15,'C',12,2);
INSERT INTO "subjects" VALUES (1,'me','Management ','18cs51',3,'theory',5);
INSERT INTO "subjects" VALUES (2,'cns','Computer Networks & Security','18cs52',3,'theory',5);
INSERT INTO "subjects" VALUES (3,'dbms','Data Base Management System','15cs53',4,'major',5);
INSERT INTO "subjects" VALUES (4,'atc','Automata Theory & Conputability','18cs54',4,'major',5);
INSERT INTO "subjects" VALUES (5,'python','Application Development Using Python','18cs55',4,'not_theory',5);
INSERT INTO "subjects" VALUES (6,'unix','Unix Programming','18cs56',3,'not_theory',5);
INSERT INTO "subjects" VALUES (7,'env','Environment','18cs55',1,'minor',5);
INSERT INTO "subjects" VALUES (8,'cns_lab','cns laboratory','18csl55',2,'lab',5);
INSERT INTO "subjects" VALUES (10,'dbms_lab','dbms_laboratory','18csl56',2,'lab',5);
INSERT INTO "subjects" VALUES (11,'ic','ic','18csl57',0,'lab',5);
INSERT INTO "subjects" VALUES (12,'apti','aptitude','18cs78',1,'spl',5);
INSERT INTO "Faculty" VALUES (1,'BA','Mrs.Babitha');
INSERT INTO "Faculty" VALUES (2,'NA','Mr.Namitha');
INSERT INTO "Faculty" VALUES (3,'PLK','Dr.Pushpalatha');
INSERT INTO "Faculty" VALUES (4,'SUP','Ms.Supriya');
INSERT INTO "Faculty" VALUES (5,'DSP','Mr.Duddela Sai Prashanth');
INSERT INTO "Faculty" VALUES (6,'SA','Mr.Suhas Adiga');
INSERT INTO "Faculty" VALUES (7,'SSS','Mr.Shailesh SHetty S');
INSERT INTO "Faculty" VALUES (8,'MF','Dr.Musthafa');
INSERT INTO "Faculty" VALUES (9,'ALK','Ms.Alakananda');
INSERT INTO "Faculty" VALUES (10,'JS','Mr.Janardhana Swamy');
INSERT INTO "Faculty" VALUES (11,'KAN','Mrs.Kanmani');
INSERT INTO "Faculty" VALUES (12,'MR','Ms.Mega Rani');
INSERT INTO "Faculty" VALUES (14,'ic_fac','ic_fac');
INSERT INTO "Faculty" VALUES (15,'NR','Mr. Nagesh Rao');
INSERT INTO "Faculty" VALUES (16,'VBS','Mr. Vanishree B S');
INSERT INTO "Faculty" VALUES (17,'PNS','Mrs. Pooja N S');
INSERT INTO "Faculty" VALUES (18,'HA','Mr . Harish Acharya');
INSERT INTO "Faculty" VALUES (19,'SA','Ms.  Shiji Abraham');
CREATE VIEW view2 as SELECT r.*, f.fac_short_name, s.sub_short_name from sub_fac r, faculty f, subjects s WHERE r.fac_id = f.fac_id and r.sub_id = s.sub_id;
COMMIT;
