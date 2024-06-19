import setuptools

def readme():
    try:
        with open('README.md', encoding="utf-8") as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
    name="simpleui",
    version="4.60.4",
    author="PySimpleGUI",  # alternative author
    author_email="PySimpleGUI@PySimpleGUI.org",  # alternative maintainer_email
    description="Fork of the LGPL3 version of PySimpleGUI",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="GUI UI tkinter Qt WxPython Remi wrapper simple easy beginner novice student graphics progressbar progressmeter",
    url="https://github.com/PySimpleGUI/PySimpleGUI",
    packages=setuptools.find_packages(exclude=('tests', 'docs')),
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
    entry_points={
        'gui_scripts': [
            'psgissue=PySimpleGUI.PySimpleGUI:main_open_github_issue',
            'psgmain=PySimpleGUI.PySimpleGUI:_main_entry_point',
            'psgupgrade=PySimpleGUI.PySimpleGUI:_upgrade_entry_point',
            'psghelp=PySimpleGUI.PySimpleGUI:main_sdk_help',
            'psgver=PySimpleGUI.PySimpleGUI:main_get_debug_data',
            'psgsettings=PySimpleGUI.PySimpleGUI:main_global_pysimplegui_settings',
        ],},
)