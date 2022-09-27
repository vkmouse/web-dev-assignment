from functions import calculate, avg, func, maxProduct, twoSum, maxZeros
import unittest

class TestFunctions(unittest.TestCase):
    def testCalculate(self):
        self.assertEqual(calculate(1, 3, 1), 6)
        self.assertEqual(calculate(4, 8, 2), 18)
        self.assertEqual(calculate(-1, 2, 2), 0)

    def testAvg(self):
        actual = avg({
            "employees":[
                {
                    "name":"John",
                    "salary":30000,
                    "manager":False
                },
                {
                    "name":"Bob",
                    "salary":60000,
                    "manager":True
                },
                {
                    "name":"Jenny",
                    "salary":50000,
                    "manager":False
                },
                {
                    "name":"Tony",
                    "salary":40000,
                    "manager":False
                }
            ]
        })
        self.assertEqual(40000, actual)

    def testFunc(self):
        self.assertEqual(func(2)(3, 4), 14)
        self.assertEqual(func(5)(1, -5), 0)
        self.assertEqual(func(-3)(2, 9), 15)

    def testMaxProduct(self):
        self.assertEqual(maxProduct([5, 20, 2, 6]), 120)
        self.assertEqual(maxProduct([10, -20, 0, 3]), 30)
        self.assertEqual(maxProduct([10, -20, 0, -3]), 60)
        self.assertEqual(maxProduct([-1, 2]), -2)
        self.assertEqual(maxProduct([-1, 0, 2]), 0)
        self.assertEqual(maxProduct([5,-1, -2, 0]), 2)
        self.assertEqual(maxProduct([-5, -2]), 10)

    def testTwoSum(self):
        self.assertEqual(twoSum([2, 11, 7, 15], 9), [0, 2])

    def testMaxZeros(self):
        self.assertEqual(maxZeros([0, 1, 0, 0]), 2)
        self.assertEqual(maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]), 4)
        self.assertEqual(maxZeros([1, 1, 1, 1, 1]), 0)
        self.assertEqual(maxZeros([0, 0, 0, 1, 1]), 3)