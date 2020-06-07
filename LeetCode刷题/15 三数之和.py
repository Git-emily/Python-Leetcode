'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]'''
class Solution:
    def threeSum(self,nums):
        list1=[]
        nums.sort()
        if len(nums) < 3:
            return list1

        for i in range(len(nums)-2):
            j = i + 1
            p = len(nums) - 1
            if nums[i] > 0:
                break
            if i>0 and nums[i-1] == nums[i]:    #必须选择i-1和i想比：因为【-1，-1，2】，可以尝试。。
                                                   #并且必须在循环时就排除重复的情况，最后对list1进行去重会出现超出时间限制的情况；此外，采用三层循环也会导致超出时间限制。
                continue
            while j < p:
                if nums[i]+ nums[j]+nums[p] ==0:
                    list1.append([nums[i],nums[j],nums[p]])
                    while j<p and nums[j] == nums[j+1]:   #原因同判断nums[i-1]和nums[i]一样，用nums=[-2,0,0,2,2]来测;加上j<p的原因，用[0，0，0]来测
                        j+=1
                    while j<p and nums[p] == nums[p-1]:
                        p-=1
                    j += 1
                    p -= 1
                elif nums[i]+nums[j]+nums[p] < 0:
                    j+=1
                else:
                    p-=1
        return list1
if __name__ =='__main__':
    s = Solution()
    print(s.threeSum([0,0,0]))
