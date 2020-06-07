import heapq
class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution:
    def __init__(self):
        self.headNode = None

    def initList(self,data1,data2,data3):
        list1 = []
        self.head1 = ListNode(data1[0])
        self.head2 = ListNode(data2[0])
        self.head3 = ListNode(data3[0])
        r1 = self.head1
        r2 = self.head2
        r3 = self.head3
        p1 = self.head1
        p2 = self.head2
        p3 = self.head3
        for i in data1[1:]:
            node1 = ListNode(i)
            p1.next = node1
            p1 = p1.next
        for j in data2[1:]:
            node2 = ListNode(j)
            p2.next = node2
            p2 = p2.next
        for k in data3[1:]:
            node3 = ListNode(k)
            p3.next = node3
            p3 = p3.next

        list1.append(r1)
        list1.append(r2)
        list1.append(r3)

        return list1


    '''#方法一：将链表转换为数组的形式
    def mergeKLists(self,lists):
        list2 = []
        for i in lists:
            while i:
                list2.append(i.val)
                i = i.next
        list2.sort()
        self.head = ListNode(list2[0])
        r = self.head
        p = self.head
        for cha in list2[1:]:
            node = ListNode(cha)
            p.next = node
            p = p.next
        return r '''

  #方法二，采用堆的形式，思路与方法一相同
    def mergeKLists(self,lists):
        cur = ListNode(0)
        h = cur
        listx = []
        for i in range(len(lists)):
            while lists[i]:
                heapq.heappush(listx,(lists[i].val,i))  #定义堆(二叉树)，将值添加到listx中
                lists[i] = lists[i].next
        while listx:
            val,indx = heapq.heappop(listx)   #以堆的形式压入，弹出时就会按照从小到大的顺序
            h.next = ListNode(val)
            h = h.next

        return cur.next



if __name__ =='__main__':
    s = Solution()
    data1 = [1,4,5]
    data2 = [1,3,4]
    data3 = [2,6]
    lists = s.initList(data1,data2,data3)
    print(s.mergeKLists(lists))



