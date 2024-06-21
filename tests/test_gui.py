import os


# set a vitrual framebuffer for headless actions runners.
# the whole thing is really hacky, but allows to run the code on actions on a
# virtual display under ubuntu
# compatibility issues are present, so this does not work under newwer python
# versions.
if os.name != "nt" and os.getenv("GITHUB_ACTIONS"):
    os.system('Xvfb :1 -screen 0 1600x1200x16  &')
    os.environ["DISPLAY"] = ":1.0"

# after that import simplegui and tkinter with it
import simplegui as sg

import sys
sys.path.insert(0, "./examples/DemoPrograms")
sys.path.insert(0, "../examples/DemoPrograms")

import time
import pytest
import platform




# patch the window read function to actually exit pytest controlled
class ExitException(Exception):
    pass

def exit_function(*_args, **_kwargs):
    time.sleep(1)
    raise ExitException()

sg.Window.read = exit_function



expected_to_not_work = False
if os.name != "nt" and os.getenv("GITHUB_ACTIONS") and (sys.version_info.minor >= 12 or platform.python_implementation() == "PyPy"):
    # skip tests if this matches
    # we might get
    # _tkinter.TclError: couldn't connect to display ":1.0"
    expected_to_not_work = True



@pytest.mark.skipif(expected_to_not_work, reason="Screen emulation in Actions not working on this configuration")
def test_demo_all_elements():
    import Demo_All_Elements
    with pytest.raises(ExitException):
        Demo_All_Elements.main()


