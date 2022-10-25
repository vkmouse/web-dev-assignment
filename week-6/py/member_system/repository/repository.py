from typing import List
from member_system.core import Member, Message

class MemberRepository:
    def addMember(self, __name: str, __username: str, __password: str) -> bool:
        return NotImplemented

    def getMember(self, __username: str, __password: str) -> Member | None:
        return NotImplemented

class MessageRepository:
    def addMessage(self, __memberId: int, __content: str) -> None:
        return NotImplemented
    
    def getMessages(self) -> List[Message]:
        return NotImplemented

class UnitOfWork:
    def __init__(self):
        self.__memberRepository = self._createMemberRepository()
        self.__messageRepository = self._createMessageRepository()

    @property
    def memberRepository(self):
        return self.__memberRepository

    @property
    def messageRepository(self):
        return self.__messageRepository

    def _createMemberRepository(self) -> MemberRepository:
        return NotImplemented

    def _createMessageRepository(self) -> MessageRepository:
        return NotImplemented
