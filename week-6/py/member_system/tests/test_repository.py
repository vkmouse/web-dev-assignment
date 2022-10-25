from member_system.core.types import Message
from member_system.repository import UnitOfWork, MemoryUnitOfWork, MySQLUnitOfWork

def repositoryTest(unitOfWork: UnitOfWork):
    assert unitOfWork.memberRepository.getMember('test', 'test') == None
    assert unitOfWork.memberRepository.addMember('Tester', 'test', 'test') == True
    assert unitOfWork.memberRepository.getMember('test', 'test') != None
    assert unitOfWork.memberRepository.addMember('Tester', 'test', 'test') == False

def messageRepositoryTest(unitOfWork: UnitOfWork):
    unitOfWork.memberRepository.addMember('1', '1', '1')
    unitOfWork.memberRepository.addMember('2', '2', '2')
    unitOfWork.messageRepository.addMessage(1, '123')
    unitOfWork.messageRepository.addMessage(2, '456')
    unitOfWork.messageRepository.addMessage(1, '789')
    assert unitOfWork.messageRepository.getMessages() == [
        { Message(1, '123', 1) },
        { Message(2, '456', 2) },
        { Message(3, '789', 1) },
    ]

def testMemoryMemberRepository():
    unitOfWork = MemoryUnitOfWork()
    repositoryTest(unitOfWork)

def testMySQLMemberRepository():
    unitOfWork = MySQLUnitOfWork({
        'user': 'root',
        'password': '12345678',
        'host': '192.168.56.102',
        'database': 'website',
        'raise_on_warnings': True
    }, debug=True)
    repositoryTest(unitOfWork)

def testMemoryMessageRepository():
    unitOfWork = MemoryUnitOfWork()
    messageRepositoryTest(unitOfWork)
