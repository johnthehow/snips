import argparse

def simple_args(*args):
	parser = argparse.ArgumentParser()
	for i in args:
		parser.add_argument(i)
	res_args = parser.parse_args()
	return res_args

