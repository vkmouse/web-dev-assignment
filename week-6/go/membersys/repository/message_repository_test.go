package repository

import (
	. "Project/membersys/core"

	"testing"

	"github.com/stretchr/testify/assert"
)

func messageRepositoryTest(t *testing.T, u *UnitOfWork) {
	AddMember(u.MemberRepository, "name1", "1", "1")
	AddMember(u.MemberRepository, "name2", "2", "2")
	AddMessage(u.MessageRepository, 1, "123")
	AddMessage(u.MessageRepository, 2, "456")
	AddMessage(u.MessageRepository, 1, "789")
	messages := GetMessages(u.MessageRepository)
	assert.Equal(t, messages[0], Message{Name: "name1", Content: "123"})
	assert.Equal(t, messages[1], Message{Name: "name2", Content: "456"})
	assert.Equal(t, messages[2], Message{Name: "name1", Content: "789"})
}

func TestMemoryMessageRepository(t *testing.T) {
	u := NewMemoryUnitOfWork()
	messageRepositoryTest(t, &u.UnitOfWork)
}
