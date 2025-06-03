> **Note:** Please fork this repository before making any changes. Do not commit directly to the original NexVerse Freebie Pack repository.

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

- User registration, login, logout
- Profile update and password reset
- Account deletion
- Beautiful, responsive UI
- Pytest-based testing with clear console output
- GitHub Actions CI/CD pipeline
- Easy database backup script

## Setup Instructions

1. Fork the repository to your own GitHub account using the "Fork" button at the top right of the repo page.

2. Clone your forked repository:
   ```
   git clone https://github.com/<your-username>/user-management-app.git
   cd user-management-app
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python src/app.py
   ```

5. Access the application in your web browser at `http://127.0.0.1:5000`.

## Usage Guidelines

- Navigate to the landing page to either register a new account or log in with an existing account.
- After logging in for the first time, users will be prompted to reset their password.
- Once logged in, users can access their profile dashboard.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

---

## Changelog

### v1.0.0 (2024-06-03)
- Initial release as part of NexVerse Freebie Pack
- User registration, login, logout
- Profile update and password reset
- Account deletion feature
- Beautiful, responsive UI
- Pytest-based testing with clear console output
- GitHub Actions CI/CD pipeline
- Easy database backup script

---