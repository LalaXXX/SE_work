import unittest
class TestClass:
    def maxSubArray(nums):
    # 动态规划，原地修改数组
        maxnum = nums[0]
        for i in range(1,len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            if nums[i] > 0:
                maxnum = max(maxnum,nums[i])
            else:
                maxnum = 0
        return maxnum 

class TestDemo(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test1(self):
        self.assertEqual(TestClass.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6, "test 1 fail")
    def test2(self):   
        self.assertEqual(TestClass.maxSubArray([-2,11,-4,13,-5,-2]), 20, "test 2 fail")
    def test3(self):   
        self.assertEqual(TestClass.maxSubArray([-2,-1,0]), 0, "test 3 fail")
    def tes4(self):   
        self.assertEqual(TestClass.maxSubArray([0,1,2]), 3, "test 4 fail")
    def test5(self):   
        self.assertEqual(TestClass.maxSubArray([-1,-1,-1]), 0, "test 5 fail")
    def test6(self):   
        self.assertEqual(TestClass.maxSubArray([1,1,1]), 3, "test 6 fail")
    def test7(self):   
        self.assertEqual(TestClass.maxSubArray([1,2,3]), 6, "test 7 fail")
    def test8(self):   
        self.assertEqual(TestClass.maxSubArray([-3,-2,-1]), 0, "test 8 fail")
        
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
