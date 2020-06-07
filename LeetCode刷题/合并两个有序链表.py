'''将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4'''
class ListNode():
    def __init__(self,val=None):
        self.val = val
        self.next = None

class Solution:
    def __init__(self):
        self.headNode = None

    def initList(self,data1,data2):
        self.head1 = ListNode(data1[0])
        self.head2 = ListNode(data2[0])
        r1 = self.head1
        r2 = self.head2
        p1 = self.head1
        p2 = self.head2
        for i ,j in zip(data1[1:],data2[1:]):
            node1 = ListNode(i)
            node2 = ListNode(j)
            p1.next = node1
            p1 = p1.next
            p2.next = node2
            p2 = p2.next

        return r1,r2
    '''
#法一：将其转为list，再转回链表
    def mergeTwoLists(self,l1,l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        list1 = []
        list2 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next

        list1.extend(list2)
        list1.sort()
        self.head = ListNode(list1[0])
        r = self.head
        p = self.head
        for i in list1[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next

        return r

'''
    def mergeTwoLists(self,l1,l2):
        cur = ListNode(0) #初始化定义cur为结点，且val=0
        h = cur    #cur将会在后面遍历，直至队尾；
        cur1 = l1
        cur2 = l2
        while cur1 !=None and cur2 !=None:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
  #判断cur1和cur2分别是否到各自的链表的末尾，如果不是，将剩余元素添加到新的cur末尾即可
        if cur1!=None:
            cur.next = cur1

        if cur2 != None:
            cur.next = cur2

        return h.next   #因为在h定义时，在链表的头部新增了ListNode(0),故需要删除，只返回h.next以后的






if __name__ == '__main__':
    s = Solution()
    data1 = [1,2,4]
    data2 = [1,3,4]
    l1,l2 = s.initList(data1,data2)
    print(s.mergeTwoLists(l1,l2))





