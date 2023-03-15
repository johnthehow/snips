from time import time

def deco_timer(func):
    def func_wrapper(*args,**kwargs):
        from time import time
        time_start = time()
        result = func(*args,**kwargs)
        time_end = time()
        time_spend = time_end - time_start
        print(f'time cost: {time_spend} seconds')
        return result
    return func_wrapper


class with_timer(object):
    def __enter__(self):
        self.time_start = time()
    def __exit__(self,exc_type, exc_val,exc_tb):
        self.time_end = time()
        print(self.time_end - self.time_start)