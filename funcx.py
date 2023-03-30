from itertools import product
from thehow.snips.constants import nested_dict_keylist

def paraseq(func,paralists): # 20230330150547
	for seq_idx in product(*paralists):
		func(*seq_idx)

func = lambda a,b,c,d:print(a,b,c,d)

if __name__ == '__main__':
	paraseq(func, nested_dict_keylist)