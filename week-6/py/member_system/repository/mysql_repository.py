import mysql.connector
from member_system.core import Member
from member_system.repository.repository import MemberRepository, UnitOfWork

class MySQLMemberRepository(MemberRepository):
    def __init__(self, config):
        self.cnx = mysql.connector.connect(**config)
        self.cursor = self.cnx.cursor()

    def addMember(self, __name: str, __username: str, __password: str) -> bool:
        if self.__usernameExists(__username):
            return False
        query = (
            'INSERT INTO member (name, username, password) '
            'VALUES (%s, %s, %s)')
        data = (__name, __username, __password,)
        self.cursor.execute(query, data)
        self.cnx.commit()
        return True

    def getMember(self, __username: str, __password: str) -> Member | None:
        query = (
            'SELECT id, name '
            'FROM member '
            'WHERE username=%s AND password=%s')
        data = (__username, __password,)
        self.cursor.execute(query, data)
        row = self.cursor.fetchone()
        if row == None:
            return None
        else:
            (id, name,) = row
            return Member(id, name, __username, __password)

    def __usernameExists(self, __username: str):
        query = (
            'SELECT COUNT(*) '
            'FROM member '
            'WHERE username=%s')
        data = (__username,)
        self.cursor.execute(query, data)
        [(count,)] = self.cursor.fetchall()
        return count > 0

class MySQLUnitOfWork(UnitOfWork):
    def __init__(self, config):
        self.__config = config
        UnitOfWork.__init__(self)

    def _createMemberRepository(self) -> MemberRepository:
        return MySQLMemberRepository(self.__config)