import threading

class Singleton(type):

    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            with Singleton._instance_lock:
                if not hasattr(cls,"_instance"):
                    cls._instance = super(Singleton,cls).__call__(*args,**kwargs)
        return cls._instance

class Foo(metaclass=Singleton):

    def __init__(self):
        pass

obj1 = Foo()
obj2 = Foo()
print(obj1 is obj2)