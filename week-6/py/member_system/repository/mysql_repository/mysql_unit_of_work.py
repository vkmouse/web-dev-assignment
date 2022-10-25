import json
import mysql.connector
from member_system.repository.mysql_repository.mysql_member_repository import MySQLMemberRepository
from member_system.repository.mysql_repository.mysql_message_repository import MySQLMessageRepository
from member_system.repository.unit_of_work import MemberRepository, MessageRepository, UnitOfWork

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