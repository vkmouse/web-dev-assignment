package mysql_repository

import (
	. "Project/membersys/core"

	"fmt"

	_ "github.com/go-sql-driver/mysql"
)

type MySQLMessageRepository struct {
	MySQLRepository
	memberTableName string
}

func (r *MySQLMessageRepository) CreateTableStatement() string {
	return fmt.Sprintf(`
		CREATE TABLE %s (
			id           BIGINT        AUTO_INCREMENT,
			member_id    BIGINT        NOT NULL,
			content      VARCHAR(255)  NOT NULL,
			like_count   INT UNSIGNED  NOT NULL DEFAULT 0,
			time         DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
			PRIMARY KEY  (id),
			FOREIGN KEY  (member_id) REFERENCES %s(id)
		);
	`, r.TableName(), r.memberTableName)
}

func (r *MySQLMessageRepository) TableName() string {
	if r.debug {
		return "test_message"
	} else {
		return "message"
	}
}

func (r *MySQLMessageRepository) AddMessage(memberId int, content string) {
	query := fmt.Sprintf(
		"INSERT INTO %s (member_id, content) VALUES (?, ?)",
		r.TableName())
	r.db.Exec(query, memberId, content)
}

func (r *MySQLMessageRepository) GetMessages() []Message {
	query := fmt.Sprintf(`
		SELECT name, content FROM %s 
		INNER JOIN %s ON %s.member_id = %s.id 
        ORDER BY %s.id`,
		r.TableName(), r.memberTableName, r.TableName(), r.memberTableName, r.TableName())
	rows, _ := r.db.Query(query)
	messages := []Message{}
	for rows.Next() {
		var message Message
		rows.Scan(&message.Name, &message.Content)
		messages = append(messages, message)
	}
	return messages
}
