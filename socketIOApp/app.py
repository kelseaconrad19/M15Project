# from web_socket_server import WebSocketServer, socketio, app
# from flask import render_template
# import json
#
# my_app = WebSocketServer().create_app()
# message_storage = {}
# users = {}
#
# @socketio.on('message')
# def handle_message(data):
#     try:
#         data = json.loads(data)
#         username = data['username']
#         message = data['message']
#
#         if username not in message_storage:
#             message_storage[username] = []
#         message_storage[username].append(message)
#         print(f'received message from {username}: ' + message)
#         socketio.emit('message', {'user': username, 'message': message})
#     except json.JSONDecodeError as e:
#         print(f'Error decoding JSON: {e}')
#     except KeyError as e:
#         print(f'Missing key in data: {e}')
#
# @socketio.on('get_user_messages')
# def handle_get_user_messages(data):
#     try:
#         data = json.loads(data)
#         username = data['username']
#
#         if username in message_storage:
#             user_messages = message_storage[username]
#         else:
#             user_messages = []
#         print(f'received get_user_messages request from {username}')
#         socketio.emit('get_user_messages', {'user': username, 'messages': user_messages})
#     except json.JSONDecodeError as e:
#         print(f'Error decoding JSON: {e}')
#     except KeyError as e:
#         print(f'Missing key in data: {e}')
#
# @socketio.on('connect')
# def handle_connect():
#     print('connected')
#
# @socketio.on('disconnect')
# def handle_disconnect():
#     print('disconnected')
#
# @app.route('/')
# def index():
#     return render_template('base.html')
#
# if __name__ == '__main__':
#     socketio.run(my_app, allow_unsafe_werkzeug=True)