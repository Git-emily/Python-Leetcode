'''编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。'''
'''思路：取出strs中最短的字符串，将该字符串的每个字符与其他的字符串字符相匹配'''
class Solution:
    def longestCommonPrefix(self,strs):
        if not strs:
            return ''
        shortstr = min(strs,key=len)
        for i,cha in enumerate(shortstr):
            for other in strs:
                if other[i] != cha:
                    return shortstr[:i]
        return shortstr


if __name__=='__main__':
    s = Solution()
    print(s.longestCommonPrefix(["dog","racecar","car"]))

