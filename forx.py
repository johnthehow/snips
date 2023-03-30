from itertools import product

from thehow.snips import constants
from thehow.snips import dictx

def func(*args):
	return [i for i in args]

'''
[函数注释]
	[功能]
		1. 主要功能: 模拟多层嵌套的for循环, 尤其是循环层数事先不能确定时
		2. 额外功能
	[设计图]
		1. 索引码: 
		2. 文件类型: 
	[参数]
		1. func
			1. 数据类型: function
			2. 数据结构: function
			3. 参数类型: 必选
			4. 语义: 放在循环最内层被运行的函数
			5. 取值范围: 
			6. 获得来源: 手动输入
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
def nested_for(func,lists): # 20230330125323
	result = dictx.create_nested_dict(lists, len(lists)-1)
	for idx_seq in product(*lists):
		oneres = func(*idx_seq)
		dictx.dict_seqidx_setter(result,idx_seq,oneres)
	return result


if __name__ == '__main__':
	res = nested_for(func, constants.nested_dict_keylist)
	print(res)