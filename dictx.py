''' 
[模块注释] 20230315113144
	[功能]
		1. 为dict类添加更多功能
	[发展计划]
		1. 将该模块中的函数继承到python内建dict类中
		2. 第三方库munch能够将嵌套字典对象化, 缺点是当key是数字时, 无法对象化
	[实验用变量]
		20230320173143; lst = [['α', 'β', 'γ', 'δ'], ['甲', '乙', '丙', '丁'], ['甲', '乙', '丙', '丁'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], [1, 2, 3, 4], [1, 2, 3, 4]]
		20230320173529; dic1 = {'α': {'甲': {'a': {1: [11,23], 2: [], 3: [23,77], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '乙': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '丙': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '丁': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}}, 'β': {'甲': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '乙': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '丙': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '丁': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}}, 'γ': {'甲': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '乙': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '丙': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '丁': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}}, 'δ': {'甲': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '乙': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '丙': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '丁': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}}}
		20230320173532; dic2 = {'α': {'甲': {'a': {1: [43,96], 2: [], 3: [111], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '乙': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '丙': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '丁': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}}, 'β': {'甲': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '乙': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '丙': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '丁': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}}, 'γ': {'甲': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '乙': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '丙': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '丁': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}}, 'δ': {'甲': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '乙': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '丙': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}, '丁': {'a': {1: [], 2: [], 3: [], 4: []}, 'b': {1: [], 2: [], 3: [], 4: []}, 'c': {1: [], 2: [], 3: [], 4: []}, 'd': {1: [], 2: [], 3: [], 4: []}}}}
		20230320173157; dicts = [dic1,dic2]

'''
from itertools import product
import inspect

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
					2. 输入: lsts = [['α','β','γ','δ'],['甲','乙','丙','丁'],['a','b','c','d'],[1,2,3,4]]
					3. 语句: create_nested_dict(lsts, 3)
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
'''
def create_nested_dict(lists,idx): # 20230315092535
	lists = list(reversed(lists))
	def rec(lists,idx): # 20230315092535
		if idx>0:
			listpop = lists[idx]
			return {i:rec(lists,idx-1) for i in listpop}
		else:
			listpop = lists[idx]
			return {i:[] for i in listpop}
	return rec(lists, idx)


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

'''
[函数注释]
	[功能]
		1. 主要功能: 从嵌套字典中提取出, 各级key, 并以列表的方式存储, 是dict.from_keys()的反函数
		2. 额外功能
	[设计图]
		1. 存储位置:
		2. 索引码:
		3. 文件类型:
	[参数]
		1. [参数1]
			1. 数据类型:
			2. 数据结构:
			3. 参数类型:
			4. 语义:
			5. 默认值:
			6. 取值范围:
			7. 获得来源:
			8. 样例文件/输入:
		2. [参数2]
			1. 数据类型:
			2. 数据结构:
			3. 参数类型:
			4. 语义:
			5. 默认值:
			6. 取值范围:
			7. 获得来源:
			8. 样例文件/输入: 
	[输出]
		1. 默认输出
			1. 语义:
			2. 数据类型:
			3. 数据结构:
			3. 样例文件/输出:
		2. [条件输出1]
			1. 语义:
			2. 数据结构:
			3. 样例文件/输出:
	[用例]
		1. [用例1]
			1. 语义:
			2. 语句:
			3. 输出样例
	[依赖]
		1. 
		2. 
	[已知问题]
		1. 当每个最高层下的dict下的每个dict的key不是完全相同时, 提取出的keys不能反应各个dict的结构
			2. 问题复现
				1. 复现环境
				2. 复现语句
					1. extract_keylists(dicts[0])
				3. 复现存档
					1. 输入: dicts = 20230426213514.pkl
					2. 输出: keylists = 20230426213634.pkl
	[开发计划]
		1. 拟改名为dict_to_keys
		2.
	[备注]
		1.
		2. 
'''
def extract_keylists(dic): # 20230320151046
	keylists = []
	def uniq_lists(lists):
		res = []
		def reducer(lists):
			if len(lists)>1:
				# print(lists[0])
				res.append(lists[0])
				lists = [j for j in lists if j!=lists[0]]
				return reducer(lists)
			else:
				if lists != []:
					res.append(lists)
		reducer(lists)
		return res
	def extractor(dic):
		keylists.append(list(dic.keys()))
		for i in dic.values():
			if isinstance(i, dict):
				keylists.append(list(i.keys()))
				return extractor(i)
			else:
				pass
	extractor(dic)
	keylists = uniq_lists(keylists)
	return keylists


'''
[函数注释]
	[功能]
		1. 主要功能: 清空前套字典最后一层的值为空列表(原地生效)
		2. 额外功能
	[设计图]
		1. 索引码: 
		2. 文件类型: 
	[参数]
		1. [参数1]
			1. 数据类型: dict
			2. 数据结构: {key:{key:key:[val,val]}}
			3. 参数类型: 必选参数
			4. 语义: 被清空的字典
			5. 取值范围: 
			6. 获得来源: 手动输入
			7. 样例文件/输入: dict2vac = {'1': {'a': {'α': [7, 9, 7]}, 'b': {'α': [1, 3, 2], 'β': []}}, '2': {'a': {'α': [], 'β': []}, 'b': {'α': [], 'β': [], 'γ': []}}, '3': {'a': {'α': [], 'β': [], 'δ': [3, 9, 2]}}}
	[用例]
		1. [用例1]
			1. 语句: vacate_dict(dict2vac)
			2. 输出
				1. 语义: 被清空至只剩框架的字典
				2. 数据类型: dict
				3. 数据结构: {key:{key:key:[]}}
				4. 样例文件/输出: {'1': {'a': {'α': []}, 'b': {'α': [], 'β': []}}, '2': {'a': {'α': [], 'β': []}, 'b': {'α': [], 'β': [], 'γ': []}}, '3': {'a': {'α': [], 'β': [], 'δ': []}}}
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
		1. 完全由CHATGPT-4编写, 聊天记录 20230619021552.txt
		2. 
'''
def vacate_dict(dic): # 20230619021107
    for k, v in dic.items():
        if isinstance(v, dict):
            empty_lists(v)
        elif isinstance(v, list) and v:
            dic[k] = []

'''
[函数注释]
	[功能]
		1. 主要功能: 合并结构相同的嵌套字典们(而不是像dict.update那样拼接)
		2. 额外功能
	[设计图]
		1. 存储位置:
		2. 索引码:
		3. 文件类型:
	[参数]
		1. dicts
			1. 数据类型: list
			2. 数据结构: [dict,dict]
			3. 参数类型: 必选参数
			4. 语义: 结构相同的嵌套字典的列表
			5. 默认值:
			6. 取值范围:
			7. 获得来源: 手动输入
			8. 样例文件/输入: 本文件:20230320173157
	[输出]
		1. 默认输出
			1. 来源语句: merge_dicts(dicts)
			2. 语义: 合并结构相同的嵌套字典们(而不是像dict.update那样拼接)
			3. 数据类型: dict
			4. 数据结构: {key:{key:[val,val]}}
			5. 样例文件/输出: 
	[依赖]
		1. 
		2. 
	[已知问题]
		1. 深层的dict的keys不全
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
def merge_dicts(dicts): # 20230321190735
	if len(dicts) == 0:
		print(f'[{inspect.stack()[0][3]}] No dict get')
	keylists = extract_keylists(dicts[0]) # 用于生成空的结果承载嵌套字典的keylist
	empty_nested_dict = create_nested_dict(keylists, len(keylists)-1) # # 空的结果承载嵌套字典
	for i in product(*keylists):
		single_res = []
		for d in dicts:
			single_res += dict_seqidx_getter(d, i)
		dict_seqidx_setter(empty_nested_dict, i, single_res)
	return empty_nested_dict


'''
[函数注释]
	[功能]
		1. 主要功能: 按照key排序字典
		2. 额外功能
	[设计图]
		1. 索引码: 
		2. 文件类型: 
	[参数]
		1. dic
			1. 数据类型: dict
			2. 数据结构: dict
			3. 参数类型: 必选
			4. 语义: 被按照key排序的字典
			5. 取值范围: 
			6. 获得来源: 手动输入
			7. 样例文件/输入: dic  = {'c':2,'b':1,'a':4}
	[用例]
		1. sort_dict_by_key(dic)
			1. 输出
				1. 语义: 排序后的字典
				2. 数据类型: dict
				3. 数据结构: dict
				4. 样例文件/输出: {'a': 4, 'b': 1, 'c': 2}
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
def sorted_dict_by_key(dic): # 20230403112258
	return {k: v for k, v in sorted(dic.items(), key = lambda kv: kv[0])}

'''
[函数注释]
	[功能]
		1. 主要功能: 按照key排序字典
		2. 额外功能
	[设计图]
		1. 索引码: 
		2. 文件类型: 
	[参数]
		1. dic
			1. 数据类型: dict
			2. 数据结构: dict
			3. 参数类型: 必选
			4. 语义: 被按照key排序的字典
			5. 取值范围: 
			6. 获得来源: 手动输入
			7. 样例文件/输入: dic  = {'c':2,'b':1,'a':4}
	[用例]
		1. sort_dict_by_key(dic)
			1. 输出
				1. 语义: 排序后的字典
				2. 数据类型: dict
				3. 数据结构: dict
				4. 样例文件/输出: {'b': 1, 'c': 2, 'a': 4}
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
def sorted_dict_by_val(dic): # 20230403112733
	return {k: v for k, v in sorted(dic.items(), key = lambda kv: kv[1])}