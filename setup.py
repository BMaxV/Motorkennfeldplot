import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Motorkennfeldplot",
    version = "1.0",
    author = "Bruno Maximilian Voss",
    author_email = "bruno.m.voss@gmail.com",
    description = ("Plots a Fuelchart"
                                   "to the cheese shop a5 pypi.org."),
    license = "MIT",
    keywords = "exercise",
   
    packages=['Motorkennfeldplot'],
    #long_description=read('README'),
 #   classifiers=[
 #       "Development Status :: 3 - Alpha",
 #       "Topic :: Utilities",
 #       "License :: OSI Approved :: BSD License",
 #   ],
)
