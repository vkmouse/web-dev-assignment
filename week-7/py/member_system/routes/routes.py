from flask import Flask, request, session, redirect, render_template
from member_system.repository import UnitOfWork

def configureRoutes(app: Flask, unitOfWork: UnitOfWork):
    @app.route('/')
    def index():
        if session.get('name'):
            return redirect('/member')
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
            return redirect('/')

    @app.route('/error')
    def error():
        message = request.args.get('message')
        return render_template('error.html', message=message)

    @app.route('/signin', methods=['POST'])
    def signin():
        username = request.form.get('username')
        password = request.form.get('password')
        member = unitOfWork.memberRepository.getMember(username, password)
        if member:
            session['id'] = member.id
            session['name'] = member.name
            session['username'] = member.username
            return redirect('/member')
        elif username == '' or password == '':
            return redirect('/error?message=請輸入帳號、密碼')
        else:
            return redirect('/error?message=帳號、或密碼輸入錯誤')

    @app.route('/signout')
    def signout():
        session.pop('id', None)
        session.pop('name', None)
        session.pop('username', None)
        return redirect('/')

    @app.route('/signup', methods=['POST'])
    def signup():
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        success = unitOfWork.memberRepository.addMember(name, username, password)
        if success:
            return redirect('/')
        else:
            return redirect('/error?message=帳號已經被註冊')

    @app.route('/message', methods=['POST'])
    def message():
        memberId = session['id']
        content = request.form.get('content')
        unitOfWork.messageRepository.addMessage(memberId, content)
        return redirect('/member')
