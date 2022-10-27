package routes

import (
	"net/http"
	"net/url"

	"github.com/gin-contrib/sessions"
	"github.com/gin-contrib/sessions/cookie"
	"github.com/gin-gonic/gin"
)

func SetupRouter(templateFolder string, publicFolder string) *gin.Engine {
	router := gin.Default()

	createSession(router)
	router.LoadHTMLGlob(templateFolder + "/*")
	router.Static("/public", publicFolder)
	router.GET("/", homePage)
	router.GET("/error", errorPage)
	router.GET("/member", memberPage)
	router.GET("/signout", signout)
	router.POST("/signin", signin)

	return router
}

func createSession(router *gin.Engine) {
	store := cookie.NewStore([]byte("secret"))
	router.Use(sessions.Sessions("isLogin", store))
}

func checkLogin(ctx *gin.Context) bool {
	session := sessions.Default(ctx)
	return session.Get("isLogin") == true
}

func errorPage(ctx *gin.Context) {
	message, _ := ctx.GetQuery("message")
	ctx.HTML(http.StatusOK, "error.html", gin.H{"message": message})
}

func homePage(ctx *gin.Context) {
	if checkLogin(ctx) {
		location := url.URL{Path: "/member"}
		ctx.Redirect(http.StatusFound, location.RequestURI())
	} else {
		ctx.HTML(http.StatusOK, "index.html", gin.H{})
	}
}

func memberPage(ctx *gin.Context) {
	if checkLogin(ctx) {
		ctx.HTML(http.StatusOK, "member.html", gin.H{})
	} else {
		location := url.URL{Path: "/"}
		ctx.Redirect(http.StatusFound, location.RequestURI())
	}
}

func signin(ctx *gin.Context) {
	account := ctx.PostForm("account")
	password := ctx.PostForm("password")
	SetSeesion(ctx, "isLogin", CheckLogin(account, password))

	var location url.URL
	if checkLogin(ctx) {
		location = url.URL{Path: "/member"}
	} else {
		message := GetErrorMessage(account, password)
		data := url.Values{"message": {message}}
		location = url.URL{
			Path:     "/error",
			RawQuery: data.Encode(),
		}
	}
	ctx.Redirect(http.StatusFound, location.RequestURI())
}

func signout(ctx *gin.Context) {
	SetSeesion(ctx, "isLogin", false)
	location := url.URL{Path: "/"}
	ctx.Redirect(http.StatusFound, location.RequestURI())
}

func SetSeesion(ctx *gin.Context, key interface{}, val interface{}) {
	session := sessions.Default(ctx)
	session.Set(key, val)
	session.Save()
}

func Redirect(ctx *gin.Context, code int, location string) {
	url := url.URL{Path: location}
	ctx.Redirect(code, url.RequestURI())
}
