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
# sys.path.insert(0, "../examples/DemoPrograms")

import time
import pytest
import platform




# patch the window read function to actually exit pytest controlled
class ExitException(Exception):
    pass

def exit_function(*args, **_kwargs):
    # time.sleep(1)
    args[0].close()
    raise ExitException()

sg.Window.read = exit_function



expected_to_not_work = False
if os.name != "nt" and os.getenv("GITHUB_ACTIONS") and (sys.version_info.minor >= 12 or platform.python_implementation() == "PyPy"):
    # skip tests if this matches
    # we might get
    # _tkinter.TclError: couldn't connect to display ":1.0"
    expected_to_not_work = True



@pytest.mark.skip("This does not work reliably on actions")
@pytest.mark.skipif(expected_to_not_work, reason="Screen emulation in Actions not working on this configuration")
def test_demo_all_elements():
    import Demo_All_Elements
    with pytest.raises(ExitException):
        Demo_All_Elements.main()



def get_test_files():
    exclude = [
        "Browser_START_HERE_Demo_Programs_Browser",
        "Demo_Design_Pattern",
        "Demo_Menubar_Custom_and_Traditional",
        "Demo_Multiple_Windows_read_all_windows_25_lines",
        "Demo_Multithreaded_Write_Event_Value_MultiWindow",
        "Demo_Multi_Window_read_all_windows",
        "Demo_one_line_progress_meter",
        "Demo_PIL_Use",
        "Demo_Pong_Multiple_Platforms",
        "Demo_Table_CSV",
        "Demo_Titlebar_Custom_Async",
        "Demo_Window_Relative_Location",
        "Demo_Sort_Visualizer",
        "Demo_Graph_Drag_Rectangle",
        "Demo_Graph_Drawing_And_Dragging_Figures_2_Windows",
        "Demo_Animated_GIFs_Using_PIL",
        "Demo_Desktop_Widget_Email_Notification",
        "__init__",
    ]


    files = []
    for f in os.listdir("./examples/DemoPrograms"):
        if f.endswith(".py"):
            short = f.replace(".py", "")
            skip = False
            for excl in exclude:
                if short.startswith(excl):
                    skip = True
                    break
            if not skip:
                files.append(short)
    return files




import importlib


@pytest.mark.skipif(expected_to_not_work, reason="Screen emulation in Actions not working on this configuration")
@pytest.mark.parametrize("filename", get_test_files())
@pytest.mark.skip("This does not work")
def test_examples(filename):
    with pytest.raises(ExitException):
        module = importlib.import_module(filename)
        if hasattr(module, "main"):
            module.main()


