import sqlite3
import time
import datetime

def usr_data(phoneNumber, request, fee, location, violated):
    vw, vr, rfw, rfr, tw, tr = usr_ID(phoneNumber)
    if request == 'violation_wrtie':
        vw(fee, location, violated)
        print 'violation_data stored'
    elif request == 'violation_read':
        print 'violation_data loaded'
        return vr()

    elif request == 'roadfee_wrtie':
        rfw(fee, location)
        print 'raodfee_data stored'
    elif request == 'roadfee_read':
        print 'roadfee_data loaded'
        return rfr()

    elif request == 'track_wrtie':
        tw(location)
        print 'track_data stored'
    elif request == 'track_read':
        print 'track_data loaded'
        return tr()

    else:
        print 'Invailid request'

def usr_ID(phoneNumber):
    usr = phoneNumber + '.db'
    conn = sqlite3.connect(usr)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS violation (time, fee, location, violated)")
    cur.execute("CREATE TABLE IF NOT EXISTS roadfee (time, fee, location)")
    cur.execute("CREATE TABLE IF NOT EXISTS track (time, location)")
    date_stamp = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))

    def violated_write(fv, lv, vv):
        tv = date_stamp
        cur.execute("INSERT INTO violation (time, fee, location, violated) VALUES(?,?,?,?)",
                     (tv, fv, lv, vv))
        conn.commit()
        cur.close()
        conn.close()
        
        
    def roadfee_write(frf, lrf):
        trf = date_stamp
        cur.execute("INSERT INTO roadfee (time, fee, location) VALUES(?,?,?)",
                     (trf, frf, lrf))
        conn.commit()
        cur.close()
        conn.close()


    def track_write(lt):
        tt = date_stamp
        cur.execute("INSERT INTO track (time, location) VALUES(?,?)",
                     (tt, lt))
        conn.commit()
        cur.close()
        conn.close()

    def violated_read():
        cur.execute("SELECT * FROM violation")
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data

    def roadfee_read():
        cur.execute("SELECT * FROM roadfee")
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data

    def track_read():
       cur.execute("SELECT * FROM track")
       data = cur.fetchall()
       cur.close()
       conn.close()
       return data

    return violated_write, violated_read, roadfee_write, roadfee_read, track_write, track_read

def usr_database(request, phoneNumber, licensePlate, password):
    w, r = user_manager()
    if request == 'write':
        w(phoneNumber, licensePlate, password)
        print 'new_usr_info stored'
    elif request == 'read':
        print 'usr_info loaded'
        return r()

    else:
        print 'Invailid request'

def user_manager():
    conn = sqlite3.connect('User_database.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS userData (phoneNumber , licensePlate, password)")
    
    def write(phoneNumber, licensePlate, password):
        cur.execute("INSERT INTO userData (phoneNumber, licensePlate, password) VALUES(?,?,?)", (phoneNumber, licensePlate, password))
        conn.commit()
        cur.close()
        conn.close()

    def  read():
        cur.execute("SELECT * FROM userData")
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    
    return write, read
