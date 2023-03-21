import inspect
from pathlib import PurePath
import sys
res = inspect.stack()[0][1]
res_parts = PurePath(inspect.stack()[0][1]).parts[5:]
syspaths = sys.path[1:]
candicate_roots = []
for i in syspaths:
	if i in res:
		candicate_roots.append(i)
root = max(candicate_roots, key=len)

print(candicate_roots)
print(syspaths)
print(root)
