def checkLogin(account, password):
    if (account == 'test' and password == 'test'):
        return True
    else:
        return False

def getErrorMessage(account, password):
    isLogin = checkLogin(account, password)
    if (not isLogin):
        if (account == '' or password == ''):
            return '請輸入帳號、密碼'
        else:
            return '帳號、或密碼輸入錯誤'
    return ''
