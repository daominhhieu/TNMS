import sqlite3
import time

conTo = sqlite3.connect('TNMS')
Cur = conTo.cursor()
def create():
	Cur.execute('CREATE TABLE IF NOT EXSITS violation(time TEXT, fee INT, location TEXT, violated TEXT)')
	Cur.execute('CREATE TABLE IF NOT EXSITS roadfee(time TEXT, fee INT, location TEXT)')
	Cur.execute('CREATE TABLE IF NOT EXSITS track(time TEXT, location TEXT)')
def violation():
	violation = [tv, fv, lv, vv]
	Cur.execute('INSERT INTO violation(time, fee , location, violated) VALUES (?, ?, ?, ?)', (t, fv, lv, vv))
	Cur.commit()
	return violation
def roadfee():
	roadfee = [trf, frf ,lrf ]
	Cur.execute('INSERT INTO roadfee(time, fee, location)')
	Cur.commit()
	conTo.close()
	return roadfee
def track():
	track = [tt, lt]
	Cur.execute('INSERT INTO track(time, location)')
	Cur.commit()
	conTo.close()
	return track
