""" setuptools distribution and installation script. """

from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup( name                 = "ws_epd",
       version              = "0.0.1",
       description          = 'TBD',
       long_description     = readme(),
       classifiers          = [
           'Development Status :: 3 - Alpha',
           'License :: OSI Approved :: MIT License',
           'Programming Language :: Python :: 2.7',
           'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
       ],
       keywords             = 'e-paper display, spi',
       url                  = 'https://github.com/hnikolov/ws_epd.git',
       author               = 'Hristo Nikolov',
       author_email         = 'h.n.nikolov@gmail.com',
       license              = 'MIT',
       packages             = [
           'ws_epd'
       ],
       install_requires     = [
           'Pillow'
       ],
       include_package_data = True,
       zip_safe             = False
    )