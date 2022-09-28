package functions

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCalculate(t *testing.T) {
	assert.Equal(t, Calculate(1, 3, 1), 6)
	assert.Equal(t, Calculate(4, 8, 2), 18)
	assert.Equal(t, Calculate(-1, 2, 2), 0)
}

func TestAvg(t *testing.T) {
	var employees Employees = Employees{
		Employees: []Employee{
			{Name: "John", Salary: 30000, Manager: false},
			{Name: "Bob", Salary: 60000, Manager: true},
			{Name: "Jenny", Salary: 50000, Manager: false},
			{Name: "Tony", Salary: 40000, Manager: false},
		},
	}
	assert.Equal(t, Avg(employees), 40000)
}

func TestFunc(t *testing.T) {
	assert.Equal(t, Func(2)(3, 4), 14)
	assert.Equal(t, Func(5)(1, -5), 0)
	assert.Equal(t, Func(-3)(2, 9), 15)
}

func TestMaxProduct(t *testing.T) {
	assert.Equal(t, MaxProduct([]int{5, 20, 2, 6}), 120)
	assert.Equal(t, MaxProduct([]int{10, -20, 0, 3}), 30)
	assert.Equal(t, MaxProduct([]int{10, -20, 0, -3}), 60)
	assert.Equal(t, MaxProduct([]int{-1, 2}), -2)
	assert.Equal(t, MaxProduct([]int{-1, 0, 2}), 0)
	assert.Equal(t, MaxProduct([]int{5, -1, -2, 0}), 2)
	assert.Equal(t, MaxProduct([]int{-5, -2}), 10)
}

func TestTwoSum(t *testing.T) {
	assert.Equal(t, TwoSum([]int{2, 11, 7, 15}, 9), []int{0, 2})
}

func TestMaxZeros(t *testing.T) {
	assert.Equal(t, MaxZeros([]int{0, 1, 0, 0}), 2)
	assert.Equal(t, MaxZeros([]int{1, 0, 0, 0, 0, 1, 0, 1, 0, 0}), 4)
	assert.Equal(t, MaxZeros([]int{1, 1, 1, 1, 1}), 0)
	assert.Equal(t, MaxZeros([]int{0, 0, 0, 1, 1}), 3)
}
