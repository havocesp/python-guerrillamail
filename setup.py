from setuptools import setup
from codecs import open


with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name='python-guerrillamail',
    version='0.2.0',
    description='Client for the Guerrillamail temporary email server',
    long_description=readme + '\n\n' + history,
    keywords='guerrillamail email client cli',
    author='Nathan Jones',
    url='https://github.com/ncjones/python-guerrillamail',
    py_modules=['guerrillamail'],
    install_requires=[
        'requests',
        "security==1.3.0",
    ],
    license='GPL3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    entry_points={
        'console_scripts': [
            'guerrillamail=guerrillamail:main',
        ],
    }
)
