from member_system.core.types import Message
from member_system.repository import UnitOfWork, MemoryUnitOfWork, MySQLUnitOfWork

def repositoryTest(unitOfWork: UnitOfWork):
    assert unitOfWork.memberRepository.getMember('test', 'test') == None
    assert unitOfWork.memberRepository.addMember('Tester', 'test', 'test') == True
    assert unitOfWork.memberRepository.getMember('test', 'test') != None
    assert unitOfWork.memberRepository.addMember('Tester', 'test', 'test') == False

def messageRepositoryTest(unitOfWork: UnitOfWork):
    unitOfWork.memberRepository.addMember('name1', '1', '1')
    unitOfWork.memberRepository.addMember('name2', '2', '2')
    unitOfWork.messageRepository.addMessage(1, '123')
    unitOfWork.messageRepository.addMessage(2, '456')
    unitOfWork.messageRepository.addMessage(1, '789')
    messages = unitOfWork.messageRepository.getMessages()
    assert messages[0].name is 'name1'
    assert messages[1].name is 'name2'
    assert messages[2].name is 'name1'
    assert messages[0].content is '123'
    assert messages[1].content is '456'
    assert messages[2].content is '789'

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
