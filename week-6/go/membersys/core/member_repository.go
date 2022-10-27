package core

type MemberRepository interface {
	AddMember(name string, username string, password string) bool
	GetMember(username string, password string) Member
}

func AddMessage(r MessageRepository, memberId int, content string) {
	r.AddMessage(memberId, content)
}

func GetMessages(r MessageRepository) []Message {
	return r.GetMessages()
}
