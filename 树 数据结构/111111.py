class Node():  # 定义一个Node类，构造两个属性，一个是item节点值，一个是节点的下一个指向
    def __init__(self, item=None):
        self.item = item
        self.next = None

class FindLoop(Node):
    def findbeginofloop(head):  # 判断是否为环结构并且查找环结构的入口节点
        slowPtr = head  # 将头节点赋予slowPtr
        fastPtr = head  # 将头节点赋予fastPtr
        loopExist = False  # 默认环不存在，为False
        if head == None:  # 如果头节点就是空的，那肯定就不存在环结构
            return False
        while fastPtr.next != None and fastPtr.next.next != None:  # fastPtr的下一个节点和下下个节点都不为空
            slowPtr = slowPtr.next  # slowPtr每次移动一个节点
            fastPtr = fastPtr.next.next  # fastPtr每次移动两个节点
            if slowPtr == fastPtr:  # 当fastPtr和slowPtr的节点相同时，也就是两个指针相遇了
                loopExist = True
                print("存在环结构")
                break

        if loopExist == True:
            slowPtr = head
            while slowPtr != fastPtr:
                fastPtr = fastPtr.next
                slowPtr = slowPtr.next
            return slowPtr

        print("不是环结构")
        return False


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2
    print(FindLoop.findbeginofloop(node1).item)