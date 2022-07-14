
from setuptools import setup, find_packages

setup(
    name='tdd-in-python',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='',
    description='An example python package',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/mazzielafa/TDD-in-python.git',
    author='',
    author_email='myemail@example.com'
)


# twine upload --repository-url http://localhost:8081/repository/hosted-python/ dist/*

# twine upload  --repository-url http://localhost:8081/repository/hosted-python/ dist/* -uadmin -pPa55w.rd