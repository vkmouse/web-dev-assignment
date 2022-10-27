package main

import (
	. "Project/membersys/routes"
)

func main() {
	router := SetupRouter("templates", "public")
	router.Run(":8080")
}
