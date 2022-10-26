package main

import (
	"Project/functions"
)

func main() {
	router := functions.SetupRouter("templates", "public")
	router.Run(":8080")
}
