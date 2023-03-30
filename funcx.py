from itertools import product
from thehow.snips.constants import nested_dict_keylist

'''
[函数注释]
	[功能]
		1. 主要功能: 将本来需要手动输入一个
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
def paraseq(func,fix_para_list,nest_para_lists): # 20230330150547
	for seq_idx in product(*nest_para_lists):
		func(fix_para,*seq_idx)

func = lambda f,a,b,c,d:print(f,a,b,c,d)

if __name__ == '__main__':
	paraseq(func, 3, nested_dict_keylist)