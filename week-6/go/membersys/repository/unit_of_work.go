package repository

type UnitOfWork struct {
	MemberRepository  MemberRepository
	MessageRepository MessageRepository
}

func (unitOfWork *UnitOfWork) init() {
}

type UnitOfWorkFactory interface {
	init()
}

func InitUnitOfWork(factory UnitOfWorkFactory) {
	factory.init()
}
