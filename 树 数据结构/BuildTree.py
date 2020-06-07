class Node(object): #object代表Node可以继承object对象
    '''创建节点类'''
    def __init__(self, data = -1 , lchild = None, rchild= None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree(object):
    '''创建树类'''
    def __init__(self):
        self.root = Node()

    '''为树添加节点'''
    def add(self,data):
        node = Node(data)
        '''如果根节点是空的,给根节点赋值'''
        if self.root == None:
            self.root == node
        else:        #不为空，对已有的节点进行层次遍历
            cur = self.root
            queue = []
            queue.append(self.root)

            while queue:
                cur = queue.pop(0)   #弹出队列的第一个元素

                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:    #如果左右子树都不为空，加入队列继续监听
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)
