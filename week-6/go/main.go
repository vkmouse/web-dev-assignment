package main

import (
	. "Project/membersys/repository"
	. "Project/membersys/routes"
)

func main() {
	router := Router{}
	unitOfWork := NewMemoryUnitOfWork()
	router.Setup("templates", "public", &unitOfWork.UnitOfWork)
	router.Engine.Run(":8080")
}
