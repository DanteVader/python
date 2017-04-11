from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import glob
import os

dir = "D:\SomeDir" # Dir where target files located at
os.chdir(dir)
build = glob.glob('run_test_build_*.zip') # Here give pattern to find your files
print build
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
for i in range(0,len(build)):
	print build[i]
	f = drive.CreateFile()
	f.SetContentFile(build[i])
	f.Upload()
	print 'title:%s, id:%s' % (f['title'], f['id']) # Print attributes of uploaded file (you can add some from PyDrive's list)

