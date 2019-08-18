from setuptools import setup

setup(name='secretsman',
      version='0.1',
      description='A secrets manager using os env or AWS SSM',
      url='http://github.com/linkai-io/secretsman',
      author='Isaac Dawson',
      license='MIT',
      packages=['secretsman'],
      install_requires=[
            'boto3==1.9.210',
            'botocore==1.12.210'
      ],
      zip_safe=True)