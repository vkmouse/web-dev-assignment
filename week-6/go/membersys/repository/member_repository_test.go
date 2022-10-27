package repository

import (
	. "Project/membersys/core"

	"testing"

	"github.com/stretchr/testify/assert"
)

func memberRepositoryTest(t *testing.T, r MemberRepository) {
	assert.Equal(t, GetMember(r, "test", "test"), Member{Id: -1})
	assert.Equal(t, AddMember(r, "Tester", "test", "test"), true)
	assert.Equal(t, GetMember(r, "test", "test"), Member{Id: 1, Name: "Tester", Username: "test", Password: "test"})
	assert.Equal(t, AddMember(r, "Tester", "test", "test"), false)
}

func TestMemoryMemberRepository(t *testing.T) {
	repo := MemoryMemberRepository{}
	memberRepositoryTest(t, &repo)
}
