package repository

import (
	. "Project/membersys/core"

	"fmt"

	_ "github.com/go-sql-driver/mysql"
)

type MySQLMemberRepository struct {
	MySQLRepository
}

func (r *MySQLMemberRepository) CreateTableStatement() string {
	return fmt.Sprintf(`
		CREATE TABLE %s (
	    	id              bigint        NOT NULL  AUTO_INCREMENT,
	    	name            varchar(255)  NOT NULL,
	    	username        varchar(255)  NOT NULL,
	    	password        varchar(255)  NOT NULL,
	    	follower_count  int unsigned  NOT NULL  DEFAULT 0,
	    	time            datetime      NOT NULL  DEFAULT CURRENT_TIMESTAMP,
	    	PRIMARY KEY (id)
		);
	`, r.TableName())
}

func (r *MySQLMemberRepository) TableName() string {
	if r.debug {
		return "test_member"
	} else {
		return "member"
	}
}

func (r *MySQLMemberRepository) AddMember(name string, username string, password string) bool {
	if r.memberExists(username) {
		return false
	}
	query := fmt.Sprintf(
		"INSERT INTO %s (name, username, password) VALUES (?, ?, ?);",
		r.TableName())
	r.db.Exec(query, name, username, password)
	return true
}

func (r *MySQLMemberRepository) GetMember(username string, password string) Member {
	member := Member{Id: -1}
	query := fmt.Sprintf(
		"SELECT id, name, username, password FROM %s WHERE username=? AND password=?",
		r.TableName())
	row := r.db.QueryRow(query, username, password)
	row.Scan(&member.Id, &member.Name, &member.Username, &member.Password)
	return member
}

func (r *MySQLMemberRepository) memberExists(username string) bool {
	query := fmt.Sprintf(
		"SELECT COUNT(*) FROM %s WHERE username=?",
		r.TableName())
	row := r.db.QueryRow(query, username)
	var count int
	row.Scan(&count)
	return count > 0
}
