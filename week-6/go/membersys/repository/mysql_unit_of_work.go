package repository

import (
	. "Project/membersys/core"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"

	"database/sql"

	_ "github.com/go-sql-driver/mysql"
)

type MySQLUnitOfWork struct {
	UnitOfWork
	config string
	debug  bool
}

type MySQLConfig struct {
	User     string `json:"user"`
	Password string `json:"password"`
	Host     string `json:"host"`
	Database string `json:"database"`
}

func (u *MySQLUnitOfWork) Init() {
	dataSourceName := loadMySQLConfig(u.config)
	db, _ := sql.Open("mysql", dataSourceName)
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

func loadMySQLConfig(configPath string) string {
	jsonFile, _ := os.Open(configPath)
	defer jsonFile.Close()
	bytes, _ := ioutil.ReadAll(jsonFile)
	var config MySQLConfig
	json.Unmarshal(bytes, &config)
	return fmt.Sprintf("%s:%s@tcp(%s)/%s", config.User, config.Password, config.Host, config.Database)
}
