import mysql.connector

class MySQLRepository:
    def withConnection(func):
        def wrap(self, *args, **kwargs):
            cnx = self.cnxpool.get_connection()
            cursor = cnx.cursor()
            output = None
            try:
                output = func(self, *args, **kwargs, cnx=cnx, cursor=cursor)
            except:
                print('Error')
            finally:
                cursor.close()
                cnx.close()
            return output
        return wrap


    def __init__(self, cnxpool: mysql.connector.pooling.MySQLConnectionPool, debug: bool):
        self.debug = debug
        self.cnxpool = cnxpool
        self.createTable()

    @withConnection
    def createTable(self, cnx, cursor):
        if not self.tableExists():
            cursor.execute(self.createTableStatement)

    @withConnection
    def dropTableIfExists(self, cnx, cursor):
        if self.tableExists():
            cursor.execute(self.dropTableStatement)

    @withConnection
    def tableExists(self, cnx, cursor) -> bool:
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