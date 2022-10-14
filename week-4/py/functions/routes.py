import functions
import time
from flask import Flask, request, redirect, render_template, make_response
from flask.wrappers import Response
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

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
        ciphertext = request.cookies.get('isLogin')
        if ciphertext != None:
            plaintext = bytes.decode(f.decrypt(ciphertext), encoding='utf-8')
            return plaintext == 'true'
        return False

def setLogin(args) -> Response:
    resp = make_response(args)
    ciphertext = generateCiphertext()
    resp.set_cookie('isLogin', value=ciphertext, expires=time.time()+60)
    return resp

def resetLogin(args) -> Response:
    resp = make_response(args)
    resp.delete_cookie('isLogin')
    return resp

def generateCiphertext():
    return f.encrypt(b'true').decode("utf-8")