from repository.repository import MemberRepository
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

    def getName(self, __username: str) -> str:
        temp = list(filter(lambda i: i['username'] == __username, self.__db))
        if len(temp) > 0:
            return temp[0]['name']
        return ''
