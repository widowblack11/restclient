from setuptools import setup
REQUIRES = [
    'requests',
    'allure',
    'curlify',
    'structlog'
]

setup(
    name='restclient',
    version='0.0.1',
    packages=['restclient'],
    url='https://github.com/widowblack11/restclient.git',
    license='MIT',
    author='oksanaprokopenko',
    author_email='-',
    istall_requires=REQUIRES,
    description='restclient with allure and logger'
)
