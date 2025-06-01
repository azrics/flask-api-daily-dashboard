import pytest
from app import app as flask_app
import sqlite3
import os

@pytest.fixture
def app():
    # Use test DB
    test_db = 'test_data.db'
    flask_app.config['TESTING'] = True
    flask_app.config['DATABASE'] = test_db
    
    # Setup test DB
    conn = sqlite3.connect(test_db)
    conn.execute('CREATE TABLE IF NOT EXISTS weather (timestamp TEXT, data TEXT)')
    conn.commit()
    conn.close()
    
    yield flask_app
    
    # Teardown
    os.remove(test_db)

@pytest.fixture
def client(app):
    return app.test_client()