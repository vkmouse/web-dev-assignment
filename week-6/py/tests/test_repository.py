from repository import MemberRepository, MemoryMemberRepository

def repositoryTest(repo: MemberRepository):
    assert repo.usernameExists('test') == False
    assert repo.getName('test') == ''
    assert repo.addUser('Tester', 'test', 'test') == True
    assert repo.usernameExists('test') == True
    assert repo.getName('test') == 'Tester'
    assert repo.addUser('Tester', 'test', 'test') == False

def testMemoryMemberRepository():
    repo = MemoryMemberRepository()
    repositoryTest(repo)