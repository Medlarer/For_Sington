import time
import threading

class Singeton(object):

    def __init__(self):
        time.sleep(1)
        # self._instance = None

    @classmethod
    def instance(cls,*args,**kwargs):
        if not hasattr(Singeton,"_instance"):
            Singeton._instance = Singeton(*args,**kwargs)
        return Singeton._instance

def task(*arg):
    obj = Singeton.instance()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()