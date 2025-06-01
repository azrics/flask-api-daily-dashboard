from scripts.data_fetcher import fetch_data
import sqlite3
import pytest

def test_data_fetcher(tmp_path):
    # Use pytest's tmp_path for DB
    test_db = tmp_path / "test.db"
    conn = sqlite3.connect(test_db)
    conn.execute('CREATE TABLE weather (timestamp TEXT, data TEXT)')
    conn.close()
    
    # Mock API call (replace with your actual test logic)
    fetch_data(db_path=test_db)
    
    conn = sqlite3.connect(test_db)
    data = conn.execute('SELECT * FROM weather').fetchall()
    conn.close()
    
    assert len(data) > 0  # Verify data was inserted