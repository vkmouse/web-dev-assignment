package main

import (
	. "Project/membersys/routes"
)

func main() {
	router := Router{}
	router.Setup("templates", "public")
	router.Engine.Run(":8080")
}
