import sympy

'''
[函数注释]
	[功能]
		1. 主要功能: 生成用于实验的符号矩阵, 内容是a11, a12这样的元素
		2. 额外功能
	[设计图]
		1. 索引码: 
		2. 文件类型: 
	[参数]
		1. head
			1. 数据类型: string
			2. 数据结构: string
			3. 参数类型: 必选
			4. 语义: 矩阵中元素的代表字母
			5. 取值范围: 
			6. 获得来源: 手动输入
			7. 样例文件/输入: 'a', 'b','c'
		2. nrow
			1. 数据类型: int
			2. 数据结构: int
			3. 参数类型: 必选
			4. 语义: 矩阵的行数
			5. 取值范围: 1~9
			6. 获得来源: 手动输入
			7. 样例文件/输入: 3
		3. ncol
			1. 数据类型: int
			2. 数据结构: int
			3. 参数类型: 必选
			4. 语义: 矩阵的列数
			5. 取值范围: 1~9
			6. 获得来源: 手动输入
			7. 样例文件/输入: 5
		4. start_ridx
			1. 数据类型: int
			2. 数据结构: int
			3. 参数类型: 必选
			4. 语义: 矩阵中最左上角元素的行标, 主要用于表现矩阵分块法
			5. 取值范围: 1~9
			6. 获得来源: 手动输入
			7. 样例文件/输入: 5
		4. start_cidx
			1. 数据类型: int
			2. 数据结构: int
			3. 参数类型: 必选
			4. 语义: 矩阵中最左上角元素的列标, 主要用于表现矩阵分块法
			5. 取值范围: 1~9
			6. 获得来源: 手动输入
			7. 样例文件/输入: 5
	[用例]
		1. A = sympyx.demo_matrix('a',3,4,2,2)
			1. 输出
				1. 语义: 生成的用于实验的符号矩阵, 每个元素的代表字母是a, 矩阵3行4列, 最左上角元素是a22
				2. 数据类型: sympy.matrices.dense.MutableDenseMatrix
				3. 数据结构: sympy.matrices.dense.MutableDenseMatrix
				4. 样例文件/输出: 20230417011844.pkl
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
def demo_matrix(head,nrow,ncol,start_ridx=1,start_cidx=1):
	container = sympy.zeros(nrow,ncol) # 结果容器
	for r,i in enumerate(range(start_ridx,start_ridx+nrow)):
		for c,j in enumerate(range(start_cidx,start_cidx+ncol)):
			sym = f'{head}{i}{j}'
			var = f'{head}{i}{j}'
			state = f'{var}=sympy.symbols("{sym}")'
			exec(state)
			container[r:c] = sym
	return container