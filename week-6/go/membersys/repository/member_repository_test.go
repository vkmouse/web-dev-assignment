package repository

import (
	. "Project/membersys/core"

	"testing"

	"github.com/stretchr/testify/assert"
)

func memberRepositoryTest(t *testing.T, u *UnitOfWork) {
	assert.Equal(t, u.MemberRepository.GetMember("test", "test"), Member{Id: -1})
	assert.Equal(t, u.MemberRepository.AddMember("Tester", "test", "test"), true)
	assert.Equal(t, u.MemberRepository.GetMember("test", "test"), Member{Id: 1, Name: "Tester", Username: "test", Password: "test"})
	assert.Equal(t, u.MemberRepository.AddMember("Tester", "test", "test"), false)
}

func TestMemoryMemberRepository(t *testing.T) {
	u := NewMemoryUnitOfWork()
	messageRepositoryTest(t, &u.UnitOfWork)
}
