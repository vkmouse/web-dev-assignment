package repository

import (
	. "Project/membersys/core"
)

type MemoryMemberRepository struct {
	db []Member
	id int
}

func (r *MemoryMemberRepository) AddMember(name string, username string, password string) bool {
	if r.memberExists(username) {
		return false
	}
	member := Member{Id: r.nextId(), Name: name, Username: username, Password: password}
	r.db = append(r.db, member)
	return true
}

func (r *MemoryMemberRepository) GetMember(username string, password string) Member {
	member := Member{Id: -1}
	for _, data := range r.db {
		if data.Username == username && data.Password == password {
			member = data
		}
	}
	return member
}

func (r *MemoryMemberRepository) GetMemberById(id int) Member {
	member := Member{Id: -1}
	for _, data := range r.db {
		if data.Id == id {
			member = data
		}
	}
	return member
}

func (r *MemoryMemberRepository) memberExists(username string) bool {
	for _, data := range r.db {
		if data.Username == username {
			return true
		}
	}
	return false
}

func (r *MemoryMemberRepository) nextId() int {
	r.id++
	return r.id
}
