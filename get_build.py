from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import glob
import os

dir = "D:\SomeDir" # Dir where target files located at
os.chdir(dir)

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def ListOfFiles(directory):
	list=[]
	file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % directory}).GetList()
	print len(file_list)
	i = 0
	for i in range(0, len(file_list)):
		for f in file_list:
			list.append(f[u'title'])
			f.GetContentFile(list[i])
		print list[i]
	return list

directory = 'root' # The 'directory' is the folder name on google drive to search files in.
ListOfFiles(directory)
