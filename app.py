from flask import Flask
from flask_session import Session
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config["SECRET_KEY"] = "JonJamLil24!"
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

socketIO = SocketIO(app, manage_session=False, cors_allowed_origins="*")

