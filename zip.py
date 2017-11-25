#script to convert folders with pngs inside into pdf
#outpu folder_name.pdf
import shutil
import os
import sys
import subprocess

for name in os.listdir():
	if not name.endswith(".py"):
		pre, ext = os.path.splitext(name)
		output_filename = pre + ".pdf"
		print ('Creating "%s"...' % output_filename)
		os.system('magick convert %s/*.png "%s"' % (pre, output_filename))