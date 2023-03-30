from itertools import product
from thehow.snips import constants

def func(*args):
	for i in args:
		print(i)

def nested_loop(func,lists): # 20230330125323
	for idx_seq in product(*lists):
		func(*idx_seq)


if __name__ == '__main__':
	nested_loop(func, constants.nested_dict_keylist)