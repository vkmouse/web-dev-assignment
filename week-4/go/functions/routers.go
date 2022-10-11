package functions

import (
	"net/http"
	"net/url"
	"strconv"

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
	router.GET("/square/:num", square)
	router.POST("/signin", signin)
	router.POST("/square", squareRedirects)

	return router
}

func createSession(router *gin.Engine) {
	store := cookie.NewStore([]byte("secret"))
	router.Use(sessions.Sessions("isLogin", store))
}

func errorPage(ctx *gin.Context) {
	message, _ := ctx.GetQuery("message")
	ctx.HTML(http.StatusOK, "error.html", gin.H{"message": message})
}

func homePage(ctx *gin.Context) {
	session := sessions.Default(ctx)
	if session.Get("isLogin") == true {
		location := url.URL{Path: "/member"}
		ctx.Redirect(http.StatusFound, location.RequestURI())
	} else {
		ctx.HTML(http.StatusOK, "index.html", gin.H{})
	}
}

func memberPage(ctx *gin.Context) {
	session := sessions.Default(ctx)
	if session.Get("isLogin") == true {
		ctx.HTML(http.StatusOK, "member.html", gin.H{})
	} else {
		location := url.URL{Path: "/"}
		ctx.Redirect(http.StatusFound, location.RequestURI())
	}
}

func signin(ctx *gin.Context) {
	account := ctx.PostForm("account")
	password := ctx.PostForm("password")
	session := sessions.Default(ctx)
	session.Set("isLogin", CheckLogin(account, password))
	session.Save()

	var location url.URL
	if session.Get("isLogin") == true {
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
	session := sessions.Default(ctx)
	session.Set("isLogin", false)
	session.Save()

	location := url.URL{Path: "/"}
	ctx.Redirect(http.StatusFound, location.RequestURI())
}

func squareRedirects(ctx *gin.Context) {
	num := ctx.PostForm("num")
	location := url.URL{Path: "/square/" + num}
	ctx.Redirect(http.StatusFound, location.RequestURI())
}

func square(ctx *gin.Context) {
	num, _ := strconv.Atoi(ctx.Param("num"))
	result := num * num
	ctx.HTML(http.StatusOK, "square.html", gin.H{"num": num, "result": result})
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
