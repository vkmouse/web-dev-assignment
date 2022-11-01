from member_system.core.types import List
from member_system.core.types import Message

class MessageRepository:
    def addMessage(self, __memberId: int, __content: str) -> None:
        return NotImplemented
    
    def getMessages(self) -> List[Message]:
        return NotImplemented