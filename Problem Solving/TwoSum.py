class Solution(object):
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    def twoSum(self):
        for i in range(len(self.nums)):
            for j in range(i+1, len(self.nums)):
                 if(self.nums[i]+self.nums[j]== self.target):
                     print("[{},{}]".format(i, j))
             
nums= [2,7,11,15]
target=9                   
obj = Solution(nums, target)
print(obj.twoSum())