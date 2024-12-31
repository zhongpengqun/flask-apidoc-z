# coding=utf8
__author__ = 'Zhong.PengQun'

from setuptools import setup

setup(name='flask_doc_z',
      version='0.0.3',
      description='Simple Flask API doc generator，forked from https://github.com/ipconfiger/flask-apidoc',
      url='',
      author='Zhong.PengQun',
      author_email='',
      license='',
      packages=['flask_doc_z'],
      package_data = {
            "flask_doc_z": ["*.html", "*.gif"],
      },
      install_requires=[
          'flask','markdown'
      ],
      entry_points = {
        'console_scripts': ['fkapidoc=flask_doc_z.generator:main'],
      },
      zip_safe=False)