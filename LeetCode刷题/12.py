from collections import Counter
class Solution:
    def threeSum(self, nums):
        list1 = []
        m = []
        for i , a in enumerate(nums):
            for j , b in enumerate(nums[i+1:]):
                for k , c in enumerate(nums[i+j+2:]):
                    if a+b+c == 0:
                        list1.append([a,b,c])
        return list1

# https://blog.csdn.net/qq_17550379/article/details/80614597