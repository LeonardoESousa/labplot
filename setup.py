"""
This script (setup.py) will copy the matplotlib styles (*.mplstyle) into the
appropriate directory on your computer (OS dependent).
This code is based on a StackOverflow answer:
https://stackoverflow.com/questions/31559225/how-to-ship-or-distribute-a-matplotlib-stylesheet
"""

import atexit
import glob
import os
import shutil

import matplotlib
from setuptools import setup
from setuptools.command.install import install


def install_styles():
    # Find all style files
    stylefiles = glob.glob('styles/**/*.mplstyle', recursive=True)
    # Find stylelib directory (where the *.mplstyle files go)
    mpl_stylelib_dir = os.path.join(matplotlib.get_configdir(), "stylelib")
    if not os.path.exists(mpl_stylelib_dir):
        os.makedirs(mpl_stylelib_dir)
    # Copy files over
    print("Installing styles into", mpl_stylelib_dir)
    for stylefile in stylefiles:
        print(os.path.basename(stylefile))
        shutil.copy(
            stylefile,
            os.path.join(mpl_stylelib_dir, os.path.basename(stylefile)))


class PostInstallMoveFile(install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(install_styles)


# Get description from README
root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Labplot',
    version='0.0.1',
    author="Leonardo",
    author_email="leonardo.sousa137@gmail.com",
    description="My Matplotlib style sheets",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    keywords=[
        "matplotlib-style-sheets",
        "matplotlib-styles",
        "python"
    ],
    url="https://github.com/LeonardoESousa/Labplot/",
    install_requires=['matplotlib', ],
    cmdclass={'install': PostInstallMoveFile, },
)