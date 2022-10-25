from member_system.repository.member_repository import MemberRepository
from member_system.repository.message_repository import MessageRepository

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
