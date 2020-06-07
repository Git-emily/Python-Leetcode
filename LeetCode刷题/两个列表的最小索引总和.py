import self as self
list1 = []
list2 = []
class Solution(object):
    def findRestaurant(self,list1,list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict = {}
        for i, item in enumerate(list1):
            dict[item] = i
        print(dict)

        minIdxSum =60  # 用于记录当前最小的索引和
        res = []
        for i, item in enumerate(list2):
            if item in dict:  # 当前餐厅两者都爱
                tmp = i + dict[item]
                if tmp < minIdxSum:  # 需要更新最小索引和
                    res = [item]
                    minIdxSum = tmp
                elif tmp == minIdxSum:  # 是目前的最小索引和
                    res.append(item)
                print(res)
                print(minIdxSum)

x= input('请输入list1，用逗号分隔：')
list1=x.split(',')
y= input('请输入list2，用逗号分隔：')
list2=y.split(',')
test = Solution.findRestaurant(self,list1,list2)

'''
样例：
Shogun,Tapioca Express,Burger King,KFC；Piatti,The Grill at Torrey Pines,Hungry Hunter Steakhouse,Shogun 
结果为：Shogun 3
Shogun,Tapioca Express,Burger King,KFC ; KFC,Shogun,Burger
结果为：Shogun 1
'''