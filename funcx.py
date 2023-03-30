from itertools import product

def paraseq(func,paralists): # 20230330150547
	for seq_idx in product(*paralists):
		print(seq_idx)