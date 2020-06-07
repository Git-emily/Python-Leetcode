#定义单链表
class ListNode(object):
    def __init__(self,x):
        if isinstance(x,int):
            self.val = x
            self.next = None

        elif isinstance(x,list):
            self.val = x[0]
            self.next = None
            cur = self
            for i in x[1:]:
                cur.next = ListNode(i)
                cur = cur.next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"

class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode):
        if isinstance(l1,list):
            l1 = ListNode(l1)
            l2 = ListNode(l2)

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        l3 = ListNode(0)  #引用ListNode类定义类一个链表节点并赋给l3
        res = l3
        flag = 0
        while l1 and l2:
            temp = 0
            temp = l1.val + l2.val + flag
            l1 = l1.next
            l2 = l2.next
            temp_pre = ListNode(temp % 10)
            flag = int(temp // 10)
            res.next = temp_pre
            res = res.next
            print('res是',res)

        if l1:
            while l1:
                temp = 0
                temp = l1.val +flag
                l1 = l1.next
                temp_pre = ListNode(temp % 10)
                flag = int(temp // 10)
                res.next = temp_pre
                res = res.next
                print('res是', res)
        if l2:
            while l2:
                temp = 0
                temp = l2.val +flag
                l2 = l2.next
                temp_pre = ListNode(temp % 10)
                flag = int(temp // 10)
                res.next = temp_pre
                res = res.next
                print('res是', res)

        if flag:
            res.next = ListNode(1)  #res的下一节点设为1
            print('RES is:',res)
        print('l3是：',l3.next)

if __name__ == '__main__':
    s = Solution()
    s.addTwoNumbers([1,8],[0])

