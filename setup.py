# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
setup(
    name='BMI_Index',
    packages=find_packages(),
    version='1.0.0',
    include_package_data=True,
    setup_requires=["wheel"],
    install_requires=[
        'pandas==0.23.4',
        'pandas==0.23.4',
        'numpy==1.15.4',
       ]
)