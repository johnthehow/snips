from itertools import product
from thehow.snips.constants import nested_dict_keylist
from thehow.snips.dictx import dict_seqidx_setter

'''
[函数注释]
	[功能]
		1. 主要功能: 将本来只能用于一组参数的函数, 变成能用于多组参数的函数
		2. 额外功能
	[设计图]
		1. 索引码: 
		2. 文件类型: 
	[参数]
		1. func
			1. 数据类型: function
			2. 数据结构: function
			3. 参数类型: 必选参数
			4. 语义: 希望变成能用于多组参数的函数的本来只能用于一组参数的函数
			5. 取值范围: 
			6. 获得来源: 手动输入
			7. 样例文件/输入: func = lambda f1,f2,v1,v2,v3,v4:(f1,f2,v1,v2,v3,v4)
		2. fix_para_list
			1. 数据类型: list
			2. 数据结构: [val,val]
			3. 参数类型: 必选参数
			4. 语义: 在函数中值固定不变的参数
			5. 取值范围: 
			6. 获得来源: 手动输入
			7. 样例文件/输入: fixpara = ['fix1','fix2']
			8. 注意事项: fix_para_list中的每一项, 不能是"不耐用"的生成器, 否则只有第一组参数会有结果
		3. nest_para_lists
			1. 数据类型: list
			2. 数据结构: [list,list]
			3. 参数类型: 必选参数
			4. 语义: 在函数中值不断改变,层层嵌套的参数
			5. 取值范围: 
			6. 获得来源: 手动输入
			7. 样例文件/输入: nested_paras = thehow.snips.constants.nested_dict_keylist
	[用例]
		1. paralize_nest(func, fixpara, nested_paras)
			1. 输出
				1. 语义: 对应所有变化嵌套参数组合的结果字典
				2. 数据类型: dict
				3. 数据结构: {key:{key:val}}
				4. 样例文件/输出: 20230330152632.txt
	[依赖]
		1. thehow.snips.dictx.create_nested_dict # 20230315092535
		2. thehow.snips.dictx.dict_seqidx_setter # 20230316182821
		3. itertools.product
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
def paralize_nest(func, fix_para_list, nest_para_lists): # 20230330150547
	result = create_nested_dict(nest_para_lists, len(nest_para_lists)-1)
	for seq_idx in product(*nest_para_lists):
		one_result = func(*fix_para_list,*seq_idx)
		dict_seqidx_setter(result,seq_idx,one_result)
	return result