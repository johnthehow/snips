'''
[函数注释] 20230315001106
	[功能]
		1. 主要功能: 判断嵌套字典的层数(keys的个数)
	[参数]
		1. dic
			1. 数据类型: dict
			2. 参数类型: 必选
			3. 语义: 被判断层数的嵌套字典
			4. 默认值:
			5. 取值范围:
			6. 获得来源: 手动输入
			7. 样例: dict1 = {'for':{'PREP':[1,2,3]}}
	[输出]
		1. 默认
			1. 语义: 嵌套字典的层数
			2. 数据结构:
			3. 样例
			>>>	dict1 = {'for':{'PREP':[1,2,3]}}
			>>>	dict_depth(dict1)
			>>> 2
	[用例]
		1. 用例1
			1. 语义:
			2. 语法:
				1. func(参数1, 参数2, ...)
	[依赖]
		1. 无
'''
def dict_depth(dic): # 20230315001106
	for v in dic.values():
		if isinstance(v, dict):
			return dict_depth(v) + 1
		else:
			return 1

'''
[函数注释] 20230315092535
	[功能]
		1. 主要功能: 生成嵌套字典
	[参数]
		1. lists
			1. 数据类型: list
			2. 数据结构: [[obj,obj],[obj,obj]]
			3. 参数类型: 必选
			4. 语义: 用于生成嵌套字典的key列表
			5. 默认值:
			6. 取值范围:
			7. 获得来源: 手动输入
			8. 样例文件/输入: lsts = [[1,2,3,4],['a','b','c','d'],['甲','乙','丙','丁']]
		2. idx
			1. 数据类型: int
			2. 数据结构: int
			3. 参数类型: 必选
			4. 语义: lists参数的长度-1
			5. 默认值:
			6. 取值范围:
			7. 获得来源:
			8. 样例文件/输入: 
	[输出]
		1. 默认输出
			1. 语义: 生成的嵌套字典
			2. 数据类型: dict
			3. 数据结构: {key:{key:{key:[]}}}
			3. 样例文件/输出:
	[已知问题]
		1. [问题1]
			1. 问题描述
			2. 问题复现
				1. 复现环境
				2. 复现语句
				3. 复现存档
	[开发计划]
		1. 
		2.
	[备注]
		1. 不采用fromkeys方法是因为该方法生成的字典的value使用相同的内存地址, 一个赋值, 所有内容都一样
		2. 
'''
def nested_dict(lists,idx): # 20230315092535
	if idx>0:
		lists = list(reversed(lists)) # 让最外层的keys和列表最左端的列表对应
		listpop = lists[idx]
		return {i:nested_dict(lists,idx-1) for i in listpop}
	else:
		listpop = lists[idx]
		return {i:[] for i in listpop}