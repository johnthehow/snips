from itertools import product
from thehow.snips import dictx

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
			7. 样例文件/输入: func = lambda *args:[i for i in args]
		2. lists
			1. 数据类型: list
			2. 数据结构: [[val,val],[val,val]]
			3. 参数类型: 必选
			4. 语义: 作为各层循环的keys
			5. 取值范围: 
			6. 获得来源: 手动输入
			7. 样例文件/输入: lsts = constants.nested_dict_keylist # 20230330134755
	[用例]
		1. neste_for(func,lsts)
			1. 输出
				1. 语义: 对应各个keys的func的返回值
				2. 数据类型: dict
				3. 数据结构: {key:{key:val}}
				4. 样例文件/输出: 20230330135152.txt
	[依赖]
		1. thehow.snips.dictx.create_nested_dict # 20230315092535
		2. itertools.product
		3. thehow.snips.dictx.dict_seqidx_setter # 20230316182821
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
		1. 目前, 函数的所有必选参数必须完全且仅能来自于lists, 且顺序应当对应
		2. 
'''
def nested_for(func,lists): # 20230330125323
	result = dictx.create_nested_dict(lists, len(lists)-1)
	for idx_seq in product(*lists):
		oneres = func(*idx_seq)
		dictx.dict_seqidx_setter(result,idx_seq,oneres)
	return result
