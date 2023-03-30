from itertools import product
from thehow.snips.constants import nested_dict_keylist
def paraseq(func,paralists): # 20230330150547
	for seq_idx in product(*paralists):
		print(seq_idx)