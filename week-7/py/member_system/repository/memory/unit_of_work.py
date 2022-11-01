from member_system.core import MemberRepository
from member_system.core import MessageRepository
from member_system.core import UnitOfWork
from member_system.repository.memory.member_repository import MemoryMemberRepository
from member_system.repository.memory.message_repository import MemoryMessageRepository

class MemoryUnitOfWork(UnitOfWork):
    def _createMemberRepository(self) -> MemberRepository:
        return MemoryMemberRepository()
    
    def _createMessageRepository(self) -> MessageRepository:
        return MemoryMessageRepository(self.memberRepository)
