import mysql.connector

from member_system.core import List
from member_system.core import Message
from member_system.core import MessageRepository
from member_system.repository.mysql.repository import MySQLRepository

class MySQLMessageRepository(MySQLRepository, MessageRepository):
    def __init__(self, cnxpool: mysql.connector.pooling.MySQLConnectionPool, memberTableName: str, debug: bool):
        self.memberTableName = memberTableName
        MySQLRepository.__init__(self, cnxpool, debug)

    @MySQLRepository.withConnection
    def addMessage(self, __memberId: int, __content: str, cnx, cursor) -> None:
        query = 'INSERT INTO {} (member_id, content) VALUES (%s, %s)'.format(self.tableName)
        data = (__memberId, __content,)
        cursor.execute(query, data)
        cnx.commit()

    @MySQLRepository.withConnection
    def getMessages(self, cnx, cursor) -> List[Message]:
        query = (
            'SELECT name, content '
            'FROM {message} '
            'INNER JOIN {member} '
            '  ON {message}.member_id = {member}.id '
            'ORDER BY {message}.id'
        ).format(message=self.tableName, member=self.memberTableName)
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
