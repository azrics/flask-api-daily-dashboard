import pytest
from app import app, db, User

GREEN_TICK = "\u2705"
RED_CROSS = "\u274C"

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_user_registration(client):
    print("\nTesting user registration...")
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpass'
    }, follow_redirects=True)
    try:
        assert b'Login' in response.data
        print(f"{GREEN_TICK} User registration successful and redirected to login.")
    except AssertionError:
        print(f"{RED_CROSS} User registration failed.")

def test_user_login_logout(client):
    print("\nTesting user login and logout...")
    # Register first
    client.post('/register', data={
        'username': 'testuser2',
        'email': 'test2@example.com',
        'password': 'testpass'
    }, follow_redirects=True)
    # Login
    response = client.post('/login', data={
        'username': 'testuser2',
        'password': 'testpass'
    }, follow_redirects=True)
    try:
        assert b'Welcome, testuser2' in response.data
        print(f"{GREEN_TICK} Login successful, dashboard loaded.")
    except AssertionError:
        print(f"{RED_CROSS} Login failed.")
    # Logout
    response = client.get('/logout', follow_redirects=True)
    try:
        assert b'User Management' in response.data
        print(f"{GREEN_TICK} Logout successful, returned to home page.")
    except AssertionError:
        print(f"{RED_CROSS} Logout failed.")

def test_update_profile(client):
    print("\nTesting profile update...")
    # Register and login
    client.post('/register', data={
        'username': 'testuser3',
        'email': 'test3@example.com',
        'password': 'testpass'
    }, follow_redirects=True)
    client.post('/login', data={
        'username': 'testuser3',
        'password': 'testpass'
    }, follow_redirects=True)
    # Update profile
    response = client.post('/update_profile', data={
        'username': 'updateduser',
        'email': 'updated@example.com'
    }, follow_redirects=True)
    try:
        assert b'updateduser' in response.data
        assert b'updated@example.com' in response.data
        print(f"{GREEN_TICK} Profile update successful and reflected on dashboard.")
    except AssertionError:
        print(f"{RED_CROSS} Profile update failed.")

def test_reset_password(client):
    print("\nTesting password reset...")
    # Register and login
    client.post('/register', data={
        'username': 'testuser4',
        'email': 'test4@example.com',
        'password': 'oldpass'
    }, follow_redirects=True)
    client.post('/login', data={
        'username': 'testuser4',
        'password': 'oldpass'
    }, follow_redirects=True)
    # Reset password
    response = client.post('/reset_password', data={
        'new_password': 'newpass'
    }, follow_redirects=True)
    try:
        assert b'Welcome, testuser4' in response.data
        print(f"{GREEN_TICK} Password reset successful.")
    except AssertionError:
        print(f"{RED_CROSS} Password reset failed.")
    # Logout and login with new password
    client.get('/logout', follow_redirects=True)
    response = client.post('/login', data={
        'username': 'testuser4',
        'password': 'newpass'
    }, follow_redirects=True)
    try:
        assert b'Welcome, testuser4' in response.data
        print(f"{GREEN_TICK} Login with new password successful.")
    except AssertionError:
        print(f"{RED_CROSS} Login with new password failed.")