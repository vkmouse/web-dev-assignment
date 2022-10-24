class MemberRepository:
    def addUser(self, __name: str, __username: str, __password: str) -> bool:
        return NotImplemented

    def usernameExists(self, __username: str) -> bool:
        return NotImplemented

    def getName(self, __username: str) -> str:
        return NotImplemented
