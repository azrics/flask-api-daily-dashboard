# User Management Application

This project is a user management application built using Flask. It allows users to register, log in, reset their passwords, and access a profile dashboard.

## Project Structure

```
user-management-app
├── src
│   ├── app.py                # Main application file
│   ├── templates             # HTML templates for the application
│   │   ├── index.html        # Landing page with registration and login buttons
│   │   ├── register.html     # Registration form for new users
│   │   ├── login.html        # Login form for existing users
│   │   ├── reset_password.html # Password reset form for first-time login
│   │   └── dashboard.html     # User profile dashboard after successful login
│   └── models.py             # Data models for user management
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Features

- User registration with username, email, and password.
- User login with username and password.
- Password reset functionality for first-time login.
- User profile dashboard displaying user information.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd user-management-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/app.py
   ```

4. Access the application in your web browser at `http://127.0.0.1:5000`.

## Usage Guidelines

- Navigate to the landing page to either register a new account or log in with an existing account.
- After logging in for the first time, users will be prompted to reset their password.
- Once logged in, users can access their profile dashboard.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.