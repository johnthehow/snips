from itertools import product
from thehow.snips.constants import nested_dict_keylist
def paraseq(func,paralists): # 20230330150547
	for seq_idx in product(*paralists):
		print(seq_idx)
def func(*args):
	for i in funcs:
		print(i)

if __name__ == '__main__':
	paraseq(func, nested_dict_keylist)