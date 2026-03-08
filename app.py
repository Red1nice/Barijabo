from flask import Flask,render_template
from flask_socketio import SocketIO
from database import db
import config

from routes.auth_routes import auth
from routes.ticket_routes import tickets
from routes.chat_routes import chat
from routes.admin_routes import admin
from routes.search_routes import search
from routes.notification_routes import notify

app=Flask(__name__)

app.config.from_object(config)

db.init_app(app)

socketio=SocketIO(app)

app.register_blueprint(auth)
app.register_blueprint(tickets)
app.register_blueprint(chat)
app.register_blueprint(admin)
app.register_blueprint(search)
app.register_blueprint(notify)

@app.route("/")

def home():

    return render_template("index.html")

if __name__=="__main__":

    socketio.run(app,debug=True)
