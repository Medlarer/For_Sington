import threading

class Singleton(object):

    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton,"_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton,"_instance"):#类加括号执行__new__方法,__new__创建一个实例Singleton
                    Singleton._instance = object.__new__(cls) #继承object类的__new__方法，类调用方法，是函数，加参数
        return Singleton._instance

def task(arg):
    obj = Singleton()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()

obj1 = Singleton()
obj2 = Singleton()
print(obj1,obj2)