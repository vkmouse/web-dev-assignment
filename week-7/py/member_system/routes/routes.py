import re
from flask import Flask
from flask import request
from flask import session
from flask import redirect
from flask import render_template
from flask import url_for

from member_system.core import UnitOfWork

def configureRoutes(app: Flask, unitOfWork: UnitOfWork):
    @app.route('/')
    def index():
        if session.get('name'):
            return redirect(url_for('member'))
        else:
            return render_template('index.html')

    @app.route('/member')
    def member():
        name = session.get('name')
        messages = unitOfWork.messageRepository.getMessages()
        messages = map(lambda m: f'{m.name}: {m.content}', messages)
        if name:
            return render_template('member.html', name=name, messages=messages)
        else:
            return redirect(url_for('index'))

    @app.route('/error')
    def error():
        message = request.args.get('message')
        return render_template('error.html', message=message)

    @app.route('/signin', methods=['POST'])
    def signin():
        username = request.form.get('username')
        password = request.form.get('password')

        # input validation 
        isValid = validate(
            username = username,
            password = password,
        )
        if not isValid:
            return redirect(url_for('error', message='帳號、或密碼不合法'))

        # access database
        member = unitOfWork.memberRepository.getMember(username, password)
        if member:
            session['id'] = member.id
            session['name'] = member.name
            session['username'] = member.username
            return redirect(url_for('member'))
        else:
            return redirect(url_for('error', message='帳號、或密碼輸入錯誤'))

    @app.route('/signout')
    def signout():
        session.pop('id', None)
        session.pop('name', None)
        session.pop('username', None)
        return redirect(url_for('index'))

    @app.route('/signup', methods=['POST'])
    def signup():
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')

        # input validation 
        isValid = validate(
            name = name,
            username = username,
            password = password,
        )
        if not isValid:
            return redirect(url_for('error', message='帳號資料有誤'))

        # access database
        success = unitOfWork.memberRepository.addMember(name, username, password)
        if success:
            return redirect(url_for('index'))
        else:
            return redirect(url_for('error', message='帳號已經被註冊'))

    @app.route('/message', methods=['POST'])
    def message():
        memberId = session['id']
        content = request.form.get('content')
        unitOfWork.messageRepository.addMessage(memberId, content)
        return redirect(url_for('member'))

def validate(username = None, password = None, name = None):
    if ((name == None or name != '') and 
        (username == None or re.match('[A-Za-z\d.]{4,30}', username)) and
        (password == None or re.match('(?=.*[A-Za-z])[a-zA-Z\d]{4,100}', password))):
        return True
    return False
