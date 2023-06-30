from time import time

'''
[函数注释]
    [功能]
        1. 主要功能: 装饰器型计时器
        2. 额外功能
    [用例]
        1. [用例1]
            1. 语句
                >>> from thehow.snips.timex import deco_timer

                >>> @deco_timer
                    def func(args):
                       代码段
                       return

                >>> func(args)
'''
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

'''
[函数注释]
    [功能]
        1. 主要功能: 上下文管理器型计时器
        2. 额外功能
    [用例]
        1. [用例1]
            1. 语句
                from thehow.snips.timer import with_timer
                with with_timer() as tm:
                    代码段
'''
class with_timer(object): # 20230321183039
    def __enter__(self):
        self.time_start = time()
    def __exit__(self,exc_type, exc_val,exc_tb):
        self.time_end = time()
        print(self.time_end - self.time_start)