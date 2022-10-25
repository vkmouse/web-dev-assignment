from member_system.repository import UnitOfWork, MemoryUnitOfWork
from member_system.repository.mysql_repository import MySQLUnitOfWork

def repositoryTest(unitOfWork: UnitOfWork):
    assert unitOfWork.memberRepository.getMember('test', 'test') == None
    assert unitOfWork.memberRepository.addMember('Tester', 'test', 'test') == True
    assert unitOfWork.memberRepository.getMember('test', 'test') != None
    assert unitOfWork.memberRepository.addMember('Tester', 'test', 'test') == False

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