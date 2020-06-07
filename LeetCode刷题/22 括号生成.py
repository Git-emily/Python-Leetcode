'''给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
'''采用回溯法，当'('的数量小于n时，向S中添加；当')'小于'('的数量时，S中添加')' '''
class Solution:
    def generateParenthesis(self,n):
        list1 = list()
        self.backtracks(n,list1, S='', l=0, r =0)
        return list1

    def backtracks(self,n,list1,S, l,r):
        if l < n:
            self.backtracks(n,list1,S+'(',l+1,r)
        if r < l :
            self.backtracks(n,list1,S+')',l,r+1)
        if len(S) == 2*n:
            list1.append(S)
            return



if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))





