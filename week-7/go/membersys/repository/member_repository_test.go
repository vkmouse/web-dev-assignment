package repository

import (
	. "Project/membersys/core"
	. "Project/membersys/repository/memory_repository"
	. "Project/membersys/repository/mysql_repository"

	"testing"

	"github.com/stretchr/testify/assert"
)

func memberRepositoryTest(t *testing.T, u *UnitOfWork) {
	m := u.MemberRepository
	emptyMember := Member{Id: -1}
	testMember := Member{Id: 1, Name: "Tester", Username: "test", Password: "test"}
	assert.Equal(t, emptyMember, m.GetMember("test", "test"))
	assert.Equal(t, emptyMember, m.GetMemberByUsername("test"))
	assert.Equal(t, true, m.AddMember("Tester", "test", "test"))
	assert.Equal(t, testMember, m.GetMember("test", "test"))
	assert.Equal(t, testMember, m.GetMemberByUsername("test"))
	assert.Equal(t, false, m.AddMember("Tester", "test", "test"))
	assert.Equal(t, true, m.UpdateNameById(1, "test123"))
	assert.Equal(t, false, m.UpdateNameById(2, "test123"))
}

func TestMemoryMemberRepository(t *testing.T) {
	u := NewMemoryUnitOfWork()
	memberRepositoryTest(t, &u.UnitOfWork)
}

func TestMySQLMemberRepository(t *testing.T) {
	u := NewMySQLUnitOfWork("../../config.json", true)
	memberRepositoryTest(t, &u.UnitOfWork)
}
