
def wrapper(cls):
    instance = {}
    def inner(*args,**kwargs):
        if cls not in instance:
            instance[cls] = cls(*args,**kwargs)
        return instance[cls]
    return inner

@wrapper
class Singleton(object):

    def __init__(self):
        pass

obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)