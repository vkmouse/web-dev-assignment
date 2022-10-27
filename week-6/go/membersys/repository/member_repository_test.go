package repository

import (
	. "Project/membersys/core"

	"testing"

	"github.com/stretchr/testify/assert"
)

func memberRepositoryTest(t *testing.T, u *UnitOfWork) {
	assert.Equal(t, GetMember(u.MemberRepository, "test", "test"), Member{Id: -1})
	assert.Equal(t, AddMember(u.MemberRepository, "Tester", "test", "test"), true)
	assert.Equal(t, GetMember(u.MemberRepository, "test", "test"), Member{Id: 1, Name: "Tester", Username: "test", Password: "test"})
	assert.Equal(t, AddMember(u.MemberRepository, "Tester", "test", "test"), false)
}

func TestMemoryMemberRepository(t *testing.T) {
	u := NewMemoryUnitOfWork()
	messageRepositoryTest(t, &u.UnitOfWork)
}
