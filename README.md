# Chat Application

This is a simple chat application built using Flask, Flask-SocketIO, and Socket.IO for real-time communication between users. Users can join different chat rooms, send messages, and leave the rooms. This README will help you understand how to set up, run, and use the application.

## Features

- **Real-Time Communication**: Chat messages are transmitted in real-time between users in the same room.
- **Room-Based Chat**: Users can create or join specific rooms by providing a room name.

## Prerequisites

To run this project, ensure you have the following installed:

- Python 3.7+
- Pip

You also need to install the necessary Python packages. The required packages are listed in the `requirements.txt` file.

## Installation

1. Clone this repository to your local machine:
   ```sh
   git clone <repository_url>
   cd chat_application
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration

The application uses Flask's secret key to maintain sessions. You can update the secret key in `app.py`:

```python
app.config["SECRET_KEY"] = "your_secret_key_here"
```

Ensure you also have CORS enabled for Flask and SocketIO to avoid cross-origin issues:

```python
from flask_cors import CORS
CORS(app, resources={r"/*": {"origins": "*"}})

socketIO = SocketIO(app, manage_session=False, cors_allowed_origins="*")
```

## Running the Application

1. Start the Flask server by running `run.py`:
   ```sh
   python run.py
   ```

2. By default, the application will be accessible at `http://127.0.0.1:5000/`.

3. Open your browser and navigate to the application.

## Usage

- Enter a username and a room name to join a chat.
- You will be taken to the chatroom where you can send and receive messages.
- Messages are displayed in a list format, showing the username and the message.
- Click on the "Leave chat room" button to exit the chatroom.

## Folder Structure

- **app.py**: Contains the main Flask application setup.
- **routes.py**: Handles routes and SocketIO events.
- **run.py**: The entry point for starting the Flask server.
- **templates/**: Contains the HTML files for the application (`base.html`, `index.html`, `chatroom.html`).
- **static/**: Holds any static files such as CSS or JavaScript if needed.

## Important Files

- **`base.html`**: The base HTML template, containing the basic layout shared across all pages.
- **`index.html`**: The homepage where users enter their username and room name.
- **`chatroom.html`**: The chatroom interface where users can see and send messages.

## Troubleshooting

- **Cross-Origin Read Blocking (CORB)**: If you see CORB errors in the console, ensure CORS is enabled properly in both the Flask and SocketIO configurations.
- **Messages Not Appearing**: Check the browser console for any JavaScript errors, and ensure the SocketIO client is connecting successfully to the server.

