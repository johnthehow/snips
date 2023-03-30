import os
from pathlib import Path

'''
[函数注释]
	[功能]
		1. 主要功能: 列出一个目录中所有文件的完整路径
		2. 额外功能
	[设计图]
		1. 索引码: 
		2. 文件类型: 
	[参数]
		1. directory
			1. 数据类型: string, pathlib.Path
			2. 数据结构: string, pathlib.Path
			3. 参数类型: 必选参数
			4. 语义: 路径
			5. 取值范围: 
			6. 获得来源: 手动输入
			7. 样例文件/输入: r'D:/test'
	[用例]
		1. listdir_full(r'D:/test')
			2. 输出
				1. 语义: 一个目录中所有文件的完整路径
				2. 数据类型: list
				3. 数据结构: [str,str]
				4. 样例文件/输出: 
	[依赖]
		1. pathlib.Path
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
def listdir_full(directory): # 20230330153344
	return [Path(directory).joinpath(file) for file in os.listdir(directory)]