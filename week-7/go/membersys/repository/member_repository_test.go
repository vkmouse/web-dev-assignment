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
	assert.Equal(t, m.GetMember("test", "test"), Member{Id: -1})
	assert.Equal(t, m.AddMember("Tester", "test", "test"), true)
	assert.Equal(t, m.GetMember("test", "test"), Member{Id: 1, Name: "Tester", Username: "test", Password: "test"})
	assert.Equal(t, m.AddMember("Tester", "test", "test"), false)
}

func TestMemoryMemberRepository(t *testing.T) {
	u := NewMemoryUnitOfWork()
	memberRepositoryTest(t, &u.UnitOfWork)
}

func TestMySQLMemberRepository(t *testing.T) {
	u := NewMySQLUnitOfWork("../../config.json", true)
	memberRepositoryTest(t, &u.UnitOfWork)
}
