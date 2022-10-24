from member_system.repository import UnitOfWork, MemoryUnitOfWork

def repositoryTest(unitOfWork: UnitOfWork):
    assert unitOfWork.memberRepository.usernameExists('test') == False
    assert unitOfWork.memberRepository.getMember('test', 'test') == None
    assert unitOfWork.memberRepository.addUser('Tester', 'test', 'test') == True
    assert unitOfWork.memberRepository.usernameExists('test') == True
    assert unitOfWork.memberRepository.getMember('test', 'test') != None
    assert unitOfWork.memberRepository.addUser('Tester', 'test', 'test') == False

def testMemoryMemberRepository():
    unitOfWork = MemoryUnitOfWork()
    repositoryTest(unitOfWork)
