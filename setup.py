

from setuptools import setup, find_packages


setup(

    name='fanfic-crawler',
    version='0.1.0',
    description='Harry Potter fan fiction.',
    url='https://github.com/davidmcclure/fanfic-crawler',
    license='MIT',
    author='David McClure',
    author_email='dclure@stanford.edu',
    packages=find_packages(),
    scripts=['bin/fanfic'],

)
