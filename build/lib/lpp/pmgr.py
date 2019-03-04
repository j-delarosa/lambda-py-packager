from pip._internal import main as _main
import os
import tempfile
import shutil

class PIP:


	def __init__(self,path):
		self.tmp = os.path.join(tempfile.gettempdir(),'lpp')
		self.file = os.path.join(path,'requirements.txt')
		os.mkdir(self.tmp)
		self.build()
		# self.destruct()


		''''''

	def build(self):
		''''''
		print(_main(['install','-r',self.file,'-t',self.tmp]))

	def destruct(self):
		shutil.rmtree(self.tmp)

# PIP(r'C:\Users\jdelarosa\Google Drive\Repos\rubix-ocr')