class parent():   #父类
    def __init__(self,name,age,weight):  #init()构造函数，是在创建实例p时，p就具有了属性，因为在类中的方法就可以直接使用变量
        self.name=name    #重新给类的name变量赋值，并可全局调用
        self.age=age
        self.weight=weight
        print('Hi,','%s'%(self.name)) #实例p在执行时，会先执行init，再执行parinform
    def parinform(self):
        print('This is parent,','%s is %s weights %s' % (self.name,self.age,self.__weight))

#p = parent('Emily',25,48)   #将变量赋值给person类实例化
#p.parinform()   #调用person类的方法

class child1(parent):   #子类，继承父类
    def __init__(self,name,age):    #子类重写init(),实例化子类时，不会调用父类的init
        self.name=name
        self.age=age
        print('Good','%s' %self.name)

    def parinform(self):    #子类重写父类的方法
        print('This is child1','%s is %s' %(self.name,self.age))

    def chiinform(self):
        super(child, self).chiinform()

class child2(parent):   #子类不重写init(),实例化子类时，会自动调用父类的init方法
    def parinform(self):
        print('This is child2','%s is %s and her weight is %s' %(self.name,self.age,self.weight))

class child3(parent):  #子类需重写init，但需要调用父类的init构造方法
    def __init__(self,name,age,weight):
        super(child3,self).__init__(name,age,weight)
        print('This is child3','%s is %s, her weight is %s' %(self.name,self.age,self.weight))
        self.name='Emily4'
    def parinform(self):
        print('This is child3','my name is %s' %(self.name))    #注意此处的结果

if __name__=='__main__':
    q=child1('Emily1',26)
    q.parinform()
    r=child2('Emily2',27,47)
    r.parinform()
    s=child3('Emily3',28,46)
    s.parinform()