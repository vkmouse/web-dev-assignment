from member_system.repository.repository import MemberRepository, UnitOfWork

class MemoryMemberRepository(MemberRepository):
    def __init__(self):
        self.__db = []

    def addUser(self, __name: str, __username: str, __password: str) -> bool:
        if self.usernameExists(__username):
            return False
        self.__db.append({
            'name': __name,
            'username': __username,
            'password': __password,
        })
        return True

    def usernameExists(self, __username: str) -> bool:
        return len(list(filter(lambda i: i['username'] == __username, self.__db))) > 0

    def memberExists(self, __username: str, __password: str) -> str:
        temp = list(filter(lambda i: i['username'] == __username and i['password'] == __password, self.__db))
        return len(temp) > 0

class MemoryUnitOfWork(UnitOfWork):
    def _createMemberRepository(self) -> MemberRepository:
        return MemoryMemberRepository()