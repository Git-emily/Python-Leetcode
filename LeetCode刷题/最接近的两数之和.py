'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).'''
class Solution:
    def threeSumClosest(self,nums,target):
        nums.sort()
        res = float('inf')  #设置res为无穷大或无穷小
        result  = 0
        for i in range(len(nums)-2):
            j = i+1
            p = len(nums) - 1
            while j < p:
                m = nums[i]+nums[j]+nums[p]
                if abs(m-target) < res:
                    res = abs(m-target)
                    result = m
                if m > target :
                    p-=1
                elif m < target:
                    j+=1
                else:
                    return target


        return result


if __name__=='__main__':
    s = Solution()
    print(s.threeSumClosest([1,1,-1,-1,3],-1))

