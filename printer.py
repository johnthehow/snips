import inspect
from pathlib import Path
res1 = inspect.stack()[0][1]
res2 = inspect.stack()[0][3]
print(res1)
print(res2)