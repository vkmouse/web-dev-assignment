from member_system.core import Member

class MemberRepository:
    def addMember(self, __name: str, __username: str, __password: str) -> bool:
        return NotImplemented

    def getMember(self, __username: str, __password: str) -> Member | None:
        return NotImplemented

    def getMemberByUsername(self, __username: str) -> Member | None:
        return NotImplemented

    def updateNameById(self, __id: int, __newName: str) -> bool:
        return NotImplemented
