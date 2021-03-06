from os import path
from setuptools import setup, find_packages

# Package meta-data.
NAME = "pogam"
AUTHOR = "Ludovic Tiako"
EMAIL = "ludovic.tiako@gmail.com"
DESCRIPTION = "A web scraper for (French) real estate listings."
URL = "https://github.com/ludaavics/pogam"
REQUIRES_PYTHON = ">=3.8.0"

REQUIRED = [
    "beautifulsoup4",
    "click",
    "click-log",
    "fake-useragent>=0.1.11",
    "flask>=1.1.1",
    "flask-sqlalchemy>=2.4.1",
    "requests>=2.22.0",
    "sqlalchemy>=1.3.10",
    "sqlalchemy-aurora-data-api==0.1.4",
]

EXTRAS = []

version = {}
here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    readme = f.read()

with open(path.join(here, "LICENSE")) as f:
    license = f.read()

with open(path.join(here, NAME, "__version__.py")) as f:
    exec(f.read(), version)
version = version["__version__"]

setup(
    name=NAME,
    version=version,
    description=DESCRIPTION,
    long_description=readme,
    long_description_content_type="text/x-rst",
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    entry_points="""
        [console_scripts]
        pogam=pogam.cli:cli
    """,
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,
)
