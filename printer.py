import inspect
from pathlib import PurePath
res = PurePath(inspect.stack()[0][1]).parts
print(res)
