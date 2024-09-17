import pytest
from microblog import create_app

def test_home_page():
    """Test the home page."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        response = client.get('/', follow_redirects=True)
        assert response.status_code == 200
        assert b'Microblog' in response.data

def test_login_page():
    """Test the login page."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        response = client.get('/auth/login')
        assert response.status_code == 200
        assert b'Microblog' in response.data

def test_404_page():
    """Test a non-existent page."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        response = client.get('/nonexistent')
        assert response.status_code =
