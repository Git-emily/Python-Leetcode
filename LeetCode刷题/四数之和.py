'''给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
注意：
答案中不可以包含重复的四元组。
示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]'''
'''方法一和二的思路是一样的，在处理出现重复值以及判断条件上的区别'''
'''法一'''
'''
class Solution:
    def fourSum(self,nums,target):
        list1 = []
        nums.sort()

        if len(nums) == 4 and nums[0] + nums[1] +nums[2]+nums[3] == target:
            return [nums]

        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                p = j+1
                q = len(nums)-1
                while p < q:
                    if nums[i]+nums[j]+nums[p]+nums[q] == target:
                        tmp = [nums[i], nums[j], nums[p], nums[q]]
                        if tmp not in list1:
                            list1.append(tmp)
                    if nums[i]+nums[j]+nums[p]+nums[q] > target:
                        q -= 1
                    elif nums[i]+nums[j]+nums[p]+nums[q] < target:
                        p += 1
                    else:
                        p += 1
                        q -= 1

        return list1

'''
'''法二'''
class Solution:
    def fourSum(self,nums,target):
        list1 = []
        nums.sort()

        for i in range(len(nums)-3):
            if sum(nums[i:i+4]) >target:
                break
            if i>0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1,len(nums)-2):
                if nums[i] + sum(nums[j:j+3]) > target:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                p = j+1
                q = len(nums)-1
                while p < q:
                    tmp = nums[i] + nums[j] + nums[p] + nums[q]
                    if tmp == target:
                        list1.append([nums[i], nums[j], nums[p], nums[q]])
                        while p<q and nums[p] == nums[p+1]:
                            p += 1
                        while p<q and nums[q] == nums[q-1]:
                            q -= 1
                        p += 1
                        q -= 1
                    elif nums[i]+nums[j]+nums[p]+nums[q] < target:
                        p += 1
                    else:
                        q -= 1


        return list1

if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([-3,-2,-1,0,0,1,2,3],0))





