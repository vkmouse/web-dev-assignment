package core

type UnitOfWork struct {
	MemberRepository  MemberRepository
	MessageRepository MessageRepository
}

func (unitOfWork *UnitOfWork) Init() {
}

type UnitOfWorkFactory interface {
	Init()
}

func InitUnitOfWork(factory UnitOfWorkFactory) {
	factory.Init()
}
