import functions
from flask import Flask, request, session, redirect, render_template
from repository import UnitOfWork

def configureRoutes(app: Flask, unitOfWork: UnitOfWork):
    @app.route('/')
    def index():
        if (session.get('isLogin')):
            return redirect('/member')
        else:
            return render_template('index.html')

    @app.route('/member')
    def member():
        if (session.get('isLogin')):
            return render_template('member.html')
        else:
            return redirect('/')

    @app.route('/error')
    def error():
        message = request.args.get('message')
        return render_template('error.html', message=message)

    @app.route('/signin', methods=['POST'])
    def signin():
        account = request.form.get('account')
        password = request.form.get('password')
        session['isLogin'] = functions.checkLogin(account, password)
        if session.get('isLogin'):
            return redirect('/member')
        else:
            message = functions.getErrorMessage(account, password)
            return redirect(f'/error?message={message}')

    @app.route('/signout')
    def signout():
        session['isLogin'] = False
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
