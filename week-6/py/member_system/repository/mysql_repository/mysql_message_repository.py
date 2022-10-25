from typing import List
from mysql.connector.connection import MySQLConnection
from member_system.core import Message
from member_system.repository.mysql_repository.mysql_repository import MySQLRepository
from member_system.repository.unit_of_work import MessageRepository

class MySQLMessageRepository(MySQLRepository, MessageRepository):
    def __init__(self, cnx: MySQLConnection, memberTableName: str, debug: bool):
        self.memberTableName = memberTableName
        MySQLRepository.__init__(self, cnx, debug)

    def addMessage(self, __memberId: int, __content: str) -> None:
        query = (
            'INSERT INTO {} (member_id, content) '
            'VALUES (%s, %s)'
        ).format(self.tableName)
        data = (__memberId, __content,)
        with self.cnx.cursor() as cursor:
            cursor.execute(query, data)
        self.cnx.commit()

    def getMessages(self) -> List[Message]:
        query = (
            'SELECT name, content '
            'FROM {message} '
            'INNER JOIN {member} '
            '  ON {message}.member_id = {member}.id '
            'ORDER BY {message}.id'
            
        ).format(message=self.tableName, member=self.memberTableName)
        with self.cnx.cursor() as cursor:
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
