package memory_repository

import (
	. "Project/membersys/core"
)

type MemoryUnitOfWork struct {
	UnitOfWork
}

func (u *MemoryUnitOfWork) Init() {
	memberRepository := MemoryMemberRepository{}
	u.MemberRepository = &memberRepository
	u.MessageRepository = &MemoryMessageRepository{memberRepository: &memberRepository}
}

func NewMemoryUnitOfWork() *MemoryUnitOfWork {
	unitOfWork := MemoryUnitOfWork{}
	InitUnitOfWork(&unitOfWork)
	return &unitOfWork
}
