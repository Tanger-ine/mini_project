from setuptools import setup, find_packages

setup(
    name='pdappendunits',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    author='Tanger-ine',
    author_email='parak2065@gmail.com',
    description='A utility library for file operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Tanger-ine/mini_project/tree/main/fileutils',
    license='MIT',
)