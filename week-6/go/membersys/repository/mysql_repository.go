package repository

import (
	"database/sql"
	"fmt"

	_ "github.com/go-sql-driver/mysql"
)

type MySQLRepository struct {
	db    *sql.DB
	debug bool
}

type IMySQLRepository interface {
	CreateTableStatement() string
	TableName() string
}

func (r *MySQLRepository) CreateTable(ir IMySQLRepository) {
	if !r.TableExists(ir) {
		query := ir.CreateTableStatement()
		r.db.Query(query)
	}
}

func (r *MySQLRepository) DropTable(ir IMySQLRepository) {
	if r.TableExists(ir) {
		query := fmt.Sprintf(`DROP TABLE %s`, ir.TableName())
		r.db.Query(query)
	}
}

func (r *MySQLRepository) TableExists(ir IMySQLRepository) bool {
	query := "SHOW TABLES;"
	rows, _ := r.db.Query(query)
	for rows.Next() {
		var table string
		rows.Scan(&table)
		if table == ir.TableName() {
			return true
		}
	}
	return false
}
