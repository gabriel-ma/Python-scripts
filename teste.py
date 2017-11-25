#script to change file format from jfif to jpg
import os

for name in os.listdir("."):
	if name.endswith(".jfif"):
		pre, ext = os.path.splitext(name)
		os.rename(name, pre + ".jpg")
