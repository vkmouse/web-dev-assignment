package repository

import (
	. "Project/membersys/core"
)

type MemoryMessageRepository struct {
	memberRepository *MemoryMemberRepository
	db               []Message
}

func (r *MemoryMessageRepository) AddMessage(memberId int, content string) {
	member := r.memberRepository.GetMemberById(memberId)
	r.db = append(r.db, Message{Name: member.Name, Content: content})
}

func (r *MemoryMessageRepository) GetMessages() []Message {
	return r.db
}
