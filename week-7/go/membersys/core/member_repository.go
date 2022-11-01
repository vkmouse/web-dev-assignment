package core

type MemberRepository interface {
	AddMember(name string, username string, password string) bool
	GetMember(username string, password string) Member
}
