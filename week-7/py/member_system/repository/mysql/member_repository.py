from member_system.core import Member
from member_system.core import MemberRepository
from member_system.repository.mysql.repository import MySQLRepository

class MySQLMemberRepository(MySQLRepository, MemberRepository):
    @MySQLRepository.withConnection
    def addMember(self, __name: str, __username: str, __password: str, cnx, cursor) -> bool:
        if self.__usernameExists(__username):
            return False
        query = 'INSERT INTO {} (name, username, password) VALUES (%s, %s, %s)'.format(self.tableName)
        data = (__name, __username, __password,)
        cursor.execute(query, data)
        cnx.commit()
        return True

    @MySQLRepository.withConnection
    def getMember(self, __username: str, __password: str, cnx, cursor) -> Member | None:
        query = 'SELECT id, name FROM {} WHERE username=%s AND password=%s LIMIT 1'.format(self.tableName)
        data = (__username, __password,)
        cursor.execute(query, data)
        row = cursor.fetchone()
        if row == None:
            return None
        else:
            (id, name,) = row
            return Member(id, name, __username, __password)

    @MySQLRepository.withConnection
    def getMemberByUsername(self, __username: str, cnx, cursor) -> Member | None:
        query = 'SELECT id, name FROM {} WHERE username=%s LIMIT 1'.format(self.tableName)
        data = (__username,)
        cursor.execute(query, data)
        row = cursor.fetchone()
        if row == None:
            return None
        else:
            (id, name,) = row
            return Member(id, name, __username, None)

    @MySQLRepository.withConnection
    def updateNameById(self, __id: int, __newName: str, cnx, cursor) -> bool:
        if not self.__idExists(__id):
            return False
        query = 'UPDATE {} SET name=%s WHERE id=%s'.format(self.tableName)
        data = (__newName, __id)
        cursor.execute(query, data)
        cnx.commit()
        return True

    @MySQLRepository.withConnection
    def __usernameExists(self, __username: str, cnx, cursor) -> bool:
        query = 'SELECT COUNT(*) FROM {} WHERE username=%s'.format(self.tableName)
        data = (__username,)
        cursor.execute(query, data)
        (count,) = cursor.fetchone()
        return count > 0

    @MySQLRepository.withConnection
    def __idExists(self, __id: int, cnx, cursor) -> bool:
        query = 'SELECT COUNT(*) FROM {} WHERE id=%s'.format(self.tableName)
        data = (__id,)
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
