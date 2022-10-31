import pytest
from member_system.repository import UnitOfWork, MemoryUnitOfWork, MySQLUnitOfWork

def memberRepositoryTest(unitOfWork: UnitOfWork):
    assert unitOfWork.memberRepository.getMember('test', 'test') == None
    assert unitOfWork.memberRepository.getMemberByUsername('test') == None
    assert unitOfWork.memberRepository.addMember('Tester', 'test', 'test') == True
    assert unitOfWork.memberRepository.getMember('test', 'test') != None
    assert unitOfWork.memberRepository.getMemberByUsername('test') != None
    assert unitOfWork.memberRepository.addMember('Tester', 'test', 'test') == False
    assert unitOfWork.memberRepository.updateNameById(1, 'test123') == True
    assert unitOfWork.memberRepository.updateNameById(2, 'test123') == False

def messageRepositoryTest(unitOfWork: UnitOfWork):
    unitOfWork.memberRepository.addMember('name1', '1', '1')
    unitOfWork.memberRepository.addMember('name2', '2', '2')
    unitOfWork.messageRepository.addMessage(1, '123')
    unitOfWork.messageRepository.addMessage(2, '456')
    unitOfWork.messageRepository.addMessage(1, '789')
    messages = unitOfWork.messageRepository.getMessages()
    assert messages[0].name == 'name1'
    assert messages[1].name == 'name2'
    assert messages[2].name == 'name1'
    assert messages[0].content == '123'
    assert messages[1].content == '456'
    assert messages[2].content == '789'

def testMemoryMemberRepository():
    unitOfWork = MemoryUnitOfWork()
    memberRepositoryTest(unitOfWork)

@pytest.mark.skipif(not MySQLUnitOfWork.isAvailable('config.json'), reason="database is not avaibable")
def testMySQLMemberRepository():
    unitOfWork = MySQLUnitOfWork('config.json', debug=True)
    memberRepositoryTest(unitOfWork)

def testMemoryMessageRepository():
    unitOfWork = MemoryUnitOfWork()
    messageRepositoryTest(unitOfWork)

@pytest.mark.skipif(not MySQLUnitOfWork.isAvailable('config.json'), reason="database is not avaibable")
def testMySQLMessageRepository():
    unitOfWork = MySQLUnitOfWork('config.json', debug=True)
    messageRepositoryTest(unitOfWork)