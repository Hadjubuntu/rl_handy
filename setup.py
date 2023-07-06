from setuptools import setup, find_packages
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rl_handy',
    version='0.1',
    url='https://github.com/Hadjubuntu/rl_handy',
    author='Adrien Hadj-Salah',
    author_email='adrien.hadj.salah@gmail.com',
    description='Reinforcement Learnin applied to Human and nature dynamics (HANDY) model',
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'numpy==1.18.1',
        'gym==0.15.4',
        'baselines==0.1.5',
        'pytest==5.2.2',
        'matplotlib==3.1.2',
        'scipy==1.10.0',
        'jupyter==1.0.0'],
)
