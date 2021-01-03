import sqlite3
connection = sqlite3.connect("database/TimesOfTimeTable.db")
crsr = connection.cursor()
sql_command = """CREATE TABLE Faculty ( FAC_ID INTEGER PRIMARY KEY AUTOINCREMENT,FAC_SHORT_NAME VARCHAR(8),FAC_NAME VARCHAR(25));"""
crsr.execute(sql_command)
sql_command = """INSERT INTO Faculty (FAC_SHORT_NAME, FAC_NAME) VALUES ("BA","Mrs.Babitha");"""
crsr.execute(sql_command)
sql_command = """INSERT INTO Faculty (FAC_SHORT_NAME, FAC_NAME) VALUES ("NA","Mr.Namitha");"""
crsr.execute(sql_command)
sql_command = """INSERT INTO Faculty (FAC_SHORT_NAME, FAC_NAME) VALUES ("PLK","Dr.Pushpalatha");"""
crsr.execute(sql_command)
sql_command = """INSERT INTO Faculty (FAC_SHORT_NAME, FAC_NAME) VALUES ("SUP","Ms.Supriya");"""
crsr.execute(sql_command)
sql_command = """INSERT INTO Faculty (FAC_SHORT_NAME, FAC_NAME) VALUES ("DSP","Mr.Duddela Sai Prashanth");"""
crsr.execute(sql_command)
sql_command = """INSERT INTO Faculty (FAC_SHORT_NAME, FAC_NAME) VALUES ("SA","Mr.Suhas Adiga");"""
crsr.execute(sql_command)
sql_command = """INSERT INTO Faculty (FAC_SHORT_NAME, FAC_NAME) VALUES ("SSS","Mr.Shailesh SHetty S");"""
crsr.execute(sql_command)
sql_command = """INSERT INTO Faculty (FAC_SHORT_NAME, FAC_NAME) VALUES ("MF","Dr.Musthafa");"""
crsr.execute(sql_command)
sql_command = """INSERT INTO Faculty (FAC_SHORT_NAME, FAC_NAME) VALUES ("ALK","Ms.Alakananda");"""
crsr.execute(sql_command)
sql_command = """INSERT INTO Faculty (FAC_SHORT_NAME, FAC_NAME)VALUES ("JS","Mr.Janardhana Swamy");"""
crsr.execute(sql_command)
sql_command = """INSERT INTO Faculty (FAC_SHORT_NAME, FAC_NAME) VALUES ("KAN","Mrs.Kanmani");"""
crsr.execute(sql_command)
connection.commit()






