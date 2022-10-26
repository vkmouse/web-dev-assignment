package functions

import (
	"net/http"
	"net/http/httptest"
	"net/url"
	"strings"
	"testing"

	"github.com/gin-gonic/gin"
	"github.com/stretchr/testify/assert"
)

func setupRouter() *gin.Engine {
	return SetupRouter("../templates", "../public")
}

func assertPath(t *testing.T, req *http.Request, expected string) {
	assert.Equal(t, expected, req.URL.Path)
}

func assertQuery(t *testing.T, req *http.Request, expected url.Values) {
	assert.Equal(t, expected.Encode(), req.URL.RawQuery)
}

func assertContains(t *testing.T, w *httptest.ResponseRecorder, expected string) {
	assert.Contains(t, w.Body.String(), expected)
}

func assertStatusOK(t *testing.T, w *httptest.ResponseRecorder) {
	assert.Equal(t, http.StatusOK, w.Code)
}

func get(router *gin.Engine, path string, data url.Values, follow bool) (*httptest.ResponseRecorder, *http.Request) {
	w := httptest.NewRecorder()
	req, _ := http.NewRequest(http.MethodGet, path, nil)
	req.URL.RawQuery = data.Encode()
	router.ServeHTTP(w, req)

	if follow {
		return followRedirects(router, w, req)
	}
	return w, req
}

func post(router *gin.Engine, path string, data url.Values, follow bool) (*httptest.ResponseRecorder, *http.Request) {
	w := httptest.NewRecorder()
	body := strings.NewReader(data.Encode())
	req, _ := http.NewRequest(http.MethodPost, path, body)
	req.Header.Add("Content-Type", "application/x-www-form-urlencoded")
	router.ServeHTTP(w, req)

	if follow {
		req.Method = http.MethodGet
		return followRedirects(router, w, req)
	}
	return w, req
}

func followRedirects(router *gin.Engine, w *httptest.ResponseRecorder, req *http.Request) (*httptest.ResponseRecorder, *http.Request) {
	location := w.Header().Get("Location")
	if location == "" {
		return w, req
	}

	req.URL, _ = url.Parse(location)
	w = httptest.NewRecorder()
	router.ServeHTTP(w, req)
	return followRedirects(router, w, req)
}

func TestError(t *testing.T) {
	messages := []string{
		"請輸入帳號、密碼",
		"帳號、或密碼輸入錯誤",
	}

	router := setupRouter()
	for _, message := range messages {
		data := url.Values{"message": {message}}
		w, req := get(router, "/error", data, true)
		assertPath(t, req, "/error")
		assertQuery(t, req, data)
		assertContains(t, w, message)
		assertStatusOK(t, w)
	}
}

func TestHome(t *testing.T) {
	router := setupRouter()
	w, req := get(router, "/", nil, true)
	assertPath(t, req, "/")
	assertContains(t, w, "歡迎光臨，請輸入帳號密碼")
	assertStatusOK(t, w)
}

func TestMemberIfLogin(t *testing.T) {
	router := setupRouter()
	router.GET("/mockapi", func(ctx *gin.Context) {
		SetSeesion(ctx, "isLogin", true)
		Redirect(ctx, http.StatusFound, "/member")
	})

	w, req := get(router, "/mockapi", nil, true)
	assertPath(t, req, "/member")
	assertContains(t, w, "歡迎光臨，這是會員頁")
	assertStatusOK(t, w)
}

func TestRedirectsHomeToMemberIfLogin(t *testing.T) {
	router := setupRouter()
	router.GET("/mockapi", func(ctx *gin.Context) {
		SetSeesion(ctx, "isLogin", true)
		Redirect(ctx, http.StatusFound, "/")
	})

	w, req := get(router, "/mockapi", nil, true)
	assertPath(t, req, "/member")
	assertContains(t, w, "歡迎光臨，這是會員頁")
	assertStatusOK(t, w)
}

func TestRedirectsMemberToHomeIfNotLogin(t *testing.T) {
	router := setupRouter()
	w, req := get(router, "/member", nil, true)
	assertPath(t, req, "/")
	assertContains(t, w, "歡迎光臨，請輸入帳號密碼")
	assertStatusOK(t, w)
}

func TestSigninSuccess(t *testing.T) {
	data := url.Values{"account": {"test"}, "password": {"test"}}
	router := setupRouter()
	w, req := post(router, "/signin", data, true)
	assertPath(t, req, "/member")
	assertContains(t, w, "歡迎光臨，這是會員頁")
	assertStatusOK(t, w)
}

func TestSigninWithoutAccountOrPassword(t *testing.T) {
	data := url.Values{"account": {""}, "password": {""}}
	router := setupRouter()
	w, req := post(router, "/signin", data, true)
	assertPath(t, req, "/error")
	assertContains(t, w, "請輸入帳號、密碼")
	assertStatusOK(t, w)
}

func TestSigninForPasswordMismatchError(t *testing.T) {
	data := url.Values{"account": {"123"}, "password": {"123"}}
	router := setupRouter()
	w, req := post(router, "/signin", data, true)
	assertPath(t, req, "/error")
	assertContains(t, w, "帳號、或密碼輸入錯誤")
	assertStatusOK(t, w)
}

func TestSquare(t *testing.T) {
	router := setupRouter()
	w, req := get(router, "/square/4", nil, true)
	assertPath(t, req, "/square/4")
	assertContains(t, w, "16")
	assertStatusOK(t, w)
}
