'''给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0

        d = {}
        p = 0
        start = 0
        res = 0
        for i in range(len(s)):   #i从前向后遍历
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]]+1    #start用来标记最近重复字符的位置
            p = i-start+1   #list下标起始值为0，如何元素全部不重复，会出现少1的情况
            d[s[i]] = i
            res = max(res,p)  #res存储的值为前面的字符中不重复字符串的最大长度
            print(res,p)
            print('max:',res)
        #return p

if __name__=='__main__':
    s = Solution()
    s.lengthOfLongestSubstring('a')
