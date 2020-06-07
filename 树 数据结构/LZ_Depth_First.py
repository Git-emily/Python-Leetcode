from 树.LZ_BuildTree import BinaryTree

class BinaryTree2(BinaryTree):
    def pre_order(self, start):
        node = start
        if node == None:
            return

        print(node.data)
        if node.lchild == None and node.rchild == None:
            return
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)


    def in_order(self, start):
        node = start
        if node == None:
            return
        self.in_order(node.lchild)
        print(node.data)
        self.in_order(node.rchild)


    def post_order(self, start):
        node = start
        if node == None:
            return
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.data)


    def isEmpty(self):
        return True if self.root.data == -1 else False


if __name__ == '__main__':
    arr = []
    for i in range(10):
        arr.append(i)
    print(arr)

    tree = BinaryTree2()
    for i in arr:
        tree.add(i)
    #print('level_order:',tree.level_order())
    print('pre order:',tree.pre_order(tree.root))
   # print('\npre order loop:',tree.pre_order_loop())
    print('\nin_order:',tree.in_order(tree.root))
  #  print('\nin_order loop:',tree.in_order_loop())
    print('\npost_order:',tree.post_order(tree.root))
#    print('\npost_order_loop:',tree.post_order_loop())
   # print('\npost_order_loop1:',tree.post_order_loop1())