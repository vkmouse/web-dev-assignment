import json
import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool
from member_system.repository.mysql_repository.mysql_member_repository import MySQLMemberRepository
from member_system.repository.mysql_repository.mysql_message_repository import MySQLMessageRepository
from member_system.repository.unit_of_work import MemberRepository, MessageRepository, UnitOfWork

class MySQLUnitOfWork(UnitOfWork):
    def __init__(self, configPath: str, debug=False):
        self.__debug = debug
        config = self.loadConfig(configPath)
        self.initDb(config)
        self.__cnxpool = MySQLConnectionPool(pool_name='mypool', pool_size=4, **config)
        UnitOfWork.__init__(self)

    def __del__(self):
        if self.__debug:
            self.messageRepository.dropTableIfExists()
            self.memberRepository.dropTableIfExists()

    def _createMemberRepository(self) -> MemberRepository:
        return MySQLMemberRepository(self.__cnxpool, self.__debug)

    def _createMessageRepository(self) -> MessageRepository:
        return MySQLMessageRepository(self.__cnxpool, self.memberRepository.tableName, self.__debug)

    @staticmethod
    def isAvailable(configPath: str) -> bool:
        try:
            config = MySQLUnitOfWork.loadConfig(configPath)
            mysql.connector.connect(**config)
            return True
        except:
            return False

    @staticmethod
    def loadConfig(configPath: str):
        with open(configPath) as file:
            return json.load(file)
    
    @staticmethod
    def initDb(config):
        database = config['database']
        config['database'] = None
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute('SHOW DATABASES;')
        if not (database,) in cursor.fetchall():
            cursor.execute('CREATE DATABASE ' + database)
        cursor.close()
        cnx.close()
        config['database'] = database
