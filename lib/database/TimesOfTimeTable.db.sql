BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Faculty" (
	"FAC_ID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"FAC_SHORT_NAME"	VARCHAR(8),
	"FAC_NAME"	VARCHAR(25)
);
CREATE TABLE IF NOT EXISTS "subjects" (
	"sub_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"sub_short_name"	varchar(8) NOT NULL,
	"sub_name"	varchar(20) NOT NULL,
	"sub_code"	varchar(10) NOT NULL,
	"sub_credit"	int NOT NULL,
	"sub_type"	varchar(10) NOT NULL
);
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
INSERT INTO "subjects" VALUES (1,'me','Management ','18cs51',3,'T');
INSERT INTO "subjects" VALUES (2,'cns','Computer Networks & Security','18cs52',3,'T');
INSERT INTO "subjects" VALUES (3,'dbms','Data Base Management System','15cs53',4,'M');
INSERT INTO "subjects" VALUES (4,'atc','Automata Theory & Conputability','18cs54',4,'M');
INSERT INTO "subjects" VALUES (5,'python','Application Development Using Python','18cs55',4,'NT');
INSERT INTO "subjects" VALUES (6,'unix','Unix Programming','18cs56',3,'NT');
COMMIT;
