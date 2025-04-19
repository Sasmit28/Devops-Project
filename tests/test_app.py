import pytest
from app import app, db, Todo

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_create_todo(client):
    response = client.post('/api/todos', json={
        'title': 'Test Todo',
        'description': 'This is a test.'
    })
    assert response.status_code == 201
    assert response.get_json()['title'] == 'Test Todo'

def test_get_all_todos(client):
    client.post('/api/todos', json={'title': 'Sample'})
    response = client.get('/api/todos')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_single_todo(client):
    post_resp = client.post('/api/todos', json={'title': 'Read book'})
    todo_id = post_resp.get_json()['id']
    response = client.get(f'/api/todos/{todo_id}')
    assert response.status_code == 200
    assert response.get_json()['title'] == 'Read book'

def test_update_todo(client):
    post_resp = client.post('/api/todos', json={'title': 'Old Title'})
    todo_id = post_resp.get_json()['id']
    response = client.put(f'/api/todos/{todo_id}', json={'title': 'New Title'})
    assert response.status_code == 200
    assert response.get_json()['title'] == 'New Title'

def test_delete_todo(client):
    post_resp = client.post('/api/todos', json={'title': 'To Delete'})
    todo_id = post_resp.get_json()['id']
    response = client.delete(f'/api/todos/{todo_id}')
    assert response.status_code == 204
