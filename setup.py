"""
Python setup file for Docker build
"""

from setuptools import find_packages
from setuptools import setup

setup(
    name='simple-pipeline',
    description="Flask Python App to learn CI/CD using GitHub Actions",
    author='Drathion',
    url='',
    packages=find_packages('src'),
    package_dir={
        '': 'src'},
    include_package_data=True,
    keywords=[
        'web_app', 'test', 'flask'
    ],
    entry_points={
        'console_scripts': [
            'web_server = app:main']},
)
