''' 
[模块注释] 20230315113144
	[功能]
		1. 为dict类添加更多功能
	[发展计划]
		1. 将该模块中的函数继承到python内建dict类中
		2. 
'''


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
			1. 语义: 嵌套字典的层数(即有多少层key)
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
    return max(dict_depth(v) if isinstance(v,dict) else 0 for v in dic.values()) + 1



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
			8. 样例文件/输入: lsts = [[1,2,3,4],['a','b','c','d'],['甲','乙','丙','丁'],['α','β','γ','δ']]
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
			4. 样例文件/输出:
				1. 样例1
					1. 环境: 20230315213038
					2. 输入: lsts = [[1,2,3,4],['a','b','c','d'],['甲','乙','丙','丁'],['α','β','γ','δ']]
					3. 语句: nested_dict(lsts, 3)
					4. 输出: 20230315212857
	[已知问题]
		1. [问题1]
			1. 问题描述:
			2. 问题复现
				1. 复现环境
				2. 复现语句
				3. 复现存档
	[开发计划]
		1. 计划省去第二个参数
		2.
	[备注]
		1. 不采用fromkeys方法是因为该方法生成的字典的value使用相同的内存地址, 一个赋值, 所有内容都一样
		2. 字典key顺序和列表顺序相反
'''
def nested_dict(lists,idx): # 20230315092535
	if idx>0:
		listpop = lists[idx]
		return {i:nested_dict(lists,idx-1) for i in listpop}
	else:
		listpop = lists[idx]
		return {i:[] for i in listpop}


'''
[函数注释] 20230312003819
	[功能]
		1. 主要功能: 用tuple或者list作为dict的下标索引字典, 返回其值
		2. 额外功能
	[参数]
		1. dic
			1. 数据类型: dict
			2. 数据结构: {key:{key:{key:[]}}}
			3. 参数类型: 必选
			4. 语义: 被索引的字典(嵌套字典)
			5. 默认值:
			6. 取值范围:
			7. 获得来源: 手动输入
			8. 样例文件/输入: 20230316004113
		2. seq_idx
			1. 数据类型: tuple/list
			2. 数据结构: tuple/list
			3. 参数类型: 必选
			4. 语义: 索引字典的下标
			5. 默认值:
			6. 取值范围:
			7. 获得来源: 手动输入
			8. 样例文件/输入: seq_idx = ('γ','乙','c',2)
	[输出]
		1. 默认输出
			1. 语义: 字典的对应下标的值
			2. 数据类型:
			3. 数据结构:
			3. 样例文件/输出:
	[用例]
		1. [用例1]
			1. 语义:
			2. 语句:
			3. 输出样例
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
		1.
		2. 
'''
def dict_seqidx_getter(dic,seq_idx): # 20230312003819
	len_tup_idx = len(seq_idx)
	idx_popout = seq_idx[0]
	inner_dic = dic[idx_popout] # 读取内层字典
	seq_idx = seq_idx[1:] # 更新tup
	if len_tup_idx>1:
		return dict_seqidx_getter(inner_dic,seq_idx)
	else:
		return inner_dic

'''
[函数注释]
	[功能]
		1. 主要功能: 以tuple或者list为下标, 设置字典的值
		2. 额外功能
	[设计图]
		1. 存储位置:
		2. 索引码:
		3. 文件类型:
	[参数]
		1. dic
			1. 数据类型: dict
			2. 数据结构: {key:{key:value}}
			3. 参数类型: 必选参数
			4. 语义: 被设置值的嵌套字典
			5. 默认值:
			6. 取值范围: 
			7. 获得来源: 手动输入
			8. 样例文件/输入: 20230319003657
		2. seq_idx
			1. 数据类型: tuple/list
			2. 数据结构: tuple/list
			3. 参数类型: 必选参数
			4. 语义: 作为字典下标的list或tuple
			5. 默认值:
			6. 取值范围:
			7. 获得来源: 手动输入
			8. 样例文件/输入: idx = ('β','甲','d',1)
	[输出]
		1. 默认输出
			1. 语义: 设置了值的嵌套字典
			2. 数据类型: dict
			3. 数据结构: {key:{key:value}}
			3. 样例文件/输出: 20230319003936
	[用例]
		1. [用例1]
			1. 语义: 以tuple或者list为下标, 设置字典的值
			2. 语句: res = dict_seqidx_setter(20230319003657, ('β','甲','d',1), '--------' )
			3. 输出样例: 20230319003936
	[依赖]
		1. 
		2. 
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
		1.
		2. 
'''
def dict_seqidx_setter(dic,seq_idx,val): # 20230316182821
	len_tup_idx = len(seq_idx)
	idx_popout = seq_idx[0] # 取下标第一个值
	if len_tup_idx>1:
		inner_dic = dic[idx_popout] # 进入内层字典, 作为下一层递归的输入
		seq_idx = seq_idx[1:] # 除去下标第一个值, 作为下一轮递归的输入
		return dict_seqidx_setter(inner_dic,seq_idx,val)
	else:
		idx_popout = seq_idx[0]
		dic[idx_popout] = val
		return dic