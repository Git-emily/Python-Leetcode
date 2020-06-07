'''采用出入栈的思想'''
from numpy.core.defchararray import strip


class Solution:
    def isValid(self,s):
        dic = {')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            if i in dic.values():
                stack.append(i)
            elif i in dic.keys():
                if stack == [] or stack.pop() != dic[i]:
                    return False
            else:
                return False

        return stack == []

if __name__ =='__main__':
    s = Solution()
    print(s.isValid("){"))