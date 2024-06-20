import setuptools

def readme():
    try:
        with open('README.md', encoding="utf-8") as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
    name="simplegui",
    version="4.60.4",
    author="PySimpleGUI",  # alternative author
    author_email="PySimpleGUI@PySimpleGUI.org",  # alternative maintainer_email
    description="Fork of the LGPL3 version of PySimpleGUI",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="GUI UI tkinter Qt WxPython Remi wrapper simple easy beginner novice student graphics progressbar progressmeter",
    url="https://github.com/PySimpleGUI/PySimpleGUI",
    packages=setuptools.find_packages(exclude=('tests', 'docs', 'examples', 'readme_creator')),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Topic :: Multimedia :: Graphics",
        "Operating System :: OS Independent"
    ),
    install_requires=[
        "psgtray"
        # Add your dependencies here.
        # example:
        # 'numpy>=1.21.0,<2.0.0',
    ],
    entry_points={
        'gui_scripts': [
        ],
        'console_scripts': [
            # 'command=simpleui.main:main_func',
            # a^      b^      c^    d^
            # a => the command line argument
            # b => the package name
            # c => the file name in the package (same as imports)
            # d => the function to call
        ],
    },
)