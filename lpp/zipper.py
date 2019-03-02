import zipfile
import os
import tempfile
import sys
import lpp.pmgr as pip

EXCLUSIONS = ['requirements.txt','README.md']

class ZipIt:

	def __init__(self):
		self.tmp = os.path.join(tempfile.gettempdir(),'lpp.zip')


	def zipdir(self,path):
		deps = pip.PIP(path)
		deps.build()
		zipf = zipfile.ZipFile(self.tmp, 'w', zipfile.ZIP_DEFLATED)
		# ziph is zipfile handle
		for root, dirs, files in os.walk(path):
			for file in files:
				zipf.write(
					os.path.relpath(
						os.path.join(root, file), os.path.join(path, '.')))
		for root, dirs, files in os.walk(deps.tmp):
			for file in files:
				zipf.write(
					os.path.relpath(
						os.path.join(root, file), os.path.join(deps.tmp, '.')))
		zipf.close()
		self.deldir()
		deps.destruct()
		return "Generated!"

	def deldir(self):
		os.remove(self.tmp)

if __name__ == '__main__':
	''''''
	# import tempfile
	# test = ZipIt() 
	# print(test.zipdir(r'C:\Users\jdelarosa\Google Drive\Repos\lambda-py-packager\lpp'))
	# print(test.deldir())
