from pathlib import Path

def resuffix(filename,suffix): # 20230329132438
	filepath = Path(filename)
	parent = filepath.parent
	stem = filepath.stem
	resuffix_filepath = parent.joinpath(stem).joinpath(suffix)
	return resuffix_filepath

