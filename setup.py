import os
from setuptools import setup, find_packages

NAME = "pymiere"
URL = 'https://github.com/qmasingarbe/{}'.format(NAME)
VERSION = "1.4.1"

with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as f:
    long_description = f.read()

setup(name=NAME,
      packages=find_packages(),
      version=VERSION,
      license='GNU',
      description="Pythonic automations for Adobe Premiere Pro. Require the `Pymiere Link` extension for Premiere (installed separately).",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Quentin Masingarbe',
      author_email='q.masingarbe@gmail.com',
      url=URL,
      keywords=[
          NAME, "video", "Premiere", "Adobe", "Pymiere", "workflow", "automation", "Creative Cloud", "edit",
          "editor", "editing", "prproj", "premiere pro"
      ],
      install_requires=['requests>=2.25'],
      # https://pypi.org/classifiers/
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                   'Natural Language :: English',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: MacOS',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   'Topic :: Multimedia :: Video',
                   'Topic :: Multimedia :: Video :: Non-Linear Editor']
)

# Update VERSION (above) then run the following from the command prompt:

# python -m pip install setuptools wheel twine
# python setup.py sdist
# python -m twine upload --repository pypi dist/*

# To test:
# pip install pymiere
