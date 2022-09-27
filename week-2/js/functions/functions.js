export function calculate(min, max, step) {
  let result = 0
  for (let i = min; i < max + 1; i += step) {
    result += i
  }
  console.log(result)
  return result
}

export function avg(data) {
  let sum = 0
  let count = 0
  for (const employee of data["employees"]) {
    if (!employee["manager"]) {
      sum += employee["salary"]
      count += 1
    }
  }
  console.log(sum / count)
}

export function func(a) {
  let result = a
  function func1(b, c) {
    console.log(result + (b * c))
  }
  return func1
}

export function maxProduct(nums) {
  const n = nums.length
  let maxResult = nums[0] * nums[1]
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      maxResult = Math.max(maxResult, nums[i] * nums[j])
    }
  }
  console.log(maxResult)
}

export function twoSum(nums, target) {
  let indexByNum = {}
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i]
    if (target - num in indexByNum) {
      return [indexByNum[target - num], i]
    } else {
      indexByNum[num] = i
    }
  }
}

export function maxZeros(nums) {
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
}

export function printSeparator() {
  console.log("---------------------------------------------------\n")
}