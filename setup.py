from setuptools import setup

setup(
    name = "lambda-py-packager",
    version = "0.1",
    install_requires = [
        'boto3 >= 1.9.1'
    ],
    packages = ['lambda-py-packager'],
    entry_points = {
        'console_scripts': ['lpp = packager.handler:main'],
    }
)