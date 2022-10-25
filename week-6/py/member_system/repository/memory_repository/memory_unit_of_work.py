from member_system.repository.unit_of_work import MemberRepository, MessageRepository, UnitOfWork
from member_system.repository.memory_repository.memory_member_repository import MemoryMemberRepository
from member_system.repository.memory_repository.memory_message_repository import MemoryMessageRepository

class MemoryUnitOfWork(UnitOfWork):
    def _createMemberRepository(self) -> MemberRepository:
        return MemoryMemberRepository()
    
    def _createMessageRepository(self) -> MessageRepository:
        return MemoryMessageRepository(self.memberRepository)
