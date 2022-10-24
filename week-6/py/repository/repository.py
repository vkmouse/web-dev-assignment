class MemberRepository:
    def addUser(self, __name: str, __username: str, __password: str) -> bool:
        return NotImplemented

    def usernameExists(self, __username: str) -> bool:
        return NotImplemented

    def getName(self, __username: str, __password: str) -> str:
        return NotImplemented

class UnitOfWork:
    def __init__(self):
        self.__memberRepository = self._createMemberRepository()

    @property
    def memberRepository(self):
        return self.__memberRepository

    def _createMemberRepository(self) -> MemberRepository:
        return NotImplemented
