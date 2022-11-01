import pytest

from flask import Flask, session
from flask.testing import FlaskClient
from member_system.repository import MemoryUnitOfWork
from member_system.routes import configureRoutes
from werkzeug.test import TestResponse

@pytest.fixture()
def app():
    app = Flask(__name__, template_folder='../../templates')
    app.test_client()

    unitOfWork = MemoryUnitOfWork()
    unitOfWork.memberRepository.addMember('test', 'test', 'test')

    configureRoutes(app, unitOfWork)
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

def assertRedirects(response: TestResponse, path: str):
    assert len(response.history) == 1
    assert response.history[0].status_code == 302
    assert response.request.path == path
    assert response.status_code == 200

def assertContains(response: TestResponse, text: str):
    assert text in response.get_data().decode('utf-8')
    assert response.status_code == 200

def setSession(client: FlaskClient):
    with client.session_transaction() as session:
        session['id'] = 1
        session['name'] = 'test'
        session['username'] = 'test'

def testError(client: FlaskClient):
    messages = [
        '請輸入帳號、密碼', 
        '帳號、或密碼輸入錯誤'
    ]
    for message in messages:
        response = client.get(
            path='/error',
            query_string={ 'message': message }
        )
        assertContains(response, message)

def testHome(client: FlaskClient):
    response = client.get('/')
    assertContains(response, '歡迎光臨，請輸入帳號密碼')

def testMemberIfLogin(client: FlaskClient):
    setSession(client)
    response = client.get('/member')
    assertContains(response, '歡迎光臨，這是會員頁')
    assertContains(response, '很高興見到您，')
    assertContains(response, 'test')

def testRedirectsHomeToMemberIfLogin(client: FlaskClient):
    setSession(client)
    response = client.get(
        path='/', 
        follow_redirects=True
    )
    assertRedirects(response, '/member')

def testRedirectsMemberToHomeIfNotLogin(client: FlaskClient):
    response = client.get(
        path='/member', 
        follow_redirects=True
    )
    assertRedirects(response, '/')

def testSigninSuccess(client: FlaskClient):
    response = client.post(
        path='/signin',
        data={ 
            'username': 'test',
            'password': 'test'
        },
        follow_redirects=True
    )
    assertRedirects(response, '/member')

def testSigninWithoutUsernameOrPassword(client: FlaskClient):
    response = client.post(
        path='/signin',
        data={ 
            'username': '',
            'password': ''
        },
        follow_redirects=True
    )
    assertRedirects(response, '/error')
    assertContains(response, '請輸入帳號、密碼')

def testSigninForPasswordMismatchError(client: FlaskClient):
    response = client.post(
        path='/signin',
        data={ 
            'username': '123',
            'password': '123'
        },
        follow_redirects=True
    )
    assertRedirects(response, '/error')
    assertContains(response, '帳號、或密碼輸入錯誤')

def testSignout(client: FlaskClient):
    setSession(client)
    with client:
        response = client.get(
            path='/signout',
            follow_redirects=True
        )
        assert session.get('id', None) == None
        assert session.get('name', None) == None
        assert session.get('username', None) == None
    assertRedirects(response, '/')

def testSignupSuccess(client: FlaskClient):
    response = client.post(
        path='/signup',
        data={ 
            'name': 'signup',
            'username': 'signup',
            'password': 'signup'
        },
        follow_redirects=True
    )
    assertRedirects(response, '/')

def testSignupForUsernameExistsError(client: FlaskClient):
    response = client.post(
        path='/signup',
        data={ 
            'name': 'test',
            'username': 'test',
            'password': 'test'
        },
        follow_redirects=True
    )
    assertRedirects(response, '/error')
    assertContains(response, '帳號已經被註冊')

def testMessage(client: FlaskClient):
    setSession(client)
    response = client.post(
        path='/message',
        data={ 
            'content': '123456',
        },
        follow_redirects=True
    )
    assertRedirects(response, '/member')
    assertContains(response, 'test: 123456')