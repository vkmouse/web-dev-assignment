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
	r.unitOfWork = unitOfWork

	r.Engine = gin.Default()
	store := cookie.NewStore([]byte("secret"))
	r.Engine.Use(sessions.Sessions("session", store))

	r.Engine.LoadHTMLGlob(templateFolder + "/*")
	r.Engine.Static("/public", publicFolder)
	r.Engine.GET("/", r.homePage)
	r.Engine.GET("/error", r.errorPage)
	r.Engine.GET("/member", r.memberPage)
	r.Engine.GET("/signout", r.signout)
	r.Engine.POST("/signin", r.signin)
	r.Engine.POST("/signup", r.signup)
	r.Engine.POST("/message", r.message)
	r.Engine.GET("/api/member", r.memberGet)
	r.Engine.PATCH("/api/member", r.memberPatch)
}

func (r *Router) errorPage(ctx *gin.Context) {
	message, _ := ctx.GetQuery("message")
	ctx.HTML(http.StatusOK, "error.html", gin.H{"message": message})
}

func (r *Router) homePage(ctx *gin.Context) {
	session := sessions.Default(ctx)
	if session.Get("name") == nil {
		ctx.HTML(http.StatusOK, "index.html", gin.H{})
	} else {
		ctx.Redirect(http.StatusFound, "/member")
	}
}

func (r *Router) memberPage(ctx *gin.Context) {
	session := sessions.Default(ctx)
	name := session.Get("name")
	if name == nil {
		ctx.Redirect(http.StatusFound, "/")
	} else {
		raw := r.unitOfWork.MessageRepository.GetMessages()
		messages := []string{}
		for _, msg := range raw {
			messages = append(messages, msg.Name+": "+msg.Content)
		}
		ctx.HTML(http.StatusOK, "member.html", gin.H{"name": name, "messages": messages})
	}
}

func (r *Router) signin(ctx *gin.Context) {
	username := ctx.PostForm("username")
	password := ctx.PostForm("password")
	member := r.unitOfWork.MemberRepository.GetMember(username, password)
	success := member.Id != -1
	var location url.URL
	if success {
		session := sessions.Default(ctx)
		session.Set("id", member.Id)
		session.Set("name", member.Name)
		session.Set("username", member.Username)
		session.Save()
		location = url.URL{Path: "/member"}
	} else if username == "" || password == "" {
		data := url.Values{"message": {"請輸入帳號、密碼"}}
		location = url.URL{
			Path:     "/error",
			RawQuery: data.Encode(),
		}
	} else {
		data := url.Values{"message": {"帳號、或密碼輸入錯誤"}}
		location = url.URL{
			Path:     "/error",
			RawQuery: data.Encode(),
		}
	}

	ctx.Redirect(http.StatusFound, location.RequestURI())
}

func (r *Router) signout(ctx *gin.Context) {
	session := sessions.Default(ctx)
	session.Clear()
	session.Save()
	ctx.Redirect(http.StatusFound, "/")
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

func (r *Router) message(ctx *gin.Context) {
	session := sessions.Default(ctx)
	memberId := session.Get("id").(int)
	content := ctx.PostForm("content")
	r.unitOfWork.MessageRepository.AddMessage(memberId, content)
	ctx.Redirect(http.StatusFound, "/member")
}
