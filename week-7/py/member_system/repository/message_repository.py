from typing import List
from member_system.core import Message

class MessageRepository:
    def addMessage(self, __memberId: int, __content: str) -> None:
        return NotImplemented
    
    def getMessages(self) -> List[Message]:
        return NotImplemented