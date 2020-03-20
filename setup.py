import sys
from cx_Freeze import setup,Executable
build_exe_options={"packages":["pyqt5"],"excludes":["tkinter"]}
if sys.platform=="win32":
    base="Win32GUI"

setup(name="Index",version="0.1",description="Index Application",options={"build_exe":build_exe_options},executables=[Executable("Index.py",base=base)])