def main():
        from tkinter import filedialog
	import json
	from pathlib import Path
	import rdbtools

	dir=False
	result=list()

	while dir==False:
		dir=filedialog.askdirectory()

	for p in Path(dir).glob('*.json'):
		with p.open() as infile:
			result.extend(json.load(infile))

	with open('dump.json', 'w') as output_file:
		json.dump(result, output_file)

if __name__=="__main__":
	main()
