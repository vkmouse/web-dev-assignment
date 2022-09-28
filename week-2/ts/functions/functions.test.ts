import { calculate, avg, func, maxProduct, twoSum, maxZeros } from "./functions"

test('calculate', () => {
  expect(calculate(1, 3, 1)).toBe(6)
  expect(calculate(4, 8, 2)).toBe(18)
  expect(calculate(-1, 2, 2)).toBe(0)
})

test('avg', () => {
  const employees = [
    {
      "name":"John",
      "salary":30000,
      "manager":false
    },
    {
      "name":"Bob",
      "salary":60000,
      "manager":true
    },
    {
      "name":"Jenny",
      "salary":50000,
      "manager":false
    },
    {
      "name":"Tony",
      "salary":40000,
      "manager":false
    }
  ]
  expect(avg({ "employees": employees })).toBe(40000)
})

test('func', () => {
  expect(func(2)(3, 4)).toBe(14)
  expect(func(5)(1, -5)).toBe(0)
  expect(func(-3)(2, 9)).toBe(15)
})

test('maxProduct', () => {
  expect(maxProduct([5, 20, 2, 6])).toBe(120)
  expect(maxProduct([10, -20, 0, 3])).toBe(30)
  expect(maxProduct([10, -20, 0, -3])).toBe(60)
  expect(maxProduct([-1, 2])).toBe(-2)
  expect(maxProduct([-1, 0, 2])).toBe(0)
  expect(maxProduct([5,-1, -2, 0])).toBe(2)
  expect(maxProduct([-5, -2])).toBe(10)
})

test('twoSum', () => {
  expect(twoSum([2, 11, 7, 15], 9)).toStrictEqual([0, 2])
})

test('maxZeros', () => {
  expect(maxZeros([0, 1, 0, 0])).toBe(2)
  expect(maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])).toBe(4)
  expect(maxZeros([1, 1, 1, 1, 1])).toBe(0)
  expect(maxZeros([0, 0, 0, 1, 1])).toBe(3)
})
