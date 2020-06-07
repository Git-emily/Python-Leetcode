'''给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].'''
'''解法一：'''
'''
class Solution:
    def letterCombinations(self,digits):
        list1 = []
        list2 = [[]]  #注意这种定义的方式
        result = []
        d = {2:['a','b','c'] , 3:['d','e','f'], 4:['g','h','i'] , 5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z'] }
        if not digits:
            return ''
        for i in digits:
            i = int(i)
            list1.append(d[i])

        for cha in list1:
            list2 = [x+[y] for x in list2 for y in cha]   #注意这种表达方式，以及list2的定义，自行测试

        for re in list2:
            print(re)
            result.append(''.join(re))   #join()函数，在re中间不加任何内容

        return (result)
'''
'''解法2，采用递归'''
class Solution:
    def letterCombinations(self,digits):
        list1 = []
        d = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
             7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

        if not digits:
            return ''

        if len(digits) == 1:
            return d[int(digits[0])]    #return返回结果，同时会返回上一层的递归，即当digits='35'的时候

        result = self.letterCombinations(digits[1:])

        for i in result:
            for j in d[int(digits[0])]:
                list1.append(j+i)
        return (list1)    #当采用递归时，return属于上一次的递归调用，等多次返回调用后，直到def时，才会出去


if __name__=='__main__':
    s = Solution()
    print(s.letterCombinations('235'))