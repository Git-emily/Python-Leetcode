'''思路：
1.是否有环： 采用slow指针和fast指针；slow指针往后遍历一个节点，fast指针遍历两个节点.当fast遍历到null节点则说明无环路；若slow和fast指针相同，则有环。
2.环的入口节点：假设链表头到环入口的距离是len，环入口到slow和fast交汇点距离为x，环的长度为R. slow和fast交会时，slow走的长度d=len+x ; fast为2d，即len+nR+x .
故2(len+x)= len+nR+x ; len = nR -x . 故算法即为：用一个cur指针指向链表头节点；一个inter指针指向第一次交汇点；当指针相等时，即为环的入口节点处.'''


class Node(object):   #Node是实现链表的基本模块，包含数据域（data）和指针（next）
    def __init__(self,data = None):
        self.data = data
        self.next = None

class FindLoop(Node):

    def findbeginofloop(head):
        slow = head
        fast = head   #特殊节点head，永远指向第一个节点
        loopExit = False   #默认环不存在，为False

        if head == None:   #如果头节点为空，即不存在环结构
            return False

        while slow.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                loopExit = True
                print("存在环结构")
                break

        if loopExit == True:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow   #返回环的入口节点

        print('不是环结构')
        return False

if __name__ ==  "__main__":
    node1 = Node(5)
    node2 = Node(4)
    node3 = Node(3)
    node4 = Node(2)
    node5 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node3
    print(FindLoop.findbeginofloop(node1).data)  #打印的是：环的入口节点值.....cause 返回环的入口节点slow,node1指的就是slow