import inspect
from pathlib import PurePath
import sys
res = inspect.stack()[0][1]
res_parts = PurePath(inspect.stack()[0][1]).parts[5:]
syspaths = sys.path
candicate_roots = []
for i in syspaths:
	if i in res:
		cadidate_roots.append(i)

print(candicate_roots)
