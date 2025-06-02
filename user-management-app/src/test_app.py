import pytest
from app import app, db, User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_user_registration_and_logout(client):
    # Register a new user
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpass'
    }, follow_redirects=True)
    assert b'Login' in response.data

    # Login with the new user
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'testpass'
    }, follow_redirects=True)
    assert b'Welcome, testuser' in response.data

    # Logout
    response = client.get('/logout', follow_redirects=True)
    assert b'User Management' in response.data