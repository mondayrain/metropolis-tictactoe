import os
import codecs
from setuptools import setup, find_packages
import metropolis_tictactoe

PATH = os.path
HERE = PATH.abspath(PATH.dirname(__file__))

requirements = codecs.open(PATH.join(HERE, 'requirements.txt'), 'r').read().split()
long_description = 'Modern remake of the class game Tic Tac Toe, using PyGame for UI and event handling. \
                   Features original music by Scott Stedman (www.scottstedman.com/category/music/releases) \
                   and photography by Stephen Morgan (www.instagram.com/discoveryphotos).'

setup(
    name = 'metropolis-tictactoe',
    version = '0.5',
    description = 'Modern PyGame remake of Tic Tac Toe',
    long_description= long_description,
    url = 'https://github.com/mondayrain/metropolis-tictactoe',
    author = 'Larissa Feng',
    author_email = 'hello@larissafeng.me',
    license = 'MIT License',
    packages = 'metropolis_tictactoe',
    install_requires = requirements,
    classifiers = [
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers :: End Users/Desktop',
        'Topic :: Games/Entertainment',
    ],
    keywords = 'tic tac toe, metropolis, game'
)
