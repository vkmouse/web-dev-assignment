import pytest
import json

from flask import Flask
from flask.testing import FlaskClient
from member_system.repository import MemoryUnitOfWork
from member_system.routes import configureAPIRoutes

@pytest.fixture()
def app():
    app = Flask(__name__, template_folder='../../templates')
    app.test_client()

    unitOfWork = MemoryUnitOfWork()
    unitOfWork.memberRepository.addMember('test', 'test', 'test')

    configureAPIRoutes(app, unitOfWork)
    app.config.update({
        'TESTING': True,
        'SECRET_KEY': 'test'
    })

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def setSession(client: FlaskClient):
    with client.session_transaction() as session:
        session['id'] = 1
        session['name'] = 'test'
        session['username'] = 'test'

def testMemberQuerySuccess(client: FlaskClient):
    setSession(client)
    response = client.get(
        path='/api/member',
        query_string={ 'username': 'test' }
    )
    assert response.get_json()['data'] == {
        'id': 1,
        'name': 'test',
        'username': 'test'
    }

def testMemberQueryWithoutLogin(client: FlaskClient):
    response = client.get(
        path='/api/member',
        query_string={'username': 'test'})
    assert response.get_json()['data'] == None

def testMemberQueryFailed(client: FlaskClient):
    setSession(client)
    response = client.get(
        path='/api/member',
        query_string={'username': '123'})
    assert response.get_json()['data'] == None

def testModifyMemberNameSuccess(client: FlaskClient):
    setSession(client)
    response = client.patch(
        path='/api/member',
        data=json.dumps({ 'name': 'test123' }),
        content_type='application/json')
    assert response.get_json()['ok'] == True
