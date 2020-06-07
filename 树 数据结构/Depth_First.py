'''利用BuildTree, 进行Depth_First_Search: Preoder; inorder; postorder'''

from 树.BuildTree import BinaryTree

class BinaryTree2(BinaryTree):
    def preorder(self,root):   #先序遍历
        node = root
        if node == None:
            return
        print(node.data)

        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self,root): #中序遍历
        node = root
        if node == None:
            return
        self.inorder(node.lchild)
        print(node.data)
        self.inorder(node.rchild)

    def postorder(self,root):  #后续遍历
        node = root
        if node == None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.data)


if __name__ == '__main__':
    arr = []
    for i in range(10):
        arr.append(i)
    #print('arr:',arr)

    tree = BinaryTree2()
    for i in arr:
        tree.add(i)

    tree.preorder(tree.root)
    print('先序遍历')

    tree.inorder(tree.root)
    print('中序遍历')

    tree.postorder(tree.root)
    print('后续遍历')

