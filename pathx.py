from pathlib import Path

def resuffix(filename,suffix): # 20230329132438
	filepath = Path(filename)
	parent = filepath.parent
	stem = filepath.stem
	resuffix_filename = stem+suffix
	resuffix_filepath = parent.joinpath(resuffix_filename)
	return resuffix_filepath

