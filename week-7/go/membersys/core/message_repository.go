package core

type MessageRepository interface {
	AddMessage(memberId int, content string)
	GetMessages() []Message
}
