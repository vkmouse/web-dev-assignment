import json
from typing import List
import mysql.connector
from mysql.connector.connection import MySQLConnection
from member_system.core import Member, Message
from member_system.repository.mysql_repository import MySQLRepository
from member_system.repository.repository import MemberRepository, MessageRepository, UnitOfWork

class MySQLMemberRepository(MySQLRepository, MemberRepository):
    def addMember(self, __name: str, __username: str, __password: str) -> bool:
        if self.__usernameExists(__username):
            return False
        query = (
            'INSERT INTO {} (name, username, password) '
            'VALUES (%s, %s, %s)'
        ).format(self.tableName)
        data = (__name, __username, __password,)
        with self.cnx.cursor() as cursor:
            cursor.execute(query, data)
        self.cnx.commit()
        return True

    def getMember(self, __username: str, __password: str) -> Member | None:
        query = (
            'SELECT id, name '
            'FROM {} '
            'WHERE username=%s AND password=%s '
            'LIMIT 1'
        ).format(self.tableName)
        data = (__username, __password,)
        row = None
        with self.cnx.cursor() as cursor:
            cursor.execute(query, data)
            row = cursor.fetchone()
        if row == None:
            return None
        else:
            (id, name,) = row
            return Member(id, name, __username, __password)

    def __usernameExists(self, __username: str) -> bool:
        query = (
            'SELECT COUNT(*) '
            'FROM {} '
            'WHERE username=%s'
        ).format(self.tableName)
        data = (__username,)
        with self.cnx.cursor() as cursor:
            cursor.execute(query, data)
            (count,) = cursor.fetchone()
            return count > 0

    @property
    def tableName(self) -> str:
        if self.debug:
            return 'test_member'
        else:
            return 'member'

    @property
    def createTableStatement(self) -> str:
        return (
            'CREATE TABLE {} ('
            '    id              bigint        NOT NULL  AUTO_INCREMENT,'
            '    name            varchar(255)  NOT NULL,'
            '    username        varchar(255)  NOT NULL,'
            '    password        varchar(255)  NOT NULL,'
            '    follower_count  int unsigned  NOT NULL  DEFAULT 0,'
            '    time            datetime      NOT NULL  DEFAULT CURRENT_TIMESTAMP,'
            '    PRIMARY KEY (id)'
            ');'
        ).format(self.tableName)

class MySQLMessageRepository(MySQLRepository, MessageRepository):
    def __init__(self, cnx: MySQLConnection, memberTableName: str, debug: bool):
        self.memberTableName = memberTableName
        MySQLRepository.__init__(self, cnx, debug)

    def addMessage(self, __memberId: int, __content: str) -> None:
        pass

    def getMessages(self) -> List[Message]:
        pass

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

class MySQLUnitOfWork(UnitOfWork):
    def __init__(self, configPath: str, debug=False):
        self.__debug = debug
        self.__cnx = self.loadConfigAndConnect(configPath)
        UnitOfWork.__init__(self)

    def __del__(self):
        if self.__debug:
            self.messageRepository.dropTableIfExists()
            self.memberRepository.dropTableIfExists()

    def _createMemberRepository(self) -> MemberRepository:
        return MySQLMemberRepository(self.__cnx, self.__debug)

    def _createMessageRepository(self) -> MessageRepository:
        return MySQLMessageRepository(self.__cnx, self.memberRepository.tableName, self.__debug)

    @staticmethod
    def isAvailable(configPath: str) -> bool:
        try:
            MySQLUnitOfWork.loadConfigAndConnect(configPath)
            return True
        except:
            return False

    @staticmethod
    def loadConfigAndConnect(configPath: str):
        with open(configPath) as file:
            config = json.load(file)
            return mysql.connector.connect(**config)