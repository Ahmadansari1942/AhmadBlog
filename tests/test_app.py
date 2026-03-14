import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_api_articles(client):
    response = client.get('/api/articles')
    assert response.status_code == 200

def test_api_stats(client):
    response = client.get('/api/stats')
    assert response.status_code == 200

def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200

def test_contact_page(client):
    response = client.get('/contact')
    assert response.status_code == 200

def test_admin_page(client):
    response = client.get('/admin')
    assert response.status_code == 200

def test_404_page(client):
    response = client.get('/nonexistent-page')
    assert response.status_code == 404
