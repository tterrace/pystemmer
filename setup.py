#!/usr/bin/env python

from setuptools import setup, Extension
import os.path
import sys


def build_ext(*args, **kwargs):
    from Cython.Distutils import build_ext
    return build_ext(*args, **kwargs)


# Directory which libstemmer sources are unpacked in.
library_dir = 'libstemmer_c'

# Directories in libstemmer which contain libstemmer sources (ie, not
# examples, etc).
library_core_dirs = ('src_c', 'runtime', 'libstemmer', 'include')

src_files = [
    'libstemmer_c/src_c/stem_UTF_8_danish.c',
    'libstemmer_c/src_c/stem_UTF_8_dutch.c',
    'libstemmer_c/src_c/stem_UTF_8_english.c',
    'libstemmer_c/src_c/stem_UTF_8_finnish.c',
    'libstemmer_c/src_c/stem_UTF_8_french.c',
    'libstemmer_c/src_c/stem_UTF_8_german.c',
    'libstemmer_c/src_c/stem_UTF_8_hungarian.c',
    'libstemmer_c/src_c/stem_UTF_8_italian.c',
    'libstemmer_c/src_c/stem_UTF_8_norwegian.c',
    'libstemmer_c/src_c/stem_UTF_8_porter.c',
    'libstemmer_c/src_c/stem_UTF_8_portuguese.c',
    'libstemmer_c/src_c/stem_UTF_8_romanian.c',
    'libstemmer_c/src_c/stem_UTF_8_russian.c',
    'libstemmer_c/src_c/stem_UTF_8_spanish.c',
    'libstemmer_c/src_c/stem_UTF_8_swedish.c',
    'libstemmer_c/src_c/stem_UTF_8_turkish.c',
    'libstemmer_c/runtime/api.c',
    'libstemmer_c/runtime/utilities.c',
    'libstemmer_c/libstemmer/libstemmer_utf8.c',
    'src/Stemmer.pyx',
]

# Set the include path to include libstemmer.
include_dirs = ('src', os.path.join(library_dir, 'include'))

long_description = r"""

Stemming algorithms

PyStemmer provides access to efficient algorithms for calculating a
"stemmed" form of a word.  This is a form with most of the common
morphological endings removed; hopefully representing a common
linguistic base form.  This is most useful in building search engines
and information retrieval software; for example, a search with stemming
enabled should be able to find a document containing "cycling" given the
query "cycles".

PyStemmer provides algorithms for several (mainly european) languages,
by wrapping the libstemmer library from the Snowball project in a Python
module.

It also provides access to the classic Porter stemming algorithm for
english: although this has been superseded by an improved algorithm, the
original algorithm may be of interest to information retrieval
researchers wishing to reproduce results of earlier experiments.

""".strip()

version_str = '1.3.1'
setup(name = 'PyStemmer',
      version = version_str,
      author = 'Richard Boulton',
      author_email = 'richard@tartarus.org',
      maintainer = 'Richard Boulton',
      maintainer_email = 'richard@tartarus.org',
      url = 'http://snowball.tartarus.org/',
      download_url = 'http://snowball.tartarus.org/wrappers/PyStemmer-%s.tar.gz' % version_str,
      description = 'Snowball stemming algorithms, for information retrieval',
      long_description = long_description,
      platforms = ["any"],
      license = "MIT, BSD",
      keywords = [
      "python",
      "information retrieval",
      "language processing",
      "morphological analysis",
      "stemming algorithms",
      "stemmers"
      ],
      classifiers = [
      "Development Status :: 5 - Production/Stable",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: MIT License",
      "License :: OSI Approved :: BSD License",
      "Natural Language :: Danish",
      "Natural Language :: Dutch",
      "Natural Language :: English",
      "Natural Language :: Finnish",
      "Natural Language :: French",
      "Natural Language :: German",
      "Natural Language :: Italian",
      "Natural Language :: Norwegian",
      "Natural Language :: Portuguese",
      "Natural Language :: Russian",
      "Natural Language :: Spanish",
      "Natural Language :: Swedish",
      "Operating System :: OS Independent",
      "Programming Language :: C",
      "Programming Language :: Other",
      "Programming Language :: Python",
      "Programming Language :: Python :: 2",
      "Programming Language :: Python :: 2.6",
      "Programming Language :: Python :: 2.7",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.2",
      "Programming Language :: Python :: 3.3",
      "Programming Language :: Python :: 3.4",
      "Programming Language :: Python :: 3.5",
      "Programming Language :: Python :: 3.6",
      "Programming Language :: Python :: 3.7",
      "Topic :: Database",
      "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
      "Topic :: Text Processing :: Indexing",
      "Topic :: Text Processing :: Linguistic",
      ],
      setup_requires=['Cython>=0.28.5,<1.0'],
      ext_modules = [Extension('Stemmer', src_files,
                               include_dirs = include_dirs)],
      cmdclass = {'build_ext': build_ext}
     )
