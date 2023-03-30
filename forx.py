from itertools import product

from thehow.snips import constants
from thehow.snips import dictx
def func(*args):
	for i in args:
		print(i)

def nested_for(func,lists): # 20230330125323
	result = dictx.create_nested_dict(lists, len(lists)-1)
	for idx_seq in product(*lists):
		oneres = func(*idx_seq)
		dictx.dict_seqidx_setter()


if __name__ == '__main__':
	nested_for(func, constants.nested_dict_keylist)