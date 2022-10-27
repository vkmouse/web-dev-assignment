package repository

import (
	. "Project/membersys/core"
)

type MemberRepository interface {
	AddMember(name string, username string, password string) bool
	GetMember(username string, password string) Member
}

func AddMember(r MemberRepository, name string, username string, password string) bool {
	return r.AddMember(name, username, password)
}

func GetMember(r MemberRepository, username string, password string) Member {
	return r.GetMember(username, password)
}
