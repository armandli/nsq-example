from setuptools import setup, find_packages

setup(
  name='example',
  version='0.0.1',
  description='NSQ Example',
  authors='senseis',
  author_emails='senseisworkspace@gmail.com',
  url='https://github.com/armandli/nsq-example',
  packages=find_packages(exclude=['playground']),
  package_data={},
  data_files={},
  install_requires=[
    'pynsq',
  ],
  entry_points={
    'console_scripts':[]
  },
  scripts=[]
)
