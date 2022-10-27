package repository

type MemoryUnitOfWork struct {
	UnitOfWork
}

func (u *MemoryUnitOfWork) init() {
	memberRepository := MemoryMemberRepository{}
	u.MemberRepository = &memberRepository
	u.MessageRepository = &MemoryMessageRepository{memberRepository: &memberRepository}
}

func NewMemoryUnitOfWork() *MemoryUnitOfWork {
	unitOfWork := MemoryUnitOfWork{}
	InitUnitOfWork(&unitOfWork)
	return &unitOfWork
}
