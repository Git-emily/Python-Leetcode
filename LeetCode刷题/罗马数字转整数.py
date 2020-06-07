class Solution:
    def romanToInt(self,s):
        nums = 0
        dict = {'M':1000,'D':500,'C':100,'L':50,'X':10, 'V':5,'I':1 }

        for i in range(len(s)-1):
            first = dict.get(s[i])
            second = dict.get(s[i+1])
            if first < second:
                nums -= first
            else:
                nums += first
        nums +=dict.get(s[len(s)-1])
        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('LVIII'))

