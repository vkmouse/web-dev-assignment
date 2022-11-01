from member_system.core import List
from member_system.core import Message
from member_system.core import MessageRepository
from member_system.repository.memory.member_repository import MemoryMemberRepository

class MemoryMessageRepository(MessageRepository):
    def __init__(self, memberRepository: MemoryMemberRepository):
        self.memberRepository = memberRepository
        self.__db: List[Message] = []

    def addMessage(self, __memberId: int, __content: str) -> None:
        member = self.memberRepository.getMemberById(__memberId)
        self.__db.append(Message(member.name, __content))
    
    def getMessages(self) -> List[Message]:
        return self.__db
