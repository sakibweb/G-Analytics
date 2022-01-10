import sys
import subprocess
from setuptools import setup

print('''
    name='G-Analytics',
    version='4.0',
    packages=['G-Analytics'],
    url='https://github.com/sakibweb/G-Analytics',
    license='GNU General Public License v3.0',
    author='SAKIB',
    author_email='sakib.sr20@gmail.com',
    description='G-Analytics Easy Way To Monetize Your GIG Script : V4 | Develop By : Sakibur Rahman'
'''
)

subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

print('''
    name='G-Analytics',
    version='4.0',
    packages=['G-Analytics'],
    url='https://github.com/sakibweb/G-Analytics',
    license='GNU General Public License v3.0',
    author='SAKIB',
    author_email='sakib.sr20@gmail.com',
    description='G-Analytics Easy Way To Monetize Your GIG Script : V4 | Develop By : Sakibur Rahman'
'''
)

subprocess.check_call([sys.executable, 'G-Analytics.py'])
