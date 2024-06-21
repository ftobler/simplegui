import os

# set a vitrual framebuffer for headless actions runners.
if os.name != "nt" and os.getenv("GITHUB_ACTIONS"):
    os.system('Xvfb :1 -screen 0 1600x1200x16  &')
    os.environ["DISPLAY"] = ":0.0"

# after that import simplegui and tkinter with it
import simplegui as sg

import sys
sys.path.insert(0, "./examples/DemoPrograms")
sys.path.insert(0, "../examples/DemoPrograms")

import time
import pytest




# patch the window read function to actually exit pytest controlled
class ExitException(Exception):
    pass

def exit_function(*_args, **_kwargs):
    time.sleep(1)
    raise ExitException()

sg.Window.read = exit_function








def test_demo_all_elements():
    import Demo_All_Elements
    with pytest.raises(ExitException):
        Demo_All_Elements.main()


