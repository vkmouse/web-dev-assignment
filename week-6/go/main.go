package main

import (
	. "Project/membersys/repository"
	. "Project/membersys/routes"
)

func main() {
	router := Router{}
	// unitOfWork := NewMemoryUnitOfWork()
	unitOfWork := NewMySQLUnitOfWork("config.json", false)
	router.Setup("templates", "public", &unitOfWork.UnitOfWork)
	router.Engine.Run(":8080")
}
