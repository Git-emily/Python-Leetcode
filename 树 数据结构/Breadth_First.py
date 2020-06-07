'''广度优先搜索'''

from 树.BuildTree import BinaryTree

class BinaryTree3(BinaryTree):
    def Breadth_First(self,root):
        node = self.root
        if node == None:
            return
        queue = []
        queue.append(node)

        while queue:
            node = queue.pop(0)
            print(node.data)
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)

if __name__=='__main__':
    arr = []
    for i in range(10):
        arr.append(i)

    tree = BinaryTree3()
    for i in arr:
        tree.add(i)

    tree.Breadth_First(tree.root)
    print('层次遍历')