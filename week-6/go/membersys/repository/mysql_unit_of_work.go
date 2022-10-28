package repository

import (
	. "Project/membersys/core"

	"database/sql"

	_ "github.com/go-sql-driver/mysql"
)

type MySQLUnitOfWork struct {
	UnitOfWork
	config string
	debug  bool
}

func (u *MySQLUnitOfWork) Init() {
	db, _ := sql.Open("mysql", u.config)
	mysql := MySQLRepository{db: db, debug: u.debug}

	memberRepository := new(MySQLMemberRepository)
	memberRepository.MySQLRepository = mysql
	messageRepository := new(MySQLMessageRepository)
	messageRepository.MySQLRepository = mysql
	messageRepository.memberTableName = memberRepository.TableName()

	u.MemberRepository = memberRepository
	u.MessageRepository = messageRepository

	if u.debug {
		messageRepository.DropTable(messageRepository)
		memberRepository.DropTable(memberRepository)
		memberRepository.CreateTable(memberRepository)
		messageRepository.CreateTable(messageRepository)
	}
}

func NewMySQLUnitOfWork(config string, debug bool) *MySQLUnitOfWork {
	unitOfWork := MySQLUnitOfWork{config: config, debug: debug}
	InitUnitOfWork(&unitOfWork)
	return &unitOfWork
}
