from setuptools import setup

setup(name='battlerite-client',
      version='0.1',
      description='Battlerite REST API client',
      url='https://github.com/DrPandemic/battlerite-client',
      author='DrPandemic',
      license='MIT',
      packages=['battlerite_client'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
