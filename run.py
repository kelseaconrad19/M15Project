from app import app, socketIO
import routes

if __name__ == "__main__":
    socketIO.run(app, debug=True, allow_unsafe_werkzeug=True)