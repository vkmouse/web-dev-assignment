package repository

import (
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
