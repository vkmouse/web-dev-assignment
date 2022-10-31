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
        with self.cnxpool.get_connection() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute(query, data)
            cnx.commit()
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
        with self.cnxpool.get_connection() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute(query, data)
                row = cursor.fetchone()
            if row == None:
                return None
            else:
                (id, name,) = row
                return Member(id, name, __username, __password)

    def getMemberByUsername(self, __username: str) -> Member | None:
        query = (
            'SELECT id, name '
            'FROM {} '
            'WHERE username=%s '
            'LIMIT 1'
        ).format(self.tableName)
        data = (__username,)
        row = None
        with self.cnxpool.get_connection() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute(query, data)
                row = cursor.fetchone()
            if row == None:
                return None
            else:
                (id, name,) = row
                return Member(id, name, __username, None)

    def updateNameById(self, __id: int, __newName: str) -> bool:
        if not self.__idExists(__id):
            return False
        query = (
            'UPDATE {} '
            'SET name=%s '
            'WHERE id=%s '
        ).format(self.tableName)
        data = (__newName, __id)
        with self.cnxpool.get_connection() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute(query, data)
                cnx.commit()
                return True

    def __usernameExists(self, __username: str) -> bool:
        query = (
            'SELECT COUNT(*) '
            'FROM {} '
            'WHERE username=%s'
        ).format(self.tableName)
        data = (__username,)
        with self.cnxpool.get_connection() as cnx:
            with cnx.cursor() as cursor:
                cursor.execute(query, data)
                (count,) = cursor.fetchone()
                return count > 0

    def __idExists(self, __id: int) -> bool:
        query = (
            'SELECT COUNT(*) '
            'FROM {} '
            'WHERE id=%s'
        ).format(self.tableName)
        data = (__id,)
        with self.cnxpool.get_connection() as cnx:
            with cnx.cursor() as cursor:
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
