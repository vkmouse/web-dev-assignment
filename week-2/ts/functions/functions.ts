export function calculate(min: number, max: number, step: number): number {
  let result = 0
  for (let i = min; i < max + 1; i += step) {
    result += i
  }
  console.log(result)
  return result
}

interface Employee {
  name: string
  salary: number
  manager: boolean
}

interface Employees {
  employees: Employee[]
}

export function avg(data: Employees): number {
  let sum = 0
  let count = 0
  for (const employee of data["employees"]) {
    if (!employee["manager"]) {
      sum += employee["salary"]
      count += 1
    }
  }
  const result = sum / count
  console.log(sum / count)
  return sum / count
}

export function func(a: number) {
  function func1(b: number, c: number): number {
    const result = a + (b * c)
    console.log(result)
    return result
  }
  return func1
}

export function maxProduct(nums: number[]): number {
  const n = nums.length
  let maxResult = nums[0] * nums[1]
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      maxResult = Math.max(maxResult, nums[i] * nums[j])
    }
  }
  console.log(maxResult)
  return maxResult
}

export function twoSum(nums: number[], target: number): number[] | undefined {
  let indexByNum = new Map();
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i]
    if (indexByNum.has(target - num)) {
      return [indexByNum.get(target - num), i]
    } else {
      indexByNum.set(num, i)
    }
  }
}

export function maxZeros(nums: number[]) {
  let result = 0
  let currentZeros = 0
  for (const num of nums) {
    if (num === 0) {
      currentZeros += 1
    } else {
      result = Math.max(result, currentZeros)
      currentZeros = 0
    }
  }
  result = Math.max(result, currentZeros)
  console.log(result)
  return result
}

export function printSeparator() {
  console.log("---------------------------------------------------\n")
}
