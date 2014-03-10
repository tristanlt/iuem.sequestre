from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='iuem.sequestre',
      version=version,
      description="Produit plone destine a creer une webapp de sequestre numerique",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Tristan Le Toullec',
      author_email='tristan.letoullec@univ-brest.fr',
      url='http://www-iuem.univ-brest.fr/feiri',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['iuem'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'five.grok',
          'plone.app.dexterity [grok]',
          'plone.namedfile [blobs]',
          'collective.wtf',
          'collective.js.jqueryui',
          'collective.z3cform.datetimewidget',
          'collective.js.datatables',
          'plone.app.versioningbehavior',
	  'pycrypto'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      setup_requires=["PasteScript"],
      paster_plugins = ["ZopeSkel"],

      )
