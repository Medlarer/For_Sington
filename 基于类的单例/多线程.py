import time
import threading

class Singleton(object):

    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls,*args,**kwargs):
        if not hasattr(Singleton,"_instance"):
            with Singleton._instance_lock: #保证线程安全
                if not hasattr(Singleton,"_instance"):
                    Singleton._instance = Singleton(*args,**kwargs)
        return Singleton._instance


def task(arg):
    obj = Singleton.instance()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()


# 使用先说明，以后用单例模式，obj = Singleton.instance()
# 示例：
# obj1 = Singleton.instance()
# obj2 = Singleton.instance()
# print(obj1,obj2)
# 错误示例
# obj1 = Singleton()
# obj2 = Singleton()
# print(obj1,obj2)