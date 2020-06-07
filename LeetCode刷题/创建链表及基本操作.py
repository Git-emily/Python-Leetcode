class ListNode:#定义一个结点类
    def __init__(self,val=None):   #self代表实例本身；python解释器会自动调用__init__
        self.val = val
        self.next = None


class creat_List(): #定义一个单链表（单链表是由一个个结点构成）：在结点类的基础上
    def __init__(self):   #新建一个头指针为空的链表
        self.head = None

    def initList(self,data):   #将数据插入到链表中
        self.head = ListNode(data[0])
        p = self.head
        r = self.head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    def isEmpty(self):   #判断链表是否为空
        if self.head.next == 0:
            print('Empty List')
            return 1
        else:
            return 0

    def getLength(self): #取链表长度
        if self.isEmpty():
            exit(0)
        p = self.head
        len = 0
        while p:
            len += 1
            p = p.next
        return len

    def traveList(self): #遍历链表
        if self.isEmpty():
            exit(0)
        p = self.head
        while p:
            print(p.val)
            p = p.next

    def insertElem(self,key,index):  #链表插入数据函数
        if self.isEmpty():
            exit(0)

        if index < 0 or index > self.getLength()-1:
            exit(0)

        p = self.head
        i = 0
        while i<= index:  #找到index的val，赋给pre；将p.next赋给p，便于接到index.val的后面
            pre = p
            p = p.next
            i +=1

        node = ListNode(key)
        pre.next = node
        node.next = p

    def deleteElem(self,index):  #删除某一结点数据
        if self.isEmpty():
            exit(0)
        if index < 0 or index > self.getLength()-1:
            exit(0)

        i = 0
        p = self.head
        while p.next:
            pre = p
            p = p.next
            i+=1
            if i == index:
                pre.next = p.next
                p = None
                return 1

        pre.next = None  #while p.next为空时，直接删除即可



if __name__ == '__main__':
    data = [1,2,3,4,5]
    s = creat_List()
    res = s.initList(data)
    s.traveList()
    s.insertElem(123,2)   #在index=2后插入值123
    s.traveList()
    s.deleteElem(3)  #删除index为3的结点
    s.traveList()
