import operator
from functools import reduce

'''
[函数注释]
    [功能]
        1. 主要功能: 连乘, 将列表中的所有元素相乘
        2. 额外功能
    [设计图]
        1. 索引码: 
        2. 文件类型: 
    [参数]
        1. multipliers
            1. 数据类型: list
            2. 数据结构: [num,num]
            3. 参数类型: 必选参数
            4. 语义: 成熟
            5. 取值范围: 
            6. 获得来源: 手动输入
            7. 样例文件/输入: [1,2,3,4,5]
    [用例]
        1. product_multiple([1,2,3,4,5])
            1. 输出
                1. 语义: 连乘的积
                2. 数据类型: num
                3. 数据结构: num
                4. 样例文件/输出: 120 
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
def product_multiple(multipliers): # 20230330152948
    return reduce(operator.mul, multipliers)