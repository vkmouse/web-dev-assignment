package functions

import (
	"fmt"
)

func Calculate(min int, max int, step int) int {
	var result int = 0
	var i int
	for i = min; i < max+1; i += step {
		result += i
	}
	fmt.Println(result)
	return result
}

func Avg(employees Employees) int {
	var sum int = 0
	var count int = 0
	for _, employee := range employees.Employees {
		if !employee.Manager {
			sum += employee.Salary
			count += 1
		}
	}
	var result int = sum / count
	fmt.Println(result)
	return result
}

func Func(a int) func(b int, c int) int {
	return func(b int, c int) int {
		var result int = a + b*c
		fmt.Println(result)
		return result
	}
}

func MaxProduct(nums []int) int {
	var result int = nums[0] * nums[1]
	for index, num1 := range nums {
		for _, num2 := range nums[index+1:] {
			result = max(result, num1*num2)
		}
	}
	fmt.Println(result)
	return result
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

func MaxZeros(nums []int) int {
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
	return result
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
