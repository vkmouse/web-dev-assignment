from functions import *

def testCheckLogin():
    assert checkLogin('test', 'test') == True
    assert checkLogin('test', '') == False
    assert checkLogin('', 'test') == False
    assert checkLogin('', '') == False
    assert checkLogin('123', '456') == False

def testGetErrorMessage():
    assert getErrorMessage('', '') == '請輸入帳號、密碼'
    assert getErrorMessage('test', '') == '請輸入帳號、密碼'
    assert getErrorMessage('', 'test') == '請輸入帳號、密碼'
    assert getErrorMessage('123', '456') == '帳號、或密碼輸入錯誤'
    assert getErrorMessage('test', 'test') == ''
