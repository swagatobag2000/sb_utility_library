import os
import codecs
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.1'
DESCRIPTION = 'Convert your file as you wish'
long_description = ''
with codecs.open(os.path.join(here, "README.txt"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# Setting up
setup(
    name="sb_all_utility",
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='',
    author="Swagato Bag",
    author_email="swagatobag23@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=['Pillow', 'img2pdf', 'PyPDF2', 'pyttsx3'],
    keywords=['python', 'file', 'jpg to png', 'png to jpg', 'pdf to text', 'pdf to audio', 'image to pdf', 'json to csv'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows :: Windoes 10",
    ]
)