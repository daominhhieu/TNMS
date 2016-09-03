from flask import Flask, render_template, request, flash, url_for, redirect
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.errorhandler(405)
def page_not_found(e):
    return render_template("405.html")

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html")

@app.route('/', methods=['GET','POST'])
def login():
    error = None
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
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
    return render_template("info.html", tv=v[0], fv=v[1], lv=v[2], vv=v[3], trf=rf[0], frf=rf[1], lrf=rf[2], tt=t[0], lt=t[1])

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()
