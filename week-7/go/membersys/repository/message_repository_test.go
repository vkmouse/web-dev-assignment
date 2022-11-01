package repository

import (
	. "Project/membersys/core"
	. "Project/membersys/repository/memory_repository"
	. "Project/membersys/repository/mysql_repository"

	"testing"

	"github.com/stretchr/testify/assert"
)

func messageRepositoryTest(t *testing.T, u *UnitOfWork) {
	u.MemberRepository.AddMember("name1", "1", "1")
	u.MemberRepository.AddMember("name2", "2", "2")
	u.MessageRepository.AddMessage(1, "123")
	u.MessageRepository.AddMessage(2, "456")
	u.MessageRepository.AddMessage(1, "789")
	messages := u.MessageRepository.GetMessages()
	assert.Equal(t, messages[0], Message{Name: "name1", Content: "123"})
	assert.Equal(t, messages[1], Message{Name: "name2", Content: "456"})
	assert.Equal(t, messages[2], Message{Name: "name1", Content: "789"})
}

func TestMemoryMessageRepository(t *testing.T) {
	u := NewMemoryUnitOfWork()
	messageRepositoryTest(t, &u.UnitOfWork)
}

func TestMySQLMessageRepository(t *testing.T) {
	u := NewMySQLUnitOfWork("../../config.json", true)
	messageRepositoryTest(t, &u.UnitOfWork)
}
