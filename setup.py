from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='reporting',
    version='1.0',
    packages=find_packages(),
    package_dir={'': 'bin/automated_report_tool'},
    install_requires=[
          'cx_oracle~=8.1.0',
	  'pandas~=1.0.1',
	  'openpyxl~=3.0.5',
	  'setuptools~=45.2.0'
    ],
    url='https://github.com/nikhleshagrawal/reporting_util',
    license='',
    author='nikhleshagrawal',
    author_email='nikhlesh.agrawal@gmail.com',
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent"
    ],
    description='Reporting utility tool',
    long_description=long_description,
    long_description_content_type="text/markdown"
)
