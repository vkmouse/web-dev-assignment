package repository

import (
	. "Project/membersys/core"

	"testing"

	"github.com/stretchr/testify/assert"
)

func messageRepositoryTest(t *testing.T, memberRepository MemberRepository, messageRepository MessageRepository) {
	memberRepository.AddMember("name1", "1", "1")
	memberRepository.AddMember("name2", "2", "2")
	messageRepository.AddMessage(1, "123")
	messageRepository.AddMessage(2, "456")
	messageRepository.AddMessage(1, "789")
	messages := messageRepository.GetMessages()
	assert.Equal(t, messages[0], Message{Name: "name1", Content: "123"})
	assert.Equal(t, messages[1], Message{Name: "name2", Content: "456"})
	assert.Equal(t, messages[2], Message{Name: "name1", Content: "789"})
}

func TestMemoryMessageRepository(t *testing.T) {
	memberRepository := MemoryMemberRepository{}
	messageRepository := MemoryMessageRepository{memberRepository: &memberRepository}
	messageRepositoryTest(t, &memberRepository, &messageRepository)
}
