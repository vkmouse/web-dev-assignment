package routes

import (
	. "Project/membersys/core"

	"net/http"
	"net/url"

	"github.com/gin-contrib/sessions"
	"github.com/gin-contrib/sessions/cookie"
	"github.com/gin-gonic/gin"
)

type Router struct {
	Engine     *gin.Engine
	unitOfWork *UnitOfWork
}

func (r *Router) Setup(templateFolder string, publicFolder string, unitOfWork *UnitOfWork) {
	r.Engine = gin.Default()
	r.unitOfWork = unitOfWork

	createSession(r.Engine)
	r.Engine.LoadHTMLGlob(templateFolder + "/*")
	r.Engine.Static("/public", publicFolder)
	r.Engine.GET("/", r.homePage)
	r.Engine.GET("/error", r.errorPage)
	r.Engine.GET("/member", r.memberPage)
	r.Engine.GET("/signout", r.signout)
	r.Engine.POST("/signin", r.signin)
	r.Engine.POST("/signup", r.signup)
}

func createSession(router *gin.Engine) {
	store := cookie.NewStore([]byte("secret"))
	router.Use(sessions.Sessions("isLogin", store))
}

func checkLogin(ctx *gin.Context) bool {
	session := sessions.Default(ctx)
	return session.Get("isLogin") == true
}

func (r *Router) errorPage(ctx *gin.Context) {
	message, _ := ctx.GetQuery("message")
	ctx.HTML(http.StatusOK, "error.html", gin.H{"message": message})
}

func (r *Router) homePage(ctx *gin.Context) {
	if checkLogin(ctx) {
		location := url.URL{Path: "/member"}
		ctx.Redirect(http.StatusFound, location.RequestURI())
	} else {
		ctx.HTML(http.StatusOK, "index.html", gin.H{})
	}
}

func (r *Router) memberPage(ctx *gin.Context) {
	if checkLogin(ctx) {
		ctx.HTML(http.StatusOK, "member.html", gin.H{})
	} else {
		location := url.URL{Path: "/"}
		ctx.Redirect(http.StatusFound, location.RequestURI())
	}
}

func (r *Router) signin(ctx *gin.Context) {
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

func (r *Router) signout(ctx *gin.Context) {
	SetSeesion(ctx, "isLogin", false)
	location := url.URL{Path: "/"}
	ctx.Redirect(http.StatusFound, location.RequestURI())
}

func (r *Router) signup(ctx *gin.Context) {
	name := ctx.PostForm("name")
	username := ctx.PostForm("username")
	password := ctx.PostForm("password")
	success := r.unitOfWork.MemberRepository.AddMember(name, username, password)
	if success {
		ctx.Redirect(http.StatusFound, "/")
	} else {
		ctx.Redirect(http.StatusFound, "/error?message=帳號已經被註冊")
	}
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
