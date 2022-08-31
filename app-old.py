from flask import Flask, render_template, request, session
import sqlite3
import chatterbot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = 'fgh456fdgdscv34sdv456nsd'
app.config['SESSION_TYPE'] = 'filesystem'

# delete old trained file
if os.path.exists("db.sqlite3"):
  os.remove("db.sqlite3")
  print('Old DB deleted.')

chatbot = chatterbot.ChatBot(
    'Chatty',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I don\'t understand. I am still learning.',
            'maximum_similarity_threshold': 0.5,
        }
    ],
)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('./training/hospital.yml')

@app.route('/')
def home():
    if session.get('logged_in') == True:
        user = session.get('name')
        return render_template("bot.html", userName=user)
    else:
        return render_template("login.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/verify')
def verifyLogin():
    name = ''
    email = request.args.get('email')
    password = request.args.get('pass')
    if email == '' or password == '':
        return 'fail'

    with sqlite3.connect('userDB.db') as db:
        cur = db.cursor()
        cur.execute("SELECT * FROM user WHERE email=? AND password=?",
                    (email, password))
        row = cur.fetchone()
        print(row)
        db.commit()
        if row == None:
            return 'fail'
        else:
            name = row[1]
            session['name'] = name
            session['logged_in'] = True
    return 'success'


@app.route('/register')
def register():
    name = request.args.get('name')
    email = request.args.get('email')
    password = request.args.get('pass')
    if name == '' or email == '' or password == '':
        return 'fail'

    with sqlite3.connect('userDB.db') as db:
        cur = db.cursor()
        cur.execute("INSERT INTO user (name,email,password) VALUES (?,?,?)",
                    (name, email, password))
        db.commit()

    session['name'] = name
    session['logged_in'] = True
    return 'success'

@app.route('/logout')
def logout():
    session.pop('name')
    session.pop('logged_in')
    return 'success'

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    resp = str(chatbot.get_response(userText))
    return resp


if __name__ == "__main__":
    app.run()