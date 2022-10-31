package core

type MessageRepository interface {
	AddMessage(memberId int, content string)
	GetMessages() []Message
}

func AddMember(r MemberRepository, name string, username string, password string) bool {
	return r.AddMember(name, username, password)
}

func GetMember(r MemberRepository, username string, password string) Member {
	return r.GetMember(username, password)
}
