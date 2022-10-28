package repository

import (
	"database/sql"

	_ "github.com/go-sql-driver/mysql"
)

type MySQLUnitOfWork struct {
	MemberRepository MySQLMemberRepository
}

func NewMySQLUnitOfWork(config string, debug bool) *MySQLUnitOfWork {
	db, _ := sql.Open("mysql", config)

	unitOfWork := MySQLUnitOfWork{
		MemberRepository: MySQLMemberRepository{MySQLRepository{db: db, debug: debug}},
	}

	return &unitOfWork
}
