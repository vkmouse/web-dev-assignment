import json
import mysql.connector

from member_system.core import MemberRepository
from member_system.core import MessageRepository
from member_system.core import UnitOfWork
from member_system.repository.mysql.member_repository import MySQLMemberRepository
from member_system.repository.mysql.message_repository import MySQLMessageRepository

class MySQLUnitOfWork(UnitOfWork):
    def __init__(self, configPath: str, debug=False):
        self.__debug = debug
        config = self.loadConfig(configPath)
        self.__cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name='mypool', pool_size=4, **config)
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