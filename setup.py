from setuptools import setup

setup(
	name='clickstats',
	version='0.04',
	py_modules=['clickstats'],
	install_requires=['Click',],
	entry_points='''
		[console_scripts]
		clickstats=clickstats:calculate''',)