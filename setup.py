from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.2'

long_description = (
    read('README.txt')
    + '\n' +
    'Contributors\n'
    '~~~~~~~~~~~~\n'
    + '\n' +
    read('docs/CONTRIBUTORS.txt')
    + '\n' +
    read('docs/HISTORY.txt')
    + '\n' +
   'Download\n'
   '--------\n'
    )

setup(name='collective.piwik.pageviews',
      version=version,
      description="Analytics support for pages using Piwik",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='pageviews analytics piwik',
      author='unweb.me',
      author_email='we@unweb.me',
      url='http://svn.plone.org/svn/collective/collective.piwik.pageviews',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.piwik'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'simplejson',
          'plone.app.registry',
          'collective.piwik.core'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
