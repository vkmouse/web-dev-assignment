from flask import Flask, request, session, redirect, render_template
from repository import UnitOfWork

def configureRoutes(app: Flask, unitOfWork: UnitOfWork):
    @app.route('/')
    def index():
        if checkUsernameFromSession():
            return redirect('/member')
        else:
            return render_template('index.html')

    @app.route('/member')
    def member():
        if checkUsernameFromSession():
            return render_template('member.html')
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
        success = unitOfWork.memberRepository.memberExists(username, password)
        if success:
            session['username'] = username
            return redirect('/member')
        elif username == '' or password == '':
            return redirect('/error?message=請輸入帳號、密碼')
        else:
            return redirect('/error?message=帳號、或密碼輸入錯誤')

    @app.route('/signout')
    def signout():
        session.pop('username', None)
        return redirect('/')

    @app.route('/signup', methods=['POST'])
    def signup():
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        success = unitOfWork.memberRepository.addUser(name, username, password)
        if success:
            return redirect('/')
        else:
            return redirect('/error?message=帳號已經被註冊')

    def checkUsernameFromSession():
        username = session.get('username')
        return username and unitOfWork.memberRepository.usernameExists(username)