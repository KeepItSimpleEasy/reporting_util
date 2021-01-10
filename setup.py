from setuptools import setup

setup(
    name='reporting',
    version='1.0',
    packages=[''],
    package_dir={'': 'bin/automated_report_tool'},
    url='https://github.com/nikhleshagrawal/reporting_util',
    license='',
    author='nikhleshagrawal',
    author_email='nikhlesh.agrawal@gmail.com',
    description='This is utility tool which reads a config file and does the following for you - Runs a query in oracle database, Create an excel file, Zip the excel file, Send an email with the attachment to configured recipients, archive the xlsx and zip file'
)
