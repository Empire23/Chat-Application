# Advanced Web-Based Chat Application

A real-time chat application built with Flask and SocketIO, featuring user authentication, multiple chat rooms, message history, and multimedia sharing.

## Features

- **User Authentication**: Register and login with secure password hashing. Passwords can be auto-generated during registration.
- **Multiple Chat Rooms**: Join existing rooms or create new ones dynamically.
- **Real-Time Messaging**: Instant message delivery using WebSockets via SocketIO.
- **Message History**: Persistent storage of messages in SQLite database, with history loading on room join.
- **Multimedia Sharing**: Upload and share files (images, videos, documents) in chat.
- **Responsive UI**: Bootstrap-based interface that works on desktop and mobile.
- **Emojis Support**: Send emojis in messages (via text input).
- **Notifications**: Real-time notifications for users joining/leaving rooms.
- **Security**: Session-based authentication and file upload restrictions.

## Technologies Used

- **Backend**: Flask, Flask-SocketIO, Flask-Login, Flask-SQLAlchemy
- **Database**: SQLite
- **Frontend**: HTML, CSS (Bootstrap), JavaScript, Socket.IO client
- **Real-Time Communication**: SocketIO with eventlet
- **Password Security**: Werkzeug for hashing

## Installation

1. **Clone the repository** (if applicable) or ensure all files are in the project directory.

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the app**:
   Open your browser and go to `http://localhost:5000`

## Usage

1. **Register**: Create a new account. Leave the password field blank for an auto-generated password.
2. **Login**: Use your username and password to log in.
3. **Chat**:
   - Select a room from the sidebar or create a new one.
   - Type messages and press Send.
   - Upload files using the attachment button (📎).
   - Messages are sent in real-time to all users in the room.
4. **Logout**: Click the Logout button to end your session.

## Project Structure

```
chat-application/
├── app.py                 # Main Flask application
├── models.py              # Database models (User, Message)
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   └── chat.html
├── static/                # CSS and JS files
│   ├── style.css
│   └── script.js
├── uploads/               # Uploaded files directory (created automatically)
└── chat.db               # SQLite database (created automatically)
```

## API Endpoints

- `GET /`: Redirect to login
- `GET/POST /register`: User registration
- `GET/POST /login`: User login
- `GET /logout`: User logout
- `GET /chat`: Main chat interface (requires login)
- `POST /upload`: File upload endpoint
- `GET /uploads/<filename>`: Serve uploaded files

## SocketIO Events

- `join`: Join a room
- `leave`: Leave a room
- `message`: Send a message
- `load_history`: Load message history for a room

## Security Notes

- Passwords are hashed using Werkzeug's security functions.
- File uploads are limited to 16MB and stored in the `uploads/` directory.
- Session management via Flask-Login.
- For production, consider using HTTPS and a more robust database like PostgreSQL.

## Contributing

Feel free to fork the repository and submit pull requests for improvements.

## License

This project is open-source and available under the MIT License.
