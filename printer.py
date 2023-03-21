import inspect
from pathlib import PurePath
import sys

def module_ref():
	res = inspect.stack()[1][1].lower()
	syspaths = [i.lower() for i in sys.path[1:]]
	candicate_roots = []
	for i in syspaths:
		if i in res:
			candicate_roots.append(i)
	root = max(candicate_roots, key=len)
	remain = res.replace(root,'').replace('\\','/')
	remain_parts = PurePath(remain).parts
	# print('.'.join(remain_parts[1:])[:-3])
	return '.'.join(remain_parts[1:])[:-3]


print(module_ref())