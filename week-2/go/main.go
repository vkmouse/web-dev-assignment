package main

import (
	. "assignment2/functions"
	"fmt"
)

func main() {
	Calculate(1, 3, 1)
	Calculate(4, 8, 2)
	Calculate(-1, 2, 2)
	PrintSeperator()

	var employees Employees = Employees{
		Employees: []Employee{
			{Name: "John", Salary: 30000, Manager: false},
			{Name: "Bob", Salary: 60000, Manager: true},
			{Name: "Jenny", Salary: 50000, Manager: false},
			{Name: "Tony", Salary: 40000, Manager: false},
		},
	}
	Avg(employees)
	PrintSeperator()

	Func(2)(3, 4)
	Func(5)(1, -5)
	Func(-3)(2, 9)
	PrintSeperator()

	MaxProduct([]int{5, 20, 2, 6})
	MaxProduct([]int{10, -20, 0, 3})
	MaxProduct([]int{10, -20, 0, -3})
	MaxProduct([]int{-1, 2})
	MaxProduct([]int{-1, 0, 2})
	MaxProduct([]int{5, -1, -2, 0})
	MaxProduct([]int{-5, -2})
	PrintSeperator()

	var result []int = TwoSum([]int{2, 11, 7, 15}, 9)
	fmt.Println(result)
	PrintSeperator()

	MaxZeros([]int{0, 1, 0, 0})
	MaxZeros([]int{1, 0, 0, 0, 0, 1, 0, 1, 0, 0})
	MaxZeros([]int{1, 1, 1, 1, 1})
	MaxZeros([]int{0, 0, 0, 1, 1})
}
