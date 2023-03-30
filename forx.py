from itertools import product
from thehow.snips import constants

def nested_loop(func,lists): # 20230330125323
	for idx_seq in product(*lists):
		print(idx_seq)


if __name__ == '__main__':
	nested_loop('hello', constants.nested_dict_keylist)