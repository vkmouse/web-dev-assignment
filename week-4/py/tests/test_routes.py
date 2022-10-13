import pytest
from flask import Flask
from flask.testing import FlaskClient
from functions import *
from werkzeug.test import TestResponse

@pytest.fixture()
def app():
    app = Flask(__name__, template_folder='../templates')
    app.test_client()
    configureRoutes(app)
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

def cookieContains(client: FlaskClient, name: str, value: str) -> bool:
    for i in client.cookie_jar:
        if i.name == name and i.value == value:
            return True
    else:
        return False

def assertRedirects(response: TestResponse, path: str):
    assert len(response.history) == 1
    assert response.history[0].status_code == 302
    assert response.request.path == path
    assert response.status_code == 200

def assertContains(response: TestResponse, text: str):
    assert text in response.get_data().decode('utf-8')
    assert response.status_code == 200

def setSession(client: FlaskClient, property: str, value: any):
    client.set_cookie(
        server_name='/',
        key=property,
        value=str(value).lower())

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
    setSession(client, 'isLogin', True)
    response = client.get('/member', follow_redirects=True)
    print(response.get_data().decode('utf-8'))
    assertContains(response, '歡迎光臨，這是會員頁')

def testRedirectsHomeToMemberIfLogin(client: FlaskClient):
    setSession(client, 'isLogin', True)
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
            'account': 'test',
            'password': 'test'
        },
        follow_redirects=True
    )
    assertRedirects(response, '/member')

def testSigninWithoutAccountOrPassword(client: FlaskClient):
    response = client.post(
        path='/signin',
        data={ 
            'account': '',
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
            'account': '123',
            'password': '123'
        },
        follow_redirects=True
    )
    assertRedirects(response, '/error')
    assertContains(response, '帳號、或密碼輸入錯誤')

def testSignout(client: FlaskClient):
    setSession(client, 'isLogin', True)
    assert cookieContains(client, 'isLogin', 'true')
    response = client.get(
        path='/signout',
        follow_redirects=False,
    )
    assert response.headers['Set-Cookie'].find('isLogin=;') != -1
    client.delete_cookie(
        server_name='/',
        key='isLogin')
    response = client.get(
        path=response.headers['Location'],
        follow_redirects=True,
        headers={'Cookie':response.headers['Set-Cookie']}
    )
    assert response.request.path == '/'

def testSquare(client: FlaskClient):
    response = client.get(
        path='/square/4'
    )
    assertContains(response, '16')