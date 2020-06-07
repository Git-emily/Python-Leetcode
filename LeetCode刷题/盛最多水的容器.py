'''给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。

示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
'''
'''粗略解释：矩阵要求两条垂直线的距离越远越好，垂直线的长度越长也好。故，比较
左右两端的高度，将较短高度的那条线像前/后移动一位'''
class Solution:
    def maxArea(self,height):
        maxV = 0
        i= 0
        j = len(height)-1
        while i < j:
            maxV = max(maxV,(j-i)*min(height[i],height[j]))
            if height[i] > height[j]:
                j-=1
            else:
                i+=1
        return maxV

if __name__=='__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,6]))