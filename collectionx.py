from collections import Counter

'''
[函数注释]
	[功能]
		1. 主要功能: 增强collections.Counter的功能: 1. 按key排序 2.补全key
		2. 额外功能
	[设计图]
		1. 索引码: 
		2. 文件类型: 
	[参数]
		1. lst
			1. 数据类型: list
			2. 数据结构: [val,val]
			3. 参数类型: 必选
			4. 语义: 目标列表
			5. 取值范围: 
			6. 获得来源: 手动输入
			7. 样例文件/输入: [1,2,3,3,3,5,6,6,7,9]
		2. complete_keys
			1. 数据类型: list
			2. 数据结构: [val,val]
			3. 参数类型: 必选
			4. 语义: 用于key补全的期望中的完整key列表
			5. 取值范围: 
			6. 获得来源: 手动输入
			7. 样例文件/输入: [i for i in range(1,11)]
		3. default_val
			1. 数据类型: 任意
			2. 数据结构: 任意
			3. 参数类型: 必选
			4. 语义: 补全key时, 对应的value
			6. 取值范围:
			7. 获得来源: 手动输入
			8. 样例文件/输入: 0
	[用例]
		1. default_counter([1,2,3,3,3,5,6,6,7,9], [i for i in range(1,11)], 0)
			2. 输出
				1. 语义: 计数这个列表, 如果有列表中没出现的, 计数为0
				2. 数据类型: dict
				3. 数据结构: {key:val}
				4. 样例文件/输出: {1: 1, 2: 1, 3: 3, 4: 0, 5: 1, 6: 2, 7: 1, 8: 0, 9: 1, 10: 0}
	[依赖]
		1. collections.Counter
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
def default_counter(lst, complete_keys, default_val):
	res_dict = Counter(lst)

	for i in complete_keys:
		if i not in res_dict.keys():
			res_dict[i] = default_val
	res_dict = dict(sorted(res_dict.items(),key=lambda i:i[0]))
	return res_dict