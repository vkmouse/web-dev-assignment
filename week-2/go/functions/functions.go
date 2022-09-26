package functions

import (
	"fmt"
)

func Calculate(min int, max int, step int) {
	var result int = 0
	var i int
	for i = min; i < max+1; i += step {
		result += i
	}
	fmt.Println(result)
}

func Avg(employees Employees) {
	var sum int = 0
	var count int = 0
	for _, employee := range employees.Employees {
		if !employee.Manager {
			sum += employee.Salary
			count += 1
		}
	}
	fmt.Println(sum / count)
}

func Func(a int) func(b int, c int) {
	return func(b int, c int) {
		fmt.Println(a + b*c)
	}
}

func MaxProduct(nums []int) {
	var result int = nums[0] * nums[1]
	for index, num1 := range nums {
		for _, num2 := range nums[index+1:] {
			result = max(result, num1*num2)
		}
	}
	fmt.Println(result)
}

func TwoSum(nums []int, target int) []int {
	var indexByNum = make(map[int]int)
	for i, num := range nums {
		index, isExisted := indexByNum[target-num]
		if isExisted {
			return []int{index, i}
		} else {
			indexByNum[num] = i
		}
	}
	return []int{}
}

func MaxZeros(nums []int) {
	var result int = 0
	var current int = 0
	for _, num := range nums {
		if num == 0 {
			current++
		} else {
			result = max(result, current)
			current = 0
		}
	}
	result = max(result, current)
	fmt.Println(result)
}

func PrintSeperator() {
	fmt.Println("-------------------------------------------")
}

func max(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}
