package http

import (
	"net"
	"strings"
)

func HomePage(conn net.Conn, ctx Context) bool {
	if ctx.Method == "GET" && ctx.RequestedURL == "/" {
		resp := ""
		if strings.Contains(ctx.Cookie, "isLogin=true") {
			resp += statusLine(302)
			resp += location("/member")
		} else {
			resp += statusLine(200)
			resp += contentType("text/html")
			resp += "\n" + fromFile("templates/index.html")
		}
		conn.Write([]byte(resp))
		return true
	}
	return false
}

func MemberPage(conn net.Conn, ctx Context) bool {
	if ctx.Method == "GET" && ctx.RequestedURL == "/member" {
		resp := ""
		if strings.Contains(ctx.Cookie, "isLogin=true") {
			resp += statusLine(200)
			resp += contentType("text/html")
			resp += "\n" + fromFile("templates/member.html")
		} else {
			resp += statusLine(302)
			resp += location("/")
		}
		conn.Write([]byte(resp))
		return true
	}
	return false
}

func ErrorPage(conn net.Conn, ctx Context) bool {
	if ctx.Method == "GET" && ctx.RequestedURL == "/error" {
		resp := statusLine(200)
		resp += contentType("text/html")
		resp += "\n" + fromFile("templates/error.html")
		resp = strings.Replace(resp, "{{.message}}", strings.Replace(ctx.QueryString, "message=", "", -1), -1)
		conn.Write([]byte(resp))
		return true
	}
	return false
}

func Signin(conn net.Conn, ctx Context) bool {
	if ctx.Method == "POST" && ctx.RequestedURL == "/signin" {
		resp := statusLine(302)
		if ctx.Body == "account=test&password=test\n" {
			resp += setCookie("isLogin=true")
			resp += location("/member")
		} else {
			resp += location("/error?message=%E8%AB%8B%E8%BC%B8%E5%85%A5%E5%B8%B3%E8%99%9F%E3%80%81%E5%AF%86%E7%A2%BC\r\n\r\n")
		}
		conn.Write([]byte(resp))
		return true
	}
	return false
}

func Signout(conn net.Conn, ctx Context) bool {
	if ctx.Method == "GET" && ctx.RequestedURL == "/signout" {
		resp := statusLine(302)
		resp += setCookie("isLogin=")
		resp += location("/")
		conn.Write([]byte(resp))
		return true
	}
	return false
}

func Style(conn net.Conn, ctx Context) bool {
	if ctx.Method == "GET" && ctx.RequestedURL == "/public/style/style.css" {
		resp := statusLine(200)
		resp += contentType("text/css")
		resp += "\n" + fromFile("public/style/style.css")
		conn.Write([]byte(resp))
		return true
	}
	return false
}

func Icon(conn net.Conn, ctx Context) bool {
	if ctx.Method == "GET" && ctx.RequestedURL == "/public/style/style.css" {
		resp := statusLine(200)
		resp += contentType("text/css")
		resp += "\n" + fromFile("public/icon/favicon-16x16.css")
		conn.Write([]byte(resp))
		return true
	}
	return false
}

func NoRoute(conn net.Conn, ctx Context) bool {
	resp := statusLine(404)
	resp += "\n" + "<h1>Not Found</h1>"
	conn.Write([]byte(resp))
	return true
}
