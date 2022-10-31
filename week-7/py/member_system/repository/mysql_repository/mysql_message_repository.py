from typing import List
from mysql.connector.pooling import MySQLConnectionPool
from member_system.core import Message
from member_system.repository.mysql_repository.mysql_repository import MySQLRepository
from member_system.repository.unit_of_work import MessageRepository

class MySQLMessageRepository(MySQLRepository, MessageRepository):
    def __init__(self, cnxpool: MySQLConnectionPool, memberTableName: str, debug: bool):
        self.memberTableName = memberTableName
        MySQLRepository.__init__(self, cnxpool, debug)

    def addMessage(self, __memberId: int, __content: str) -> None:
        query = (
            'INSERT INTO {} (member_id, content) '
            'VALUES (%s, %s)'
        ).format(self.tableName)
        data = (__memberId, __content,)
        with self.cnxpool.get_connection() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute(query, data)
            cnx.commit()

    def getMessages(self) -> List[Message]:
        query = (
            'SELECT name, content '
            'FROM {message} '
            'INNER JOIN {member} '
            '  ON {message}.member_id = {member}.id '
            'ORDER BY {message}.id'
        ).format(message=self.tableName, member=self.memberTableName)
        with self.cnxpool.get_connection() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return list(map(lambda row: Message(row[0], row[1]), rows))

    @property
    def tableName(self) -> str:
        if self.debug:
            return 'test_message'
        else:
            return 'message'

    @property
    def createTableStatement(self) -> str:
        return (
            'CREATE TABLE {} ('
            '    id           BIGINT        AUTO_INCREMENT,'
            '    member_id    BIGINT        NOT NULL,'
            '    content      VARCHAR(255)  NOT NULL,'
            '    like_count   INT UNSIGNED  NOT NULL DEFAULT 0,'
            '    time         DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,'
            '    PRIMARY KEY  (id),'
            '    FOREIGN KEY  (member_id) REFERENCES {}(id)'
            ');'
        ).format(self.tableName, self.memberTableName)
