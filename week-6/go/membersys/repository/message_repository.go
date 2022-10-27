package repository

import (
	. "Project/membersys/core"
)

type MessageRepository interface {
	AddMessage(memberId int, content string)
	GetMessages() []Message
}

func AddMessage(r MessageRepository, memberId int, content string) {
	r.AddMessage(memberId, content)
}

func GetMessages(r MessageRepository) []Message {
	return r.GetMessages()
}
