import os

def listdir_full(directory):
	return [os.path.join(directory, file) for file in os.listdir(directory)]