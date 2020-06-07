import self
class Solution:
    def numUniqueEmails(self,emails):
        res = set()    #set函数，创建集合
        #print(emails)
        for email in emails:
            temp = ''
            for i in range(len(email)):
                if email[i] == '@':
                    temp += email[i:]   # 取@后面的字符串
                    break
                else:
                    if email[i] == '.':
                        continue
                    elif email[i] == '+':
                        temp += email[email.index('@'):]   #index()函数用来返回str中'@'是在第几位
                        break
                    else:
                        temp += email[i]   #用于取@前面符合条件的字符串
            res.add(temp)   #集合中添加元素，将传入的元素作为一个整体添加到集合中；PS：update方法，可将传入的元素拆分，作为个体传入到集合中
        #return len(res)
        print(res)
test = Solution.numUniqueEmails(self, ["testemailalex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
