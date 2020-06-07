'''给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0
示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5'''
'''方法一：采用两个列表合并法，但是时间复杂度没办法满足'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()

        if len(nums1) % 2 != 0:
            a = int(len(nums1)/2)
            return nums1[a]

        if len(nums1) % 2 == 0:
            a = len(nums1)//2
            b = (nums1[a-1]+nums1[a])/2
            return b
'''方法二：二分查找'''

class Solution:
    def findMedianSortedArrays(self,nums1:List[int],nums2:List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        if (l1+l2) % 2 !=0:
            return self.findKith(nums1,nums2,(l1+l2)//2)
        else:
            m = (l1+l2) / 2
            return self.findKith(nums1,nums2,(2*m - 1)/2)

    def findKith(self,nums1,nums2,k):

        i1,i2 = len(nums1)//2,len(nums2)//2
        m1,m2=nums1[i1],nums2[i2]
        if i1 + i2 >= k :
            if m1>m2:
                self.findKith(nums1[:i1],nums2,k)
            else:
                self.findKith(nums1,nums2[:i2],k)
        else:
            if m1>m2:
                self.findKith(nums1,nums2[i2+1:],k)
            else:
                self.findKith(nums1[i1+1:],nums2,k)



