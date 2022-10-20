package main

import (
	. "Project/http"
	"fmt"
	"net"
)

func main() {
	srv, err := net.Listen("tcp", ":8080")
	defer srv.Close()
	if err != nil {
		fmt.Println("error")
	}

	for {
		conn, _ := srv.Accept()
		Handle(conn, []func(conn net.Conn, ctx Context) bool{
			HomePage,
			MemberPage,
			ErrorPage,
			Style,
			Signin,
			Signout,
			Icon,

			NoRoute,
		})
	}
}
