import os
from pathlib import Path

def listdir_full(directory):
	return [Path(directory).joinpath(file) for file in os.listdir(directory)]