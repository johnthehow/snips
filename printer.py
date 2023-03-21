import inspect
from pathlib import PurePath
import sys
res = inspect.stack()[0][1].lower()
res_parts = PurePath(inspect.stack()[0][1]).parts[5:]
syspaths = [i.lower() for i in sys.path[1:]]
candicate_roots = []
for i in syspaths:
	if i in res:
		candicate_roots.append(i)
root = max(candicate_roots, key=len)
remain = res.replace(root,'').replace('\\','/')
remain_parts = PurePath(remain).parts
print(candicate_roots)
print(syspaths)
print(root)
print(remain)
print(remain_parts)
