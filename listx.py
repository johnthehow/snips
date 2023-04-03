''' 
[模块注释] 20230320174135
	[功能]
		1. 为list类添加更多功能
	[发展计划]
		1. 将该模块中的函数继承到python内建list类中
		2. 
	[实验用变量]
		20230320174456; redlist = [1,2,2,2,3,4,4,5,6,7]
		20230320174800; [1, 3, 4, 4, 5, 6, 7]
		20230320175057; lst = [['α', 'β', 'γ', 'δ'], ['甲', '乙', '丙', '丁'], ['甲', '乙', '丙', '丁'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], [1, 2, 3, 4], [1, 2, 3, 4]]
	[备注]
		1. 重新发明轮子之前, 看看有没有现成的, 比如collections.deque就是一种list的变种
		2. 应当扩充collections.UserList类, 而不是在这里写独立的函数
'''

'''
[函数注释]
	[功能]
		1. 主要功能: 删除一个列表中所有的指定值(list默认的remove方法只会移除第一个)
		2. 额外功能
	[设计图]
		1. 存储位置:
		2. 索引码:
		3. 文件类型:
	[参数]
		1. lst
			1. 数据类型: list
			2. 数据结构: list
			3. 参数类型: 必选
			4. 语义: 待被处理的列表
			5. 默认值:
			6. 取值范围:
			7. 获得来源: 手动输入
			8. 样例文件/输入: 本文件: 20230320174456
	[输出]
		1. 默认输出
			0. 语句: remove_all(redlist, 2)
			1. 语义: 删除redlist列表中所有的2
			2. 数据类型: list
			3. 数据结构: list
			3. 样例文件/输出: 本文件: 20230320174800
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
def remove_all(lst,val): # 20230320174224
	return [i for i in lst if i != val]

'''
[函数注释]
	[功能]
		1. 主要功能: 值保留列表中的唯一值, 仅支持列表元素为列表, 列表元素为一般元素时, 直接将列表转为set即可(注意set没有顺序)
		2. 额外功能
	[设计图]
		1. 存储位置:
		2. 索引码:
		3. 文件类型:
	[参数]
		1. lst
			1. 数据类型: list
			2. 数据结构: [[val,val],[val,val]]
			3. 参数类型: 必选
			4. 语义: 待被处理的嵌套列表
			5. 默认值: 
			6. 取值范围:
			7. 获得来源: 手动输入
			8. 样例文件/输入: 本文件: 20230320175057
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
def uniq_list(nested_list): # 20230320182636
	res = []
	def reducer(nested_list):
		if len(nested_list)>1:
			res.append(nested_list[0])
			nested_list = [j for j in nested_list if j!=nested_list[0]]
			return reducer(nested_list)
		else:
			if nested_list != []:
				res.append(nested_list)
	reducer(nested_list)
	return res

'''
[函数注释]
	[功能]
		1. 主要功能: 在一个列表中搜寻一个子列表, 并返回资料表的起止位置
		2. 额外功能
	[设计图]
		1. 索引码: 
		2. 文件类型: 
	[参数]
		1. sublist
			1. 数据类型: list
			2. 数据结构: list
			3. 参数类型: 必选
			4. 语义: 搜素的目标字列表
			5. 取值范围: 
			6. 获得来源: 手动输入
			7. 样例文件/输入: [2,3,4]
		2. lst
			1. 数据类型: list
			2. 数据结构: list
			3. 参数类型: 必选参数
			4. 语义: 被搜索的列表
			5. 取值范围: 
			6. 获得来源: 手动输入
			7. 样例文件/输入: [1,2,3,4,5,2,3,4,5,6]
	[用例]
		1. [用例1]
			1. 语句: locate_sublist([2,3,4], [1,2,3,4,5,2,3,4,5,6])
			2. 输出
				1. 语义: 出现字列表的位置
				2. 数据类型: list
				3. 数据结构: [(val,val),(val,val)]
				4. 样例文件/输出: [(1, 3), (5, 7)]
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
def locate_sublist(sublist,lst): # 20230320183807
    results = []
    sublist_len = len(sublist)
    for idx in (i for i,e in enumerate(lst) if e == sublist[0]):
        if lst[idx:idx+sublist_len]==sublist:
            results.append((idx,idx+sublist_len-1))
    return results


'''
[函数注释]
	[功能]
		1. 主要功能: 判断一个序列是否是另一个序列的子序列
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
def is_sublist(sublist,lst): # 20230403113339
	return any(sublist == lst[i:len(sublist) + i] for i in range(len(lst) - len(sublist) + 1))