import socket
import select
import time
from flask import Flask
from flask import render_template
from flask import Flask, redirect, url_for
from flask import request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

usser = []
msg = []

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class chat1(db.Model):
    name = db.Column(db.Text, primary_key=True, nullable=False, unique=True)
    message = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'name:{}, message:{}, time:{}'.format(
            self.name,
            self.message,
            self.time
        )


class user(db.Model):
    username = db.Column(db.Text, primary_key=True,
                         nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)


def getTime():
    t = time.localtime()
    timee = time.strftime("%m/%d/%Y, %H:%M:%S", t)
    return timee


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/up')
def homeoo():
    return render_template('signup.html')


@app.route('/room', methods=['GET', 'POST'])
def homeroo():
    global msg
    wsl = request.environ.get("wsgi.websocket")
    if wsl:
        print(wsl)
    if request.method == 'POST':
        i = request.form['inputm']
        ctime = str(getTime())
        row = {'msg': i, 'time': ctime}
        msg.append(row)
        _msg = msg.copy()
        _msg.reverse()
        return render_template('chatroom.html', msg=_msg)
    else:
        return render_template('chatroom.html', msg=msg)


@app.route('/log', methods=['POST'])
def homeottto():
    u = request.form['Username']
    p = request.form['Password']

    return render_template('chatroom.html', userName=u)


@app.route('/sign', methods=['POST'])
def homeotttoo():
    n = request.form['Name']
    w = request.form['pwd']

    ch1 = user(username=n, password=w)
    db.session.add(ch1)
    db.session.commit()
    return redirect('/')


@app.route('/demo')
def demo_url_for():
    return redirect(url_for('signup.html'))


if __name__ == '__main__':
    app.run(debug=True)
