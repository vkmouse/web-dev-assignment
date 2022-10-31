import pytest
from flask import Flask
from flask.testing import FlaskClient
import json
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
    obj = json.loads(response.get_data().decode('utf-8'))
    assert obj['data']['id'] == 1
    assert obj['data']['name'] == 'test'
    assert obj['data']['username'] == 'test'

def testMemberQueryWithoutLogin(client: FlaskClient):
    response = client.get(
        path='/api/member',
        query_string={ 'username': 'test' }
    )
    obj = json.loads(response.get_data().decode('utf-8'))
    assert obj['data'] == None

def testMemberQueryFailed(client: FlaskClient):
    setSession(client)
    response = client.get(
        path='/api/member',
        query_string={ 'username': '123' }
    )
    obj = json.loads(response.get_data().decode('utf-8'))
    assert obj['data'] == None