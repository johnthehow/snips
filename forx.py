from itertools import product

def nested_loop(func,lists): # 20230330125323
	for idx_seq in product(*lists):
		print(idx_seq)