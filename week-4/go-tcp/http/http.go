package http

import (
	"fmt"
	"net"
	"os"
)

func Handle(conn net.Conn, pages []func(conn net.Conn, ctx Context) bool) {
	defer conn.Close()

	bufSize := 256
	req := make([]byte, 0, 4096)
	buf := make([]byte, bufSize)

	for {
		n, _ := conn.Read(buf)
		req = append(req, buf[:n]...)
		if n != bufSize {
			break
		}
	}

	ctx := ParseRequest(string(req))
	fmt.Println(ctx.Method, ctx.RequestedURL, ctx.Body)
	for _, page := range pages {
		if page(conn, ctx) {
			break
		}
	}
}

func statusLine(code int) string {
	switch code {
	case 200:
		return "HTTP/1.1 200 OK\r\n"
	case 302:
		return "HTTP/1.1 302 Found\r\n"
	default:
		return "HTTP/1.1 404\r\n"
	}
}

func setCookie(s string) string {
	return fmt.Sprintf("Set-Cookie: %s\r\n", s)
}

func location(path string) string {
	return fmt.Sprintf("Location: %s\r\n", path)
}

func contentType(s string) string {
	return fmt.Sprintf("Content-Type: %s; charset=utf-8\r\n", s)
}

func fromFile(s string) string {
	data, _ := os.ReadFile(s)
	return string(data)
}
