import pathlib
from setuptools import setup
from pymiere import __name__

HERE = pathlib.Path(__file__).parent
VERSION = "0.1"

setup(name = '__name__',
      packages = ['__name__'],
      version = VERSION,
      license='MIT',
      description='A data structure which allows both object attributes and dictionary keys and values to be used simultaneously and interchangeably.',
      long_description=(HERE / "README.md").read_text(),
      long_description_content_type="text/markdown",
      author = 'Quentin Masingarbe',
      author_email = 'q.masingarbe@gmail.com',
      url = f'https://github.com/qmasingarbe/{__name__}',
      download_url = f'{url}/archive/v_{VERSION}.tar.gz',
      keywords = [__name__, "video", "Premiere", "Adobe", "Pymiere", "workflow", "automation", "Creative Cloud", "edit", "editor", "editing"],
      install_requires=['cleverdict', 'requests', 'pysimplegui'],
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: Microsoft :: Windows :: Windows 10',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   'Topic :: Multimedia :: Video :: Non-Linear Editor',],)

# Run the following from the command prompt:

# python setup.py sdist
# python -m twine upload --repository testpypi dist/*
# python -m twine upload --repository pypi dist/*
