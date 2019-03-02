import sys
import lpp.zipper as z
import boto3


class LambdaPackager:


	def __init__(self):
		self.action = sys.argv[1]
		self.function_name = sys.argv[2]
		self.repo_path = sys.argv[3]
		self.action = sys.argv[1]
		_switch = {
		'update':self.update,
		'create':self.create,
		'delete':self.delete}
		_switch[self.action]()

	def update(self):
		lmd = z.ZipIt()
		lmd.zipdir(self.repo_path)
		lmd.update(self.function_name)
		# lmd.deldir()


	def create(self):
		return

	def delete(self):
		return


def main():
	LambdaPackager()

if __name__ == '__main__':
	sys.argv = ['lpp','update', 'spies-litter', r'C:\Users\jdelarosa\Google Drive\Repos\lambda-py-packager\lpp']
	print(main())