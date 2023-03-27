import os
from pathlib.path import Path

def listdir_full(directory):
	return [os.path.join(directory, file) for file in os.listdir(directory)]