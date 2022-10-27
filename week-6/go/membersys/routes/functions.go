package routes

func CheckLogin(account string, password string) bool {
	if account == "test" && password == "test" {
		return true
	} else {
		return false
	}
}

func GetErrorMessage(account string, password string) string {
	isLogin := CheckLogin(account, password)
	if !isLogin {
		if account == "" || password == "" {
			return "請輸入帳號、密碼"
		} else {
			return "帳號、或密碼輸入錯誤"
		}
	}
	return ""
}
