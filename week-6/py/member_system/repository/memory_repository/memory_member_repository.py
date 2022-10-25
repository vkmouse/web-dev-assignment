from typing import List
from member_system.core import Member
from member_system.repository.unit_of_work import MemberRepository

class MemoryMemberRepository(MemberRepository):
    def __init__(self):
        self.__db: List[Member] = []
        self.__id: int = 0

    def addMember(self, __name: str, __username: str, __password: str) -> bool:
        usernameExists = len(list(filter(lambda i: i.username == __username, self.__db))) > 0
        if usernameExists:
            return False
        member = Member(self.__nextId, __name, __username, __password)
        self.__db.append(member)
        return True

    def getMember(self, __username: str, __password: str) -> Member | None:
        members = list(filter(lambda i: i.username == __username and i.password == __password, self.__db))
        if len(members) > 0:
            return members[0]
        else:
            return None

    def getMemberById(self, __id: int) -> Member | None:
        members = list(filter(lambda i: i.id == __id, self.__db))
        if len(members) > 0:
            return members[0]
        else:
            return None

    @property
    def __nextId(self):
        self.__id += 1
        return self.__id
