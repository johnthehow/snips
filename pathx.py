from pathlib import Path

def resuffix(filename): # 20230329132438
	filepath = Path(filename)
	parent = filepath.parent
	stem = filepath.stem
	suffix = filepath.suffix
	resuffix_filename = stem+suffix+'.'+'proc'
	resuffix_filepath = parent.joinpath(resuffix_filename)
	return resuffix_filepath

