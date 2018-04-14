class Singleton(type):

    def __init__(self,*args,**kwargs):
        print(2,self)
        super(Singleton,self).__init__(*args,**kwargs)

    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls,*args,**kwargs)
        obj.__init__(*args,**kwargs)
        return obj

class Foo(metaclass=Singleton):

    def __init__(self,name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        print(2,cls)
        return object.__new__(cls,*args,**kwargs)

#可能有问题
obj = Foo("Shaw")
