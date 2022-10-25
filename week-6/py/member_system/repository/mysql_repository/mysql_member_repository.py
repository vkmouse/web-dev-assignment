from member_system.core import Member
from member_system.repository.mysql_repository.mysql_repository import MySQLRepository
from member_system.repository.unit_of_work import MemberRepository

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
