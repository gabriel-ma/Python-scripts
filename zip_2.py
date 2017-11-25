#new version of zip.py
import shutil
import os
for folder in os.listdir():
	if not folder.endswith("py"):
		for subfolder in os.listdir(folder):
			shutil.make_archive(folder+"/"+subfolder, 'zip', folder+"/"+subfolder)