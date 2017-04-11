#!/usr/bin/env python
import os
import zipfile
import glob

# dir = os.getcwd()
# print dir
dir = "D:\SomeDir"
os.chdir(dir)

build_stage = glob.glob('pattern[0-9]*.zip')
print build_stage
build_qa = glob.glob('pattern[0-9]*.zip')
print build_qa
try:
	with open(build_qa[0], 'rb') as fileobj:
		z = zipfile.ZipFile(fileobj)
		z.extractall(dir)
		z.close()
	os.remove(build_qa[0])
except Exception:
	pass
	print "QA zip not found"
# try:
# 	with open(build_stage[0], 'rb') as fileobj:
# 		z = zipfile.ZipFile(fileobj)
# 		z.extractall(dir)
# 		z.close()
# 	os.remove(build_stage[0])
# except Exception:
# 	pass
# 	print "Stage zip not found"
