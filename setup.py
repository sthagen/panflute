"""A pythonic alternative to pandocfilters

See:
https://github.com/sergiocorreia/panflute
"""

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Import version number
version = {}
with open("panflute/version.py") as fp:
    exec(fp.read(), version)
version = version['__version__']

setup(
    name='panflute',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,

    description='Pythonic Pandoc filters',
    long_description=long_description,
    long_description_content_type='text/markdown',

    # The project's main homepage.
    url='https://github.com/sergiocorreia/panflute',
    project_urls={
        "Source": "https://github.com/sergiocorreia/panflute",
        "Documentation": "http://scorreia.com/software/panflute/",
        "Tracker": "https://github.com/sergiocorreia/panflute/issues",
    },

    # Author details
    author="Sergio Correia",
    author_email='sergio.correia@gmail.com',

    # Choose your license
    license='BSD3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',

        # Indicate who your project is intended for
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',

        'Operating System :: OS Independent',
        'Topic :: Text Processing :: Filters',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],

    # What does your project relate to?
    keywords='pandoc pandocfilters markdown latex',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),

    python_requires='>=3.6',
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'click >=6,<9',
        'pyyaml >=3,<7',
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,pypi]
    extras_require={
        'dev': [
            'configparser',
            'coverage',
            'flake8',
            'pandocfilters',
            'pytest-cov',
            'pytest',
            'requests',
        ],
        'pypi': [
            'docutils',
            'Pygments',
            'twine',
            'wheel',
        ],
        'extras': [
            "yamlloader>=1,<2",
        ],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    #package_data={
    #    'sample': ['package_data.dat'],
    #},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'panflute=panflute:main',
            'panfl=panflute:panfl',
        ],
    },
)
