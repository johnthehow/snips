from time import time

'''
[函数注释]
    [功能]
        1. 主要功能: 装饰器型计时器
        2. 额外功能
    [设计图]
        1. 索引码: 
        2. 文件类型: 
    [参数]
        1. [参数1]
            1. 数据类型: 
            2. 数据结构: 
            3. 参数类型: 
            4. 语义: 
            5. 取值范围: 
            6. 获得来源: 
            7. 样例文件/输入: 
        2. [参数2]
            1. 数据类型: 
            2. 数据结构: 
            3. 参数类型: 
            4. 语义: 
            5. 取值范围: 
            6. 获得来源: 
            7. 样例文件/输入: 
    [用例]
        1. [用例1]
            1. 语句: 
            2. 输出
                1. 语义: 
                2. 数据类型: 
                3. 数据结构: 
                4. 样例文件/输出: 
    [依赖]
        1. 
        2. 
    [已知问题]
        1. [问题1标题]
            1. 问题描述
            2. 问题复现
                1. 复现环境
                2. 复现语句
                3. 复现存档
    [开发计划]
        1. 
        2.
    [备注]
        1.
        2. 
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