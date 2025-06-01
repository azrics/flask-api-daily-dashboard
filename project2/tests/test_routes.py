def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Dashboard" in response.data

def test_weather_api_empty(client):
    response = client.get('/api/weather')
    assert response.status_code == 200
    assert response.json == {'error': 'No data'}

def test_refresh_api(client, monkeypatch):
    # Mock the data fetcher to avoid real API calls
    def mock_fetch():
        conn = sqlite3.connect(client.application.config['DATABASE'])
        conn.execute("INSERT INTO weather VALUES ('2024-01-01', '{}')")
        conn.commit()
        conn.close()
    
    monkeypatch.setattr('scripts.data_fetcher.fetch_data', mock_fetch)
    
    response = client.get('/api/refresh')
    assert response.status_code == 200
    assert response.json == {'status': 'Data updated successfully'}