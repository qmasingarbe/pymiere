import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
NAME = "pymiere"
URL = f'https://github.com/qmasingarbe/{NAME}'
VERSION = "0.37"

setup(name = NAME,
      packages = find_packages(),
      version = VERSION,
      license='MIT',
      description = "Pythonic automations for Adobe Premiere Pro.  Converts Python code to Adobe ExtendScript code and sends to/from Premiere Pro via HTTP and the `Pymiere Link` extension for Premiere (installed separately).",
      long_description=(HERE / "README.md").read_text(),
      long_description_content_type="text/markdown",
      author = 'Quentin Masingarbe',
      author_email = 'q.masingarbe@gmail.com',
      url = URL,
      download_url = f'{URL}/archive/{VERSION}.tar.gz',
      keywords = [NAME, "video", "Premiere", "Adobe", "Pymiere", "workflow", "automation", "Creative Cloud", "edit", "editor", "editing"],
      install_requires=['cleverdict>=1.7', 'requests>=2.25'],
      # https://pypi.org/classifiers/
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

# Update VERSION (above) then run the following from the command prompt:

# python -m pip install setuptools wheel twine
# python setup.py sdist
# python -m twine upload --repository testpypi dist/*

# Then:
# pip install -i https://test.pypi.org/simple/ pymiere

# And when you're ready to go fully public:
# python -m twine upload --repository pypi dist/*
