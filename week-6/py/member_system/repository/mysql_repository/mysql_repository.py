from mysql.connector.pooling import MySQLConnectionPool

class MySQLRepository:
    def __init__(self, cnxpool: MySQLConnectionPool, debug: bool):
        self.debug = debug
        self.cnxpool = cnxpool
        self.createTable()

    def createTable(self):
        with self.cnxpool.get_connection() as cnx:
            with cnx.cursor() as cursor:
                if not self.tableExists():
                    cursor.execute(self.createTableStatement)

    def dropTableIfExists(self):
        if self.tableExists():
            with self.cnxpool.get_connection() as cnx:
                with cnx.cursor() as cursor:
                    cursor.execute(self.dropTableStatement)

    def tableExists(self) -> bool:
        with self.cnxpool.get_connection() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute('SHOW TABLES;')
                isExists = (self.tableName,) in cursor.fetchall()
                return isExists

    @property
    def tableName(self) -> str:
        return NotImplemented

    @property
    def createTableStatement(self) -> str:
        return NotImplemented

    @property
    def dropTableStatement(self) -> str:
        return 'DROP TABLE {};'.format(self.tableName)