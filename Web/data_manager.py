import sqlite3
import time
import datetime

def user_name(user_name)
    usr = user_name + '.db'
    conn = sqlite3.connect(usr)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS violation (time, fee, location, violated)")
    cur.execute("CREATE TABLE IF NOT EXISTS violation (time, fee, location)")
    cur.execute("CREATE TABLE IF NOT EXISTS violation (time, location)")
    date_stamp = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))

    def violated_write(fv, lv, vv):
        tv = date_stamp
        cur.execute("INSERT INTO violation (time, fee, location, violated) VALUES(?,?,?,?)",
                     (tv, fv, lv, vv))
        conn.commit()
        
        
    def roadfee_write(frf, lrf):
        trf = date_stamp
        cur.execute("INSERT INTO roadfee (time, fee, location) VALUES(?,?,?)",
                     (trf, frf, lrf))
        conn.commit()


    def track_write(lt):
        tt = date_stamp
        cur.execute("INSERT INTO track (time, location) VALUES(?,?)",
                     (tt, lt))
        conn.commit()

    def violated_read():
        cur.execute("SELECT * FROM violation")
        data = cur.fetchall()

    def roadfee_read():
        cur.execute("SELECT * FROM roadfee")
        data = cur.fetchall()

    def track_read():
       cur.execute("SELECT * FROM track")
       data = cur.fetchall()


    cur.close()
    conn.close()

def user_manager():
    conn = sqlite3.connect('User_database.db')
    cur = conn.cursor()
    def user_manager():
    cur.execute("CREATE TABLE IF NOT EXISTS userData (phoneNumber REAL, VehID TEXT, password REAL)")
    
   def write():
        cur.execute("INSERT INTO userData (phoneNumber, VehID, password) VALUES(?,?,?)", (phoneNumber, VehID, password))
        conn.commit()

   def  read():
        cur.execute("SELECT * FROM userData")
        data = cur.fetchall()

    cur.close()
    conn.close()

