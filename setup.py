from setuptools import find_packages, setup
setup(
    name='agrostardb',
    packages=find_packages(include=['agrostardb']),
    version='0.1.0',
    description='farmer library',
    author='Me',
    license='MIT',
    install_requires=['django','djangorestframework','mysqlclient'],
    setup_requires=[],
    test_suite='tests',
)