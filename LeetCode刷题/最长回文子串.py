'''给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：
输入: "cbbd"
输出: "bb"'''
'''选择2*len(s)-1, 目的在于获取i的前后两个值（start和end）'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_ = ""
        for i in range(2 * len(s) - 1):
            print(i)
            if i % 2 == 0:  # 索引i指向偶数位置
                start = end = i // 2
                print('start:',start)
                while start >= 0 and end < len(s) and s[start] == s[end]:
                    start -= 1
                    end += 1
            else:  # 索引i指向奇数位置
                start = (i - 1) // 2
                end = (i + 1) // 2
                while start >= 0 and end < len(s) and s[start] == s[end]:
                    start -= 1
                    end += 1
            if len(str_) <= (end - start - 1):  # 更新最长字符串
                str_ = s[start + 1:end]
        return str_

if __name__ =='__main__':
    s = Solution()
    print(s.longestPalindrome('abcdefedcba'))