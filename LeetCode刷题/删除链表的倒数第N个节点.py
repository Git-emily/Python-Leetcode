'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
'''

'''Leetcode中已经默认定义好了链表和结点；当本地运行时，首先必须要自己定义ListNode，且初始化结点'''
class ListNode:   #定义一个结点类
    def __init__(self,val=None):
        self.val = val
        self.next = None

class Solution:
    '''定义一个单链表（单链表是由一个个结点构成）：在结点类的基础上'''
    def __init__(self):  #新建一个头指针为空的链表
        self.head = None

    def initList(self,data):  #将数据插入到链表中
        #创建头结点
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        #对数组data进行操作，为每一个数创建结点，组成链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node #将ListNode(1)赋给头结点head的下一个结点；依此类推
            p = p.next
        return r

    '''
      #此方法会遍历两次表
    def removeNthFromEnd(self,head,n):
        len = 0
        index = 0
        tmp = head
        while not head :
            return None
        #第一次遍历链表，将head复制给tmp，使得tmp不断向后移，但是head还是指向第一个结点
        while tmp:
            len +=1
            tmp = tmp.next

        tmp = head
        m = len - n -1
        if len == n:
            return head.next
        else:
            #第二次遍历链表
            while index != m:
                index += 1
                tmp = tmp.next
            print(index)
            tmp.next = tmp.next.next  #必须要这样写，才可以实现删除指定结点的功能，
            # 【如删除index为3的结点，当index为2的结点.next() == index为2的结点.next.next,结点2的next指向index为4的结点
        return head
    '''
     #法二：遍历一次。采用两个指针p，q均指向头结点；
    # 将指针p向后移n个位置，再将p，q同时向后移动，当指针p移动到末尾时，q指针指向的结点即为要删除的结点

    def removeNthFromEnd(self,head,n):
        p = head
        q = head
        index = 0
        while index != n:
            index +=1
            p = p.next

        if p == None:
            return head.next

        while p.next != None:
            p = p.next
            q = q.next
        q.next = q.next.next  #删除q.next.val
        return head


if __name__ == '__main__':
    s = Solution()
    data = [1,2,3,4,5]
    head = s.initList(data) #调用链表方法，得到的head为链表类型
    print(s.removeNthFromEnd(head,1))
