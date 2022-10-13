import functions
import time
from flask import Flask, request, session, redirect, render_template, make_response
from flask.wrappers import Response

def configureRoutes(app: Flask):
    @app.route('/')
    def index():
        if checkLogin():
            return redirect('/member')
        else:
            return render_template('index.html')

    @app.route('/member')
    def member():
        if checkLogin():
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
        isLogin = functions.checkLogin(account, password)
        if isLogin:
            return setLogin(redirect('/member'))
        else:
            message = functions.getErrorMessage(account, password)
            return resetLogin(redirect(f'/error?message={message}'))

    @app.route('/signout')
    def signout():
        return resetLogin(redirect('/'))

    @app.route('/square/<int:num>')
    def square(num):
        result = str(num ** 2)
        return render_template('square.html', num=num, result=result)

    def checkLogin():
        return session.get('isLogin') and request.cookies.get('isLogin')

    def setLogin(args) -> Response:
        session['isLogin'] = True
        resp = make_response(args)
        resp.set_cookie('isLogin', value='true', expires=time.time()+60)
        return resp

    def resetLogin(args) -> Response:
        if session.get('isLogin'):
            session.pop('isLogin')
        resp = make_response(args)
        resp.delete_cookie('isLogin')
        return resp