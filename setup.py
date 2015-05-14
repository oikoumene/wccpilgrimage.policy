from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='wccpilgrimage.policy',
      version=version,
      description="WCC Pilgrimage Policy",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Afterfive Technologies',
      author_email='holden@afterfivetech.com',
      url='http://github.com/oikoumene/',
      license='gpl',
      packages=find_packages(),
      namespace_packages=['wccpilgrimage'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity [grok, relations]',
          'plone.namedfile [blobs]',
          'collective.grok',
          'plone.app.referenceablebehavior',
          'collective.dexteritytextindexer',
          'plone.app.multilingual == 2.0',
          'plone.app.contenttypes == 1.1b3',
          'startupworks.pjp',
          'wccpilgrimagesite.app',
          'wccpilgrimagesite.theme',
          'z3c.jbot',
          'sc.social.like',
          'Products.ContentWellPortlets'
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': [
              'plone.app.testing',
           ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      setup_requires=["PasteScript"],
      paster_plugins=["templer.localcommands"],

      )
