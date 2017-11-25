import shutil
import os
for folder in os.listdir():
	for subfolder in folder:
		print(folder)
		#if not name.endswith("py"):
		#	shutil.make_archive(name, 'zip', name)