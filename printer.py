import inspect
from pathlib import PurePath
import sys
res = inspect.stack()[0][1]
res_parts = PurePath(inspect.stack()[0][1]).parts[5:]
print(res)
