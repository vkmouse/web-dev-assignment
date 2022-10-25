import json
import mysql.connector
from mysql.connector.connection import MySQLConnection
from member_system.core import Member
from member_system.repository.repository import MemberRepository, UnitOfWork

class MySQLMemberRepository(MemberRepository):
    def __init__(self, cnx: MySQLConnection, debug: bool):
        self.debug = debug
        self.cnx = cnx
        self.__createTable()

    def __del__(self):
        if self.debug:
            self.__dropTableIfExists()

    def addMember(self, __name: str, __username: str, __password: str) -> bool:
        if self.__usernameExists(__username):
            return False
        query = (
            'INSERT INTO {} (name, username, password) '
            'VALUES (%s, %s, %s)'
        ).format(self.__tableName)
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
        ).format(self.__tableName)
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

    def __createTable(self):
        with self.cnx.cursor() as cursor:
            if not self.__tableExists():
                cursor.execute(self.__createTableStatement)
            elif self.debug:
                cursor.execute(self.__dropTableStatement)
                cursor.execute(self.__createTableStatement)

    def __dropTableIfExists(self):
        if self.__tableExists():
            with self.cnx.cursor() as cursor:
                cursor.execute(self.__dropTableStatement)

    def __usernameExists(self, __username: str) -> bool:
        query = (
            'SELECT COUNT(*) '
            'FROM {} '
            'WHERE username=%s'
        ).format(self.__tableName)
        data = (__username,)
        with self.cnx.cursor() as cursor:
            cursor.execute(query, data)
            (count,) = cursor.fetchone()
            return count > 0

    def __tableExists(self) -> bool:
        with self.cnx.cursor() as cursor:
            cursor.execute('SHOW TABLES;')
            isExists = (self.__tableName,) in cursor.fetchall()
            return isExists

    @property
    def __tableName(self) -> str:
        if self.debug:
            return 'test_member'
        else:
            return 'member'

    @property
    def __createTableStatement(self) -> str:
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
        ).format(self.__tableName)

    @property
    def __dropTableStatement(self) -> str:
        return 'DROP TABLE {};'.format(self.__tableName)

class MySQLUnitOfWork(UnitOfWork):
    def __init__(self, configPath: str, debug=False):
        self.__debug = debug
        self.__cnx = self.loadConfigAndConnect(configPath)
        UnitOfWork.__init__(self)

    def _createMemberRepository(self) -> MemberRepository:
        return MySQLMemberRepository(self.__cnx, self.__debug)

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