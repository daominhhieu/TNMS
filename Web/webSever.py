from flask import Flask, render_template, request, flash, url_for, redirect
app = Flask(__name__)
import data_manager

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.errorhandler(405)
def page_not_found(e):
    return render_template("405.html")

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html")

@app.route('/signup/', methods=['GET','POST'])
def signup():
    error = None
    try:
        if request.method == "POST":
            sign_number     = request.form['sign_phone_number']
            license_plate   = request.form['license_plate']
            sign_password   = request.form['sign_password']
            retype_password = request.form['retype_password']

            if( (len(sign_number) == 10 or len(sign_number) == 11) and sign_number.isdigit() == True ):
                error = 'Vailid Phone Number'
                    
                if( len(sign_password) > 5 and sign_password == retype_password and sign_password.isdigit() == False and sign_password.isalpha() == False ):
                    error = '/n Vailid password'

                    if(len(license_plate) > 7 and len(license_plate) < 10 and license_plate.isdigit() == False and license_plate.isalpha() == False ):
                        data_manager.usr_database('usr_write', sign_number, license_plate, sign_password)
                        return redirect(url_for('info'))
                    else:
                        error = '/n Invailid License Plate'
                else:
                    error = '/n Invailid password'
            else:
                error = '/n Invailid Phone Number'

        return render_template("signup.html", error = error)

    except Exception as e:
        flash(e)
        return render_template("signup.html", error = error)

@app.route('/', methods=['GET','POST'])
def login():
    error = None
    try:
        if request.method == "POST":
            attempted_username = request.form['phone_number']
            attempted_password = request.form['password']
            
            flash(attempted_username)
            flash(attempted_password)

            if (attempted_username == "ad" and attempted_password == "123"):
                return redirect(url_for('info'))
            else:
                error = "Cannot Login!"

        return render_template("index.html", error = error)
            
            
    except Exception as e:
        flash(e)
        return render_template("index.html", error = error)


@app.route('/info/', methods=['GET','POST'])
def info():
    return 'NOTHING HERE YET!'

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()
