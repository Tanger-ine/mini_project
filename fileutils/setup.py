from setuptools import setup, find_packages

setup(
    name='fileutils',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    author='Your Name',
    author_email='your@email.com',
    description='A utility library for file operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/fileutils',
    license='MIT',
)