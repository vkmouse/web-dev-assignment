def calculate(min, max, step):
    result = 0
    for i in range(min, max + 1, step):
        result += i
    print(result)

def avg(data):
    sum = 0
    count = 0
    for employee in data["employees"]:
        if not employee["manager"]:
            sum += employee["salary"]
            count += 1
    print(sum / count)

def func(a):
    result = a
    def func1(b, c):
        print(result + (b * c))
    return func1

def maxProduct(nums):
    maxResult = nums[0] * nums[1]
    for index, num1 in enumerate(nums):
        for num2 in nums[index + 1:]:
            maxResult = max(maxResult, num1 * num2)
    print(maxResult)

def twoSum(nums, target):
    indexByNum = dict()
    for index, num in enumerate(nums):
        if target - num in indexByNum:
            return [indexByNum[target - num], index]
        else:
            indexByNum[num] = index

def maxZeros(nums):
    result = 0
    currentZeros = 0
    for num in nums:
        if (num == 0):
            currentZeros += 1
        else:
            result = max(result, currentZeros)
            currentZeros = 0
    result = max(result, currentZeros)
    print(result)

def printSeparator():
    print("---------------------------------------------------\n")
